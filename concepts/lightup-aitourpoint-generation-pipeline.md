---
title: LightUP 讲解点 AI 生成链路
created: 2026-05-28
updated: 2026-05-28
type: concept
tags: [FastAPI, 导览文稿, TTS, Responses API, 结构化输出]
sources:
  - /home/admin/wiki/raw/Indox/LightUP_AItourPoint_API/LightUP_AItourPoint_API_技术文档.md
  - /home/admin/wiki/raw/Indox/LightUP_AItourPoint_API/Scripts/routes/ai.py
  - /home/admin/wiki/raw/Indox/LightUP_AItourPoint_API/Scripts/services/llm_responses_service.py
---

# LightUP 讲解点 AI 生成链路

该系统负责把讲解点上下文逐步加工为可用于语音合成的内容，链路为：`speechText -> instruction -> ttsText`。

## 系统组成

### 1. 讲解文稿生成
**接口**: `POST /speech-text/generate`

**输入重点**:
- `activityId`
- `tourPointId`
- `tourPointSnapshot.artworkDescription`
- `tourPointSnapshot.artworkImageUrl`
- `controls.useVision`
- `controls.instructionLines`

**校验规则**:
- 缺少 `artworkDescription` -> HTTP 400
- `useVision=true` 但没有 `artworkImageUrl` -> HTTP 400
- `instructionLines` 为空 -> HTTP 400
- `useDeepSearch` 当前不支持 -> HTTP 400

### 2. 朗读要求生成
**接口**: `POST /tts-instruction/generate`

**用途**:
- 根据展品名称、作者、讲解文稿、图片等上下文
- 输出结构化 `instruction`
- 为 StepAudio 合成准备语气、节奏、导览场景提示

### 3. TTS 文稿生成
**接口**: `POST /tts-text/generate`

**用途**:
- 在不改写原始讲解文稿的前提下
- 仅在句间插入中文括号控制词
- 生成最终提交给 StepAudio 的 `ttsText`

## Responses API 适配层

**核心服务**: `ResponsesLLMService`

能力包括：
- 构造 Responses API payload
- 支持图文联合输入
- 提取 `output_text` 或 `output[].content[].text`
- 解析结构化 JSON 输出
- 校验 `ttsText` 不能改写 `speechText`

## 关键约束

### 1. TTS 文稿不能改写正文
服务内部会：
- 去掉 `ttsText` 中的中文括号控制词
- 把剩余文本与 `speechText` 做归一化比较
- 若正文被改写则直接报错

### 2. 控制词只能放在句间
校验要求：
- 不能放句首
- 不能放句尾
- 不能插入句子内部
- 前一个字符必须是句末标点

### 3. 模型输出结构化
- `instruction` 生成要求返回合法 JSON 对象
- `ttsText` 生成要求返回合法 JSON 对象
- 若缺关键字段会抛出 `LLMResponseError`

## 数据流

```text
讲解点快照 + 控制参数
  -> Responses API 生成 speechText
  -> Responses API 生成 instruction
  -> Responses API 生成 ttsText
  -> 校验 ttsText 仅添加句间控制词
  -> 进入音频合成阶段
```

## 相关页面

- [[lightup-aitourpoint-api]] — 项目总览
- [[lightup-aitourpoint-audio-and-lrc-system]] — 音频合成与 LRC 对齐
