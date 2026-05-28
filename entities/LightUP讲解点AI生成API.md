---
title: LightUP_AItourPoint_API
created: 2026-05-28
updated: 2026-05-28
type: entity
tags: [FastAPI, TTS, LRC, StepFun, 导览, Responses API]
sources:
  - /home/admin/wiki/raw/Indox/LightUP_AItourPoint_API/LightUP_AItourPoint_API_技术文档.md
  - /home/admin/wiki/raw/Indox/LightUP_AItourPoint_API/Scripts/
---

# LightUP_AItourPoint_API

LightUP_AItourPoint_API 是一个面向讲解点语音生成的后端服务，围绕 `speechText -> instruction -> ttsText -> audioBase64 + lrcTaskId -> lrcText` 这条链路组织接口与服务。

## 项目概述

- **后端框架**: FastAPI
- **接口前缀**: `/admin/theme-activity/tour-point/ai`
- **核心外部能力**: Responses API 文本生成、StepFun TTS、Whisper/LRC 对齐
- **输出目标**: 讲解文稿、朗读要求、TTS 文稿、音频 base64、异步 LRC 对齐结果

## 项目结构

```text
LightUP_AItourPoint_API/
├── Scripts/
│   ├── app.py                         # FastAPI 启动入口
│   ├── config.py                      # LLM / StepFun / LRC / Admin 配置
│   ├── routes/ai.py                   # 主业务路由
│   └── services/
│       ├── llm_responses_service.py   # Responses API 文本生成
│       ├── stepfun_service.py         # StepAudio TTS 封装
│       ├── lrc_align_service.py       # 音频文本对齐
│       └── lrc_task_service.py        # 进程内异步任务表 + 线程池
└── LightUP_AItourPoint_API_技术文档.md
```

## 核心系统架构

### 1. [[LightUP讲解点AI生成链路]]
- 讲解文稿生成
- 朗读要求生成
- TTS 文稿生成
- LLM 结构化输出与回退约束

### 2. [[LightUP音频生成与LRC对齐系统]]
- StepFun 音频生成
- 音色白名单与参数校验
- 音频 base64 返回
- LRC 异步任务提交与查询

## 技术特点

1. **完整链路拆段**：把文稿、朗读要求、TTS 文稿、音频、LRC 对齐拆成多个独立接口
2. **固定音色白名单**：当前只允许预设音色 ID，避免前端任意透传
3. **TTS 文稿强约束**：只能在原文句间插入中文括号控制词，不允许改写正文
4. **音频与 LRC 解耦**：`/audio/speech` 同步返回音频，LRC 通过异步任务查询
5. **配置集中化**：LLM、StepFun、Whisper/LRC、管理后台配置统一在 `config.py`

## 关键接口

- `GET /defaults`
- `GET /voices`
- `POST /speech-text/generate`
- `POST /tts-instruction/generate`
- `POST /tts-text/generate`
- `POST /audio/speech`
- `GET /lrc/tasks/{task_id}`

## 相关页面

- [[LightUP讲解点AI生成链路]] — 文稿、instruction、ttsText 的生成链路
- [[LightUP音频生成与LRC对齐系统]] — StepFun 音频输出与 LRC 异步对齐
- [[技术文档结构化写作]] — 技术文档结构化写作
