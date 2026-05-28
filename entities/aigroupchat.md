---
title: AIGroupChat
created: 2026-05-28
updated: 2026-05-28
type: entity
tags: [FastAPI, 群聊, 剧本生成, 导览, Responses API, MVP]
sources:
  - /home/admin/wiki/raw/Indox/AIGroupChat/docs/AIGroupChat技术文档.md
  - /home/admin/wiki/raw/Indox/AIGroupChat/backend/
  - /home/admin/wiki/raw/Indox/AIGroupChat/frontend/ai-group-chat-mvp/
  - /home/admin/wiki/raw/Indox/AIGroupChat/openapi/
---

# AIGroupChat

AIGroupChat 是一个面向“单活动 AI 群聊导览剧本”的技术验证项目。它把管理端活动/讲解点数据、机器人模板、静态剧本生成、剧本发布校验，以及运行时用户插话回复串成一个完整闭环。

## 项目概述

- **后端框架**: FastAPI
- **核心协议**: Responses API
- **数据边界**: 一个群聊实例只绑定一个活动，剧本中的讲解点卡片只保存 `tourPointId`
- **主要形态**: 后端接口 + 内置测试页 + 静态 MVP 前端示例 + OpenAPI 描述
- **目标闭环**: 管理端讲解点读取 → 机器人模板配置 → 静态剧本生成/发布 → 运行时插话“托住 + 绕回”

## 项目结构

```text
AIGroupChat/
├── backend/
│   ├── main.py                         # FastAPI 入口
│   ├── routes/ai_group_chat.py         # 主业务路由
│   ├── services/
│   │   ├── admin_api_client.py         # 管理端活动/讲解点读取
│   │   ├── admin_auth_service.py       # 管理端自动登录
│   │   ├── llm_responses_service.py    # Responses API 适配
│   │   ├── bot_config_store.py         # 机器人模板文件存储
│   │   └── script_store.py             # 剧本文件存储/发布
│   ├── data/ai_chat_group/             # 模板与剧本持久化
│   └── static/ai-chat-group.html       # 后端内置手工测试页
├── frontend/ai-group-chat-mvp/         # 无构建依赖的静态前端示例
├── docs/AIGroupChat技术文档.md         # 功能说明
└── openapi/                            # 后端与生成相关 OpenAPI 文件
```

## 核心系统架构

### 1. [[aigroupchat-script-generation-system]]
- 从管理端读取活动与讲解点数据
- 结合机器人模板、生成模板与 source options 构造模型输入
- 输出 `ai-chat-group-script.v0.3` 剧本并做结构校验

### 2. [[aigroupchat-runtime-reply-system]]
- 运行时只使用“已推出”的可见上下文
- 支持 `runtime/reply` 与 `hold-and-resume` 两类接口
- 用户插话不会打乱主剧情、必推讲解点顺序或未来内容

### 3. [[aigroupchat-storage-and-admin-source-system]]
- 管理端活动源读取、自动登录、401/403 失败重登
- 机器人模板 JSON 文件存储
- 剧本文件存储、索引、发布与归档

## 技术特点

1. **单活动绑定**：群聊实例只读一个活动下的讲解点，降低数据边界复杂度
2. **剧本卡片去实体化**：卡片只存 `tourPointId`，真实资源仍回到正式讲解点数据源读取
3. **结构化模型输出**：通过 Responses API `json_schema` 约束剧本生成结果
4. **MVP 双前端形态**：后端自带测试页，另有纯静态前端复现用户侧最小闭环
5. **发布链路完整**：剧本支持草稿、列表、读取、更新、发布、校验与同活动旧版本归档

## 关键接口

- `GET /api/ai-group-chat/admin-source/default-activity-id`
- `GET /api/ai-group-chat/admin-source/activity`
- `GET/PUT /api/ai-group-chat/bot-templates`
- `POST /api/ai-group-chat/config-generation/preview`
- `GET/POST/PUT /api/ai-group-chat/scripts...`
- `POST /api/ai-group-chat/scripts/{scriptId}/publish`
- `POST /api/ai-group-chat/scripts/validate`
- `POST /api/ai-group-chat/runtime/reply`
- `POST /api/ai-group-chat/runtime/hold-and-resume`
- `GET /api/ai-group-chat/llm/probe`

## 相关页面

- [[aigroupchat-script-generation-system]] — 剧本生成、Schema、configSet 组装与校验
- [[aigroupchat-runtime-reply-system]] — 运行时插话回复、托住绕回、可见上下文边界
- [[aigroupchat-storage-and-admin-source-system]] — 管理端数据读取、模板/剧本文件存储与发布
- [[technical-documentation]] — 技术文档结构化写作
