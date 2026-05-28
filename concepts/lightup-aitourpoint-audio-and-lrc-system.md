---
title: LightUP 音频生成与 LRC 对齐系统
created: 2026-05-28
updated: 2026-05-28
type: concept
tags: [FastAPI, StepFun, TTS, LRC, Whisper, 异步任务]
sources:
  - /home/admin/wiki/raw/Indox/LightUP_AItourPoint_API/LightUP_AItourPoint_API_技术文档.md
  - /home/admin/wiki/raw/Indox/LightUP_AItourPoint_API/Scripts/routes/ai.py
  - /home/admin/wiki/raw/Indox/LightUP_AItourPoint_API/Scripts/services/stepfun_service.py
  - /home/admin/wiki/raw/Indox/LightUP_AItourPoint_API/Scripts/services/lrc_task_service.py
---

# LightUP 音频生成与 LRC 对齐系统

该系统负责把 `ttsText` 提交给 StepFun 生成音频，并在音频成功后异步启动 LRC 对齐任务，最终通过任务查询接口返回字幕结果。

## 系统组成

### 1. 默认配置与音色列表
**接口**:
- `GET /defaults`
- `GET /voices`

**默认值来源**:
- `StepFunConfig`
- `LrcConfig`

**当前音色白名单**:
- `voice-tone-ROJ0LxtB8C` — 默认女声
- `voice-tone-ROAmq5MujQ` — 中医药馆长

### 2. 音频生成入口
**接口**: `POST /audio/speech`

**核心校验**:
- 必须提供 `ttsText`
- 必须提供 `speechText`
- 必须提供 `instruction`
- `model` 必须固定为配置中的 StepFun 模型
- `voice` 不能为空且必须在允许列表中

### 3. StepFun 服务封装
**核心服务**: `StepFunService`

**职责**:
- 组装 `/audio/speech` 请求 payload
- 规范化 `pronunciation_map`
- 控制 `speed`、`volume`、`response_format`、`sample_rate`
- 处理直接返回音频 bytes 或返回 URL 两种场景

### 4. LRC 异步任务
**核心服务**: `lrc_task_service.py`

**实现机制**:
- 进程内 `_lrc_tasks` 内存任务表
- `ThreadPoolExecutor(max_workers=1)` 后台串行执行
- 任务状态：`PENDING` / `RUNNING` / `COMPLETED` / `FAILED`
- 查询函数：`get_lrc_task(task_id)`

## 数据流

```text
ttsText + instruction + voice
  -> StepFunService.generate_audio()
  -> 返回 audio bytes
  -> base64 编码为 audioBase64
  -> submit_lrc_task()
  -> 后台线程调用 LrcAlignService.align()
  -> 通过 /lrc/tasks/{task_id} 查询状态与 lrcText
```

## 输出结构

音频生成成功后，同步返回：
- `audioBase64`
- `audioBase64Encoding`
- `lrcTaskId`
- `lrcStatus=PENDING`
- `contentType`
- `fileName`
- `responseFormat`
- `stepAudioModel`
- `stepAudioVoice`

LRC 完成后任务表中可读到：
- `lrcText`
- `segments`
- `alignText`
- `segmentCount`
- `completedAt`

## 限制与适用场景

- 当前 LRC 任务表是进程内内存结构，适合本地服务/单实例部署
- 若进程重启，内存任务状态会丢失
- 线程池 `max_workers=1` 更偏向稳定串行处理，而非高并发批量任务

## 相关页面

- [[lightup-aitourpoint-api]] — 项目总览
- [[lightup-aitourpoint-generation-pipeline]] — 文稿/instruction/ttsText 生成链路
