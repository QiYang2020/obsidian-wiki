---
title: Unity SVN 文件清理
updated: 2026-04-11
type: concepts
sources:
  - raw/inbox/chatgpt_personal_backup_2026-04-10_md/Unity/Unity SVN 文件清理_67ea5661-34cc-800d-9b12-fd828c573227_20250331_164625.md
---

# Unity SVN 文件清理

上传 Unity 工程到 SVN 时，以下文件/文件夹可以安全删除或在 `.svnignore` 中忽略：

| 文件夹 | 原因 |
|--------|------|
| **Library** | Unity 自动生成的编辑器缓存，可通过重新导入重建 |
| **Temp** | 运行时临时文件，重启 Unity 会自动清除 |
| **obj** | 编译时生成的中间文件 |
| **Build** | 编译后的游戏文件（除非有特殊需要） |
| **Logs** | Unity 运行日志 |
| **UserSettings 部分配置** | 本地设置和缓存文件，因人而异 |

## 实践建议

- 在项目根目录配置 `.svnignore`，将上述目录列入
- Library 是最大的体积来源，忽略它能显著减小仓库体积
- 如果团队需要共享某些 UserSettings，可选择性保留特定子文件
