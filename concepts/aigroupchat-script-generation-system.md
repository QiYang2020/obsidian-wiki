---
title: AIGroupChat 剧本生成系统
created: 2026-05-28
updated: 2026-05-28
type: concept
tags: [FastAPI, 剧本生成, Responses API, JSON Schema, 导览]
sources:
  - /home/admin/wiki/raw/Indox/AIGroupChat/docs/AIGroupChat技术文档.md
  - /home/admin/wiki/raw/Indox/AIGroupChat/backend/routes/ai_group_chat.py
  - /home/admin/wiki/raw/Indox/AIGroupChat/backend/services/llm_responses_service.py
---

# AIGroupChat 剧本生成系统

该系统负责把单活动讲解点数据、机器人模板和运营配置转成结构化群聊剧本，当前主输出版本为 `ai-chat-group-script.v0.3`。

## 系统组成

### 1. 生成入口
**主要接口**: `POST /api/ai-group-chat/config-generation/preview`

**主要输入**:
- `activityId`
- `botTemplateIds` 或直接传入 `botTemplates`
- `generationTemplate`
- `listedTourPointPolicy`
- `sourceOptions`
- `dialogueOptions`
- `inlineAdminSource`（技术验证时可直接注入活动快照）

### 2. 数据准备
**关键函数**:
- `_resolve_source()`：决定使用管理端实时读取还是 inline 快照
- `_normalize_source()`：归一化活动、展馆、展厅、讲解点数据
- `_compact_activity()` / `_compact_tour_point()`：压缩成更适合模型消费的输入结构

**归一化结果**:
- 活动摘要
- 展馆/展厅摘要
- 已筛选讲解点列表
- `sourceHash`

### 3. 模型调用构建
**关键函数**:
- `_build_generation_call()`
- `_script_schema()`
- `ResponsesLLMService.generate_json()`

**Responses API 特征**:
- 直接 POST 到 `{LLM_BASE_URL}/responses`
- 传 `instructions`
- 传 `input`
- 传 `thinking`
- 通过 `text.format.type=json_schema` 约束结构化输出

### 4. 剧本组装与校验
**关键函数**:
- `_assemble_config_set()`：兼容旧 `configSet` 形态
- `_assemble_script()`：组装 `ai-chat-group-script.v0.3`
- `_validate_script()`：结构校验、必推讲解点校验、引用合法性校验

## 剧本结构

顶层字段包括：
- `schemaVersion`
- `scriptId`
- `activityId`
- `activityName`
- `version`
- `status`
- `chatStyle`
- `bots`
- `generationTemplate`
- `runtimePolicy`
- `sourceRule`
- `groups`
- `sourceSnapshot`

其中 `groups[]` 是主要对话流结构，卡片消息通过 `tourPointId` 关联真实讲解点。

## 数据流

```text
activityId
  -> 读取管理端活动/讲解点数据
  -> 归一化 + 筛选 listed tour points
  -> 读取机器人模板
  -> 构造 instructions / input / JSON Schema
  -> Responses API 输出结构化内容
  -> 组装 configSet + script.v0.3
  -> 运行结构校验并返回预览结果
```

## 约束与边界

1. 单个群聊实例只绑定一个活动
2. 卡片只保存 `tourPointId`，不在剧本内固化真实资源内容
3. 讲解点筛选可控制是否只用 `enabled=true` 条目
4. 审核状态可选择仅记录或强制 `APPROVED`
5. 生成结果必须通过脚本校验后才能进入后续保存/发布链路

## 验证重点

- `activityId` 与活动源一致
- `botTemplateIds` 能正确解析到机器人模板
- 生成结果可被 JSON Schema 接受
- `groups[]` 对 `tourPointId` 的引用都在当前活动讲解点集合内
- 必推讲解点全部被覆盖

## 相关页面

- [[aigroupchat]] — 项目总览
- [[aigroupchat-storage-and-admin-source-system]] — 源数据与持久化
- [[aigroupchat-runtime-reply-system]] — 运行时插话回复
