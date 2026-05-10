---
name: teambition-status-checker
description: 自动监控 Teambition 任务状态，确保主任务进度与子任务保持同步，并生成日期命名的 Markdown 报告。
---

# Teambition 任务状态检查器 (Teambition Status Checker)

此技能用于自动化巡检 Teambition 中的项目进度，通过主子任务的状态权重对比，识别进度落后、遗漏启动等风险。

## 主要功能

- **双队列状态映射**：为主任务和子任务配置独立的进度等级。
- **智能提醒**：
  - `⚠️ [建议更新]`：主任务落后于所有子任务的最小进度。
  - `⚠️ [子项目待更新]`：存在尚未启动（待处理）的子任务。
- **时间自动转换**：将任务中的“实际上线时间”自动转换为东八区（UTC+8）。
- **Markdown 报告生成**：自动生成以日期命名的详细检查报告。

## 何时使用

- 需要确保“数创总需求池”或其他项目的进度准确反映在 Teambition 上时。
- 每日/每周进行项目巡检，识别进度瓶颈。
- 需要将复杂的 Teambition 任务关系整理成清晰的 Markdown 文档时。

## 如何使用

### 1. 配置 (config.json)

确保 `skills/teambition-status-checker/config.json` 中的 `headers` (包含 Cookie) 是最新的。

### 2. 执行检查

直接运行 Python 脚本：

```bash
python3 skills/teambition-status-checker/scripts/teambition_checker.py
```

### 3. 查看结果

检查完成后，当前目录下会生成一个类似 `2026-05-10_teambition_status_report.md` 的文件。

## 注意事项

- **认证失效**：如果收到 401 错误，请从浏览器复制最新的 Cookie 更新到 `config.json`。
- **过滤逻辑**：目前默认过滤“取消”状态的任务。
- **依赖项**：需要 Python 3 环境及 `requests` 库。
