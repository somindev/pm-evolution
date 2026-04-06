# PM Evolution

产品经理的进化工具集 — Claude Code 技能仓库。

## 技能分类

### 📋 需求与规划
- `promptx` — Prompt 工程框架，包含 57+ 精选框架

### 🎨 产品设计
- 待补充...

### 🎬 媒体处理
- `lj-video-download` — 视频下载技能，支持小红书、B站、YouTube、抖音等 1000+ 平台

### 📖 学习工具
- `lj-explain-words` — 深度词汇学习，提供词源、语义和视觉拓扑分析

### 💻 代码编写
- 待补充...

### ✅ 测试验证
- 待补充...

## 目录结构

```
pm-evolution/
├── skills/
│   ├── promptx/           # Prompt 工程技能
│   ├── lj-video-download/ # 视频下载技能
│   └── lj-explain-words/  # 词汇学习技能
├── README.md
└── .gitignore
```

## 添加新技能

在 `skills/` 下创建新目录，放入符合 Claude Code 规范的 `SKILL.md` 文件。

## 使用

将技能链接到 Claude Code skills 目录即可使用：
```bash
ln -s /path/to/pm-evolution/skills/xxx ~/.claude/skills/xxx
```
