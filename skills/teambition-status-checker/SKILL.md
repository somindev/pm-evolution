---
name: teambition-status-checker
description: 自动监控 Teambition 任务状态，确保主任务进度与子任务保持同步，并生成 Markdown 和交互式 HTML 仪表盘报告。
---

# Teambition 任务状态检查器 (Teambition Status Checker)

此技能用于自动化巡检 Teambition 中的项目进度，通过主子任务的状态权重对比以及上线时间跟踪，识别进度落后、逾期风险及遗漏启动等问题。

## 主要功能

- **交互式 HTML 仪表盘**：除 Markdown 外，还会自动生成美观的 HTML 报告，支持多维度标签筛选、子任务折叠展示，并内置 Teambition 任务一键跳转超链接。采用外置模板引擎（`templates/report.html`），方便修改前端样式。
- **智能 Deadline 追踪**：解析“IT 计划上线时间”，自动比对当前日期，计算并标记：
  - `🚨 [警告超期]`：展示超期天数。
  - `⏰ [接近上线]`：展示距离上线的剩余天数（阈值为 15 天内）。
- **双队列状态映射与逻辑巡检**：
  - `⚠️ [建议更新]`：主任务落后于所有子任务的最小进度。
  - `⚠️ [子项目待更新]`：存在尚未启动（待处理）的子任务。
  - `⚠️ [暂缓]`：主子任务中存在任意暂缓状态。
- **时间自动转换**：将任务中的“计划/实际上线时间”自动转换为东八区（UTC+8）。若未填写则统一提示为“上线时间待添加”。

## 何时使用

- 需要确保“数创总需求池”或其他项目的进度准确反映在 Teambition 上时。
- 每日/每周进行项目巡检，快速筛选出逾期风险项目或未处理事项。
- 需要将复杂的 Teambition 任务关系生成清晰、可视化且可交互的汇报视图时。

## 如何使用

### 1. 配置 (config.json)

确保 `skills/teambition-status-checker/config.json` 中的 `headers` (包含最新的 Cookie) 和各项 ID (如 project_id, tasklist_id, customfield_id) 配置正确。

### 2. 执行检查

直接运行 Python 脚本：

```bash
python3 skills/teambition-status-checker/scripts/teambition_checker.py
```

### 3. 查看结果

检查完成后，当前目录下会生成两份以日期命名的报告：
- **Markdown 报告**：如 `2026-05-10_teambition_status_report.md`
- **HTML 仪表盘**：如 `2026-05-10_teambition_status_report.html` (可在浏览器中直接打开交互使用)

## 注意事项

- **认证失效**：如果收到 401 错误，请从浏览器复制最新的 Cookie 更新到 `config.json`。
- **过滤逻辑**：目前默认过滤“取消”状态的任务（主任务及子任务）和所有已关闭的子任务。
- **自定义字段变动**：如果 Teambition 接口的自定义字段 ID 发生变化，需在 `config.json` 中同步更新 `plan_field_id` 和 `actual_field_id`。
- **依赖项**：需要 Python 3 环境及 `requests` 库（无需其他前端框架，HTML 报告依赖浏览器原生支持）。
