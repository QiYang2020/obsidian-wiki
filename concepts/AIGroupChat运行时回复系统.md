---
title: AIGroupChat 运行时回复系统
created: 2026-05-28
updated: 2026-05-28
type: concept
tags: [FastAPI, 运行时回复, 群聊, 上下文控制, 导览]
sources:
  - /home/admin/wiki/raw/Indox/AIGroupChat/docs/AIGroupChat技术文档.md
  - /home/admin/wiki/raw/Indox/AIGroupChat/backend/routes/ai_group_chat.py
  - /home/admin/wiki/raw/Indox/AIGroupChat/frontend/ai-group-chat-mvp/README.md
---

# AIGroupChat 运行时回复系统

该系统负责在静态剧本播放过程中处理用户插话，并以“托住 + 绕回”的方式回复，同时保持主剧情继续推进，不破坏必推讲解点顺序。

## 系统组成

### 1. 运行时直接回复
**接口**: `POST /api/ai-group-chat/runtime/reply`

**输入重点**:
- `sessionId`
- `scriptId`
- `chatStyle`
- `bots`
- `speakerSelection`
- `visibleContext`
- `userMessage`

**边界要求**:
- `visibleContext` 只能包含“已经推出”的 group/messages
- 不允许把未来尚未展示的内容传入模型

### 2. 托住并绕回
**接口**: `POST /api/ai-group-chat/runtime/hold-and-resume`

**用途**:
- 用户在群聊中发言时，系统先给出承接性的回应
- 然后把对话重新拉回主线讲解点推进
- 不改变 `dialogueIndex` 主流程顺序

### 3. 发言者选择
**模式**:
- `locked`：由指定机器人发言
- `model_select`：交给模型选择最合适的机器人

### 4. MVP 前端对应关系
静态前端示例中：
- 文本气泡对应 `dialogue-flow.json`
- 讲解点卡片对应 `tourPointCard`
- 用户输入只触发“托住 + 绕回”，不会打乱主流程
- 最终仍要求推出所有必推讲解点卡片

## 数据流

```text
静态剧本播放
  -> 用户发送文本
  -> 系统提取当前可见上下文
  -> 选择回复机器人 / 回复策略
  -> 生成托住性回应
  -> 恢复主流程继续播报
  -> 保证必推讲解点继续按序推出
```

## 核心约束

1. 用户输入不能跳过未来卡片
2. 用户输入不能重排必推讲解点顺序
3. 回复机器人只应基于当前已可见上下文作答
4. 运行时回复是补充层，不重写已发布的静态剧本结构

## 验证重点

- 用户插话后主流程仍可继续推进
- `visibleContext` 中不包含未来消息
- 指定机器人与模型选择两种模式都能工作
- 托住性回复不会破坏单活动讲解点边界

## 相关页面

- [[AIGroupChat群聊导览剧本系统]] — 项目总览
- [[AIGroupChat剧本生成系统]] — 静态剧本生成
