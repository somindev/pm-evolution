import json
import requests
import time
from datetime import datetime, timedelta, timezone
import sys
import os

class TeambitionClient:
    def __init__(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        
        self.headers = self.config['headers']
        self.base_url = self.config['api_base_url']
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def query_tasks(self):
        url = f"{self.base_url}/my/api/tasks/query"
        payload = self.config['query_params']
        response = self.session.post(url, json=payload, timeout=30)
        self._check_response(response)
        return response.json()

    def get_task_detail(self, task_id):
        # Adding a small delay to avoid rate limiting
        time.sleep(0.1)
        url = f"{self.base_url}/api/tasks/{task_id}"
        response = self.session.get(url, timeout=30)
        self._check_response(response)
        return response.json()

    def _check_response(self, response):
        # Check HTTP status code
        if response.status_code == 401:
            self._handle_auth_error()
        
        # Check for error code in JSON body (some APIs return 200 with error body)
        try:
            data = response.json()
            if isinstance(data, dict):
                code = data.get('code')
                if code == 401 or str(code) == "401":
                    self._handle_auth_error()
        except Exception:
            pass

        response.raise_for_status()

    def _handle_auth_error(self):
        print("\nError: 401 Unauthorized. Your Teambition Cookie or Token may have expired.")
        print("Please update the 'headers' in config.json with a fresh Cookie.")
        sys.exit(1)

class StatusAnalyzer:
    def __init__(self, main_levels, sub_levels, actual_field_id, plan_field_id):
        self.main_levels = main_levels
        self.sub_levels = sub_levels
        self.actual_field_id = actual_field_id
        self.plan_field_id = plan_field_id

    def get_main_level(self, status_name):
        return self.main_levels.get(status_name, 0)

    def get_sub_level(self, status_name):
        return self.sub_levels.get(status_name, 0)

    def format_time_to_utc8(self, iso_string):
        if not iso_string:
            return "N/A"
        try:
            dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
            utc8_dt = dt.astimezone(timezone(timedelta(hours=8)))
            return utc8_dt.strftime('%Y-%m-%d %H:%M:%S')
        except Exception:
            return iso_string

    def parse_to_utc8_datetime(self, iso_string):
        if not iso_string or iso_string == "上线时间待添加":
            return None
        try:
            dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
            return dt.astimezone(timezone(timedelta(hours=8)))
        except Exception:
            return None

    def get_custom_field_value(self, task_detail, field_id):
        custom_fields = task_detail.get('customfields', [])
        for field in custom_fields:
            if field.get('_customfieldId') == field_id:
                value_obj = field.get('value', {})
                if isinstance(value_obj, dict):
                    return value_obj.get('title', "上线时间待添加")
                elif isinstance(value_obj, list) and len(value_obj) > 0:
                    return value_obj[0].get('title', "上线时间待添加")
        return "上线时间待添加"

    def analyze_task(self, task_detail, subtask_details):
        main_status_obj = task_detail.get('taskflowstatus') or task_detail.get('tfsInfo') or {}
        main_status = main_status_obj.get('name', 'Unknown')
        main_level = self.get_main_level(main_status)
        
        is_main_suspended = (main_status == "暂缓")
        has_suspended_subtask = False
        
        # IT Plan Time check
        raw_plan_time = self.get_custom_field_value(task_detail, self.plan_field_id)
        plan_time_str = self.format_time_to_utc8(raw_plan_time) if raw_plan_time != "上线时间待添加" else "上线时间待添加"
        plan_dt = self.parse_to_utc8_datetime(raw_plan_time)
        
        time_status = ""
        days_diff = None  # positive = overdue days, negative = days remaining
        if plan_dt and main_level < 15:
            now = datetime.now(timezone(timedelta(hours=8)))
            diff = (now - plan_dt).days
            days_diff = diff  # positive = overdue, negative = remaining
            if now > plan_dt:
                time_status = "警告超期"
            elif plan_dt <= now + timedelta(days=15):
                time_status = "接近上线"

        subtask_info = []
        max_sub_level_mapped = 0
        
        for sub in subtask_details:
            sub_status_obj = sub.get('taskflowstatus') or sub.get('tfsInfo') or {}
            sub_status = sub_status_obj.get('name', 'Unknown')
            
            # Ignore subtasks that are cancelled or closed
            if sub_status in ["取消", "任务关闭"]:
                continue
                
            if sub_status == "暂缓":
                has_suspended_subtask = True
                
            sub_level = self.get_sub_level(sub_status)
            raw_online_time = self.get_custom_field_value(sub, self.actual_field_id)
            online_time = self.format_time_to_utc8(raw_online_time) if raw_online_time != "上线时间待添加" else "上线时间待添加"
            # Get executor name
            executor_info = sub.get('executor') or sub.get('executorInfo') or {}
            executor_name = executor_info.get('name', '未分配')
            
            subtask_info.append({
                "name": sub.get('content', 'Unknown'),
                "status": sub_status,
                "level": sub_level,
                "online_time": online_time,
                "executor": executor_name
            })
            
            if sub_level > max_sub_level_mapped:
                max_sub_level_mapped = sub_level
        
        # Get main task executor
        main_executor_info = task_detail.get('executor') or task_detail.get('executorInfo') or {}
        main_executor = main_executor_info.get('name', '未分配')

        # Logic: if subtask progress is ahead of main task
        max_sub_level = max_sub_level_mapped
        min_sub_level = min(sub['level'] for sub in subtask_info) if subtask_info else 0
        
        # Rule 1: Only suggest update if main task is behind ALL subtasks
        need_update = main_level < min_sub_level and subtask_info
        
        # Rule 2: Check for To-do subtasks
        has_todo_subtask = any(sub['status'] == "待处理" for sub in subtask_info)
        
        reason = ""
        if need_update:
            reason = f"主任务状态({main_status} - 等级 {main_level}) 落后于所有子任务的最小进度({min_sub_level})。"
        
        return {
            "main_task": task_detail.get('content', 'Unknown'),
            "main_status": main_status,
            "main_level": main_level,
            "main_executor": main_executor,
            "plan_time": plan_time_str,
            "time_status": time_status,
            "days_diff": days_diff,
            "task_id": "",  # filled in main()
            "subtasks": subtask_info,
            "max_sub_level": max_sub_level,
            "min_sub_level": min_sub_level,
            "need_update": need_update,
            "has_todo": has_todo_subtask,
            "is_suspended": is_main_suspended or has_suspended_subtask,
            "reason": reason
        }

def get_task_priority(result):
    """Return sort priority: lower number = higher urgency."""
    if result['time_status'] == "警告超期":
        return 0
    if result['time_status'] == "接近上线":
        return 1
    if result['is_suspended']:
        return 2
    if result['need_update']:
        return 3
    if result['has_todo']:
        return 4
    return 5

def get_task_badges(result):
    """Return list of (label, css_class) tuples."""
    badges = []
    if result['time_status'] == "警告超期":
        badges.append(("🚨 警告超期", "badge-overdue"))
    elif result['time_status'] == "接近上线":
        badges.append(("⏰ 接近上线", "badge-approaching"))
    if result['is_suspended']:
        badges.append(("暂缓", "badge-suspended"))
    if result['need_update']:
        badges.append(("建议更新", "badge-update"))
    if result['has_todo']:
        badges.append(("子项目待更新", "badge-todo"))
    if not badges:
        badges.append(("正常", "badge-ok"))
    return badges

def generate_html_report(all_results, html_filename, project_name, report_date):
    from html import escape

    # ── Locate template ────────────────────────────────────────────
    script_dir    = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(os.path.dirname(script_dir), "templates", "report.html")
    if not os.path.exists(template_path):
        print(f"⚠️  HTML 模板未找到: {template_path}，跳过 HTML 报告生成。")
        return

    with open(template_path, encoding='utf-8') as f:
        template = f.read()

    # ── Sort & counts ──────────────────────────────────────────────
    sorted_results = sorted(all_results, key=get_task_priority)
    total      = len(sorted_results)
    overdue    = sum(1 for r in sorted_results if r['time_status'] == "警告超期")
    approaching= sum(1 for r in sorted_results if r['time_status'] == "接近上线")
    need_update= sum(1 for r in sorted_results if r['need_update'])
    todo       = sum(1 for r in sorted_results if r['has_todo'] and not r['need_update'])
    suspended  = sum(1 for r in sorted_results if r['is_suspended'])
    normal     = sum(1 for r in sorted_results if get_task_priority(r) == 5)

    # ── Helper: days chip ──────────────────────────────────────────
    def days_label(result):
        d = result.get('days_diff')
        if d is None:
            return ""
        if result['time_status'] == "警告超期":
            return f'<span class="days-chip chip-overdue">超期 {d} 天</span>'
        elif result['time_status'] == "接近上线":
            return f'<span class="days-chip chip-approaching">还剩 {-d} 天</span>'
        return ""

    # ── Helper: badge HTML ─────────────────────────────────────────
    def render_badges(result):
        html = ""
        for lbl, cls in get_task_badges(result):
            key = cls.replace("badge-", "")
            html += f'<span class="badge {cls}" data-badge="{key}">{escape(lbl)}</span>'
        html += days_label(result)
        return html

    # ── Helper: badge key order for filter bar ─────────────────────
    def get_all_badge_keys(results):
        seen, keys = set(), []
        order = ["overdue", "approaching", "suspended", "update", "todo", "ok"]
        label_map = {
            "overdue": "🚨 警告超期", "approaching": "⏰ 接近上线",
            "suspended": "暂缓", "update": "建议更新",
            "todo": "子项目待更新", "ok": "正常"
        }
        for k in order:
            for r in results:
                for _, cls in get_task_badges(r):
                    key = cls.replace("badge-", "")
                    if key == k and key not in seen:
                        seen.add(key)
                        keys.append((key, label_map.get(key, key)))
        return keys

    # ── Helper: subtask rows ───────────────────────────────────────
    def render_subtasks(subtasks):
        if not subtasks:
            return '<p class="no-subtasks">（无有效子任务）</p>'
        rows = []
        for sub in subtasks:
            done = sub['level'] >= 15
            icon = "✅" if done else "⏳"
            rows.append(
                f'<div class="subtask-row {"subtask-done" if done else ""}">'
                f'<span class="sub-icon">{icon}</span>'
                f'<div class="sub-info">'
                f'<span class="sub-status">{escape(sub["status"])}</span>'
                f'<span class="sub-name">{escape(sub["name"])}</span>'
                f'</div>'
                f'<div class="sub-meta">'
                f'<span>👤 {escape(sub["executor"])}</span>'
                f'<span>🚀 {escape(sub["online_time"])}</span>'
                f'</div></div>'
            )
        return "\n".join(rows)

    # ── Build task cards HTML ──────────────────────────────────────
    def render_cards(results):
        cards = []
        for i, r in enumerate(results):
            prio = get_task_priority(r)
            card_cls = "task-card " + (
                "card-overdue"    if prio == 0 else
                "card-approaching"if prio == 1 else
                "card-suspended"  if prio == 2 else
                "card-warn"       if prio <= 4 else
                "card-ok"
            )
            badge_keys  = " ".join(cls.replace("badge-", "") for _, cls in get_task_badges(r))
            reason_html = f'<p class="reason">⚡ {escape(r["reason"])}</p>' if r.get("reason") else ""
            todo_html   = '<p class="todo-warn">⚠️ 存在处于"待处理"状态的子任务</p>' if r.get("has_todo") else ""

            task_id   = r.get('task_id', '')
            task_url  = f"https://www.teambition.com/task/{task_id}" if task_id else "#"
            sub_count = len(r['subtasks'])
            toggle    = (f'<button class="subtask-toggle" onclick="toggleSub(this)" aria-expanded="true">'
                         f'▾ {sub_count} 个子任务</button>') if sub_count else ""

            cards.append(
                f'<div class="{card_cls}" data-badges="{badge_keys}" style="animation-delay:{i*0.04:.2f}s">'
                f'<div class="card-header">'
                f'<div class="card-title-row">'
                f'<h3 class="card-title"><a class="card-title-link" href="{task_url}" target="_blank">{escape(r["main_task"])}</a></h3>'
                f'<div class="badges">{render_badges(r)}</div>'
                f'</div>'
                f'<div class="card-meta-row">'
                f'<span class="meta-item">👤 <strong>{escape(r["main_executor"])}</strong></span>'
                f'<span class="meta-item">📋 {escape(r["main_status"])}</span>'
                f'<span class="meta-item">📅 IT计划上线：{escape(r["plan_time"])}</span>'
                f'{toggle}'
                f'</div></div>'
                f'{reason_html}{todo_html}'
                f'<div class="subtasks">{render_subtasks(r["subtasks"])}</div>'
                f'</div>'
            )
        return "\n".join(cards)

    # ── Build filter buttons HTML ──────────────────────────────────
    filter_btns = '<button class="filter-btn active" data-filter="all">全部</button>'
    for key, label in get_all_badge_keys(sorted_results):
        filter_btns += f'<button class="filter-btn" data-filter="{key}">{escape(label)}</button>'

    # ── Fill template placeholders ─────────────────────────────────
    generated_at = datetime.now(timezone(timedelta(hours=8))).strftime('%Y年%m月%d日 %H:%M')
    html = (template
        .replace("{{PROJECT_NAME}}",    escape(project_name))
        .replace("{{REPORT_DATE}}",     report_date)
        .replace("{{GENERATED_AT}}",    generated_at)
        .replace("{{COUNT_TOTAL}}",     str(total))
        .replace("{{COUNT_OVERDUE}}",   str(overdue))
        .replace("{{COUNT_APPROACHING}}",str(approaching))
        .replace("{{COUNT_SUSPENDED}}", str(suspended))
        .replace("{{COUNT_UPDATE}}",    str(need_update))
        .replace("{{COUNT_TODO}}",      str(todo))
        .replace("{{COUNT_NORMAL}}",    str(normal))
        .replace("{{FILTER_BUTTONS}}",  filter_btns)
        .replace("{{TASK_CARDS}}",      render_cards(sorted_results))
    )

    with open(html_filename, 'w', encoding='utf-8') as f:
        f.write(html)



def main():
    # Use config in the same directory as the script if not found in root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = "config.json"
    
    if not os.path.exists(config_path):
        # Try skill directory path
        config_path = os.path.join(os.path.dirname(script_dir), "config.json")
    
    if not os.path.exists(config_path):
        print(f"Error: config.json not found in root or {os.path.dirname(script_dir)}")
        return

    client = TeambitionClient(config_path)
    analyzer = StatusAnalyzer(
        client.config['main_status_levels'], 
        client.config['subtask_status_levels'], 
        client.config['custom_field_id'],
        client.config['plan_field_id']
    )
    target_project = client.config.get('target_project', "数创总需求池")

    print(f"--- 正在查询任务列表 (项目: {target_project}) ---")
    response_data = client.query_tasks()
    
    if isinstance(response_data, dict) and 'data' in response_data:
        tasks = response_data['data'].get('result', [])
    else:
        tasks = response_data if isinstance(response_data, list) else []
    
    # Filter tasks by project name
    filtered_tasks = []
    for t in tasks:
        if not isinstance(t, dict): continue
        # Try different paths for project name
        p_info = t.get('projectInfo') or t.get('project') or {}
        p_name = p_info.get('name')
        if p_name == target_project:
            filtered_tasks.append(t)
    
    if not filtered_tasks:
        print(f"未找到项目 '{target_project}' 下的待办任务。")
        # Optional: print available projects for debugging
        all_p = set()
        for t in tasks:
            if not isinstance(t, dict): continue
            p_i = t.get('projectInfo') or t.get('project') or {}
            all_p.add(p_i.get('name'))
        if all_p:
            print(f"发现的项目有: {', '.join(filter(None, all_p))}")
        return

    print(f"找到 {len(filtered_tasks)} 个主任务，正在检查详情...")
    
    # Prepare Markdown report and results list
    all_results = []
    report_lines = []
    current_date = datetime.now().strftime('%Y-%m-%d')
    report_filename = f"{current_date}_teambition_status_report.md"
    
    report_lines.append(f"# Teambition 任务状态检查报告 ({current_date})")
    report_lines.append(f"**项目**: {target_project}")
    report_lines.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("\n---\n")

    for task in filtered_tasks:
        task_id = task.get('_id') or task.get('id')
        try:
            detail = client.get_task_detail(task_id)
            
            # Check for '取消' status early to avoid extra subtask queries
            main_status_obj = detail.get('taskflowstatus') or detail.get('tfsInfo') or {}
            main_status = main_status_obj.get('name', 'Unknown')
            if main_status == "取消":
                continue
                
            subtask_list = detail.get('subtasks', [])
            
            subtask_details = []
            for sub_brief in subtask_list:
                sub_id = sub_brief.get('_id') or sub_brief.get('id')
                sub_detail = client.get_task_detail(sub_id)
                subtask_details.append(sub_detail)
            
            result = analyzer.analyze_task(detail, subtask_details)
            result['task_id'] = task_id  # attach for hyperlinks
            
            # Build status mark
            marks = []
            icon = "✅"
            if result['time_status'] == "警告超期":
                marks.append("🚨 警告超期")
                icon = "⚠️"
            elif result['time_status'] == "接近上线":
                marks.append("⏰ 接近上线")
                icon = "⚠️"
            
            all_results.append(result)

            if result['is_suspended']:
                marks.append("暂缓")
                icon = "⚠️"
            if result['need_update']:
                marks.append("建议更新")
                icon = "⚠️"
            if result['has_todo']:
                marks.append("子项目待更新")
                icon = "⚠️"
            
            if marks:
                status_mark = f"{icon} [{' '.join(marks)}]"
            else:
                status_mark = "✅ [正常]"
                
            # Print to console
            print(f"{status_mark} 主任务: {result['main_task']}")
            
            # Append to Markdown report
            report_lines.append(f"### {status_mark} {result['main_task']}")
            report_lines.append(f"- **负责人**: {result['main_executor']}")
            report_lines.append(f"- **当前状态**: `{result['main_status']}` (等级 {result['main_level']})")
            report_lines.append(f"- **IT计划上线**: `{result['plan_time']}`")
            
            if result['subtasks']:
                report_lines.append("- **子任务详情**:")
                for sub in result['subtasks']:
                    sub_mark = "✅" if sub['level'] >= 15 else "⏳"
                    report_lines.append(f"    - {sub_mark} [{sub['status']}] {sub['name']} | 负责人: {sub['executor']} | 实际上线: {sub['online_time']}")
            else:
                report_lines.append("- (无子任务)")
                
            if result['reason']:
                report_lines.append(f"- **判定原因**: {result['reason']}")
            if result['has_todo']:
                report_lines.append(f"- **风险提示**: 存在处于'待处理'状态的子任务")
            
            report_lines.append("\n")
            
        except Exception as e:
            error_msg = f"处理任务 {task_id} 时出错: {e}"
            print(error_msg)
            report_lines.append(f"\n> ❌ {error_msg}\n")

    # Save Markdown report
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write("\n".join(report_lines))
    
    # Generate HTML report
    html_filename = report_filename.replace('.md', '.html')
    generate_html_report(all_results, html_filename, target_project, current_date)
    
    print(f"\n--- 检查完成 ---")
    print(f"Markdown 报告: {report_filename}")
    print(f"HTML 报告:     {html_filename}")

if __name__ == "__main__":
    main()
