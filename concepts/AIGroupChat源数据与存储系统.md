---
title: AIGroupChat 源数据与存储系统
created: 2026-05-28
updated: 2026-05-28
type: concept
tags: [FastAPI, 存储, 管理端, 文件存储, 发布链路]
sources:
  - /home/admin/wiki/raw/Indox/AIGroupChat/docs/AIGroupChat技术文档.md
  - /home/admin/wiki/raw/Indox/AIGroupChat/backend/config.py
  - /home/admin/wiki/raw/Indox/AIGroupChat/backend/services/script_store.py
---

# AIGroupChat 源数据与存储系统

该系统负责从管理端读取活动/讲解点数据，并以文件形式持久化机器人模板与静态剧本，是 AIGroupChat 技术验证阶段的数据底座。

## 系统组成

### 1. 管理端源数据读取
**关键服务**:
- `AdminAPIClient`
- `AdminAuthService`

**行为**:
- 读取点亮艺术管理端活动及讲解点接口
- 支持按 `activityId` 限定单活动
- 支持固定 token 或账号密码自动登录
- 遇到 401/403 时清空内存 token 并重新登录一次
- 会校验返回 `activity.id` 是否与请求活动一致

### 2. 机器人模板存储
**默认文件**:
```text
backend/data/ai_chat_group/bot_templates.json
```

**服务**:
- `BotConfigStore.list_bot_templates()`
- `BotConfigStore.save_bot_templates()`

**校验规则**:
- `botId` 不能为空
- `botId` 不能重复

### 3. 剧本文件存储
**默认目录**:
```text
backend/data/ai_chat_group/scripts/
```

**实现方式**:
- 一个剧本对应一个 JSON 文件
- 维护一个 `index.json` 提供列表查询
- `save_script()` 负责写文件并更新索引
- `publish_script()` 会把同活动其他已发布剧本归档为 `archived`

### 4. 配置来源
**配置内容**:
- `LLM_BASE_URL` / `LLM_MODEL` / `LLM_API_KEY`
- `ADMIN_API_BASE_URL` / `ADMIN_API_PREFIX`
- `ADMIN_API_TOKEN` 或 `ADMIN_API_USERNAME` + `ADMIN_API_PASSWORD`
- `AI_CHAT_GROUP_DEFAULT_ACTIVITY_ID`

配置文件中还会优先加载 `backend/.env.local`，且不覆盖已有环境变量。

## 数据流

```text
管理端活动源
  -> AdminAPIClient 拉取
  -> AdminAuthService 处理 token
  -> 归一化活动/讲解点结构
  -> 供剧本生成与校验复用

机器人模板/剧本
  -> 本地 JSON 文件持久化
  -> index.json 提供列表索引
  -> 发布时对同活动旧版本做 archived 处理
```

## 适用阶段与限制

- 当前是技术验证/MVP 阶段的数据层
- 文件存储简单直观，但更适合单实例服务
- 尚未引入数据库、对象存储或多实例并发一致性机制

## 相关页面

- [[AIGroupChat群聊导览剧本系统]] — 项目总览
- [[AIGroupChat剧本生成系统]] — 静态剧本生成
