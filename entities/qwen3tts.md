---
title: Qwen3TTS
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [tts, qwen, voice-clone, whisper, gradio, wsl, windows, lrc]
sources:
  - raw/inbox/Qwen3TTS/README.md
  - raw/inbox/Qwen3TTS/ENGINEERING.md
  - raw/inbox/Qwen3TTS/scripts/voice_design_web.py
  - raw/inbox/Qwen3TTS/whisper_align_tool/whisper_align.py
  - raw/inbox/Qwen3TTS/scripts/validate_voice_design.py
  - raw/inbox/Qwen3TTS/scripts/validate_base_clone.py
---

# Qwen3TTS

本地部署的 Qwen3-TTS 语音合成 + Whisper 对齐工具链，面向博物馆讲解等场景的语音克隆与 LRC 歌词生成系统。

## 概览

Qwen3TTS 是一个基于 [[pytorch]] 和 CUDA 的本地 TTS 工程项目，整合了阿里通义千问的 Qwen3-TTS 系列模型与 OpenAI Whisper 强制对齐工具，通过 Gradio WebUI 提供语音设计、语音克隆、批量生成和 LRC 歌词同步等能力。

核心用途：

- 博物馆展品讲解语音生成（中文女讲解员风格）
- 基于参考音频的 voice clone
- Whisper 强制对齐生成 LRC 时间轴歌词
- Excel 批量导入与汇总输出

## 技术栈

| 组件 | 技术 |
|------|------|
| 宿主系统 | Windows + WSL2 / Ubuntu-22.04 |
| Python | 3.12 |
| 推理框架 | PyTorch + CUDA (bfloat16) |
| TTS 模型 | Qwen3-TTS-12Hz-1.7B-VoiceDesign / Base |
| 对齐工具 | stable-ts (stable_whisper), openai-whisper |
| Web 服务 | Gradio |
| 数据处理 | pandas, openpyxl, soundfile, ffmpeg |

注意实现：

- 优先使用 flash_attention_2，不可用时自动回退到 sdpa
- 推理强制要求 CUDA 可用
- LRC 对齐优先使用 forced alignment（非自由转录）

## 架构

项目采用 "Windows 入口 + WSL 运行时" 的双层架构：

- **Windows 侧**：VS Code 工作区、PowerShell 启动脚本、input/outputs 目录、局域网端口转发
- **WSL 侧**：Python 环境、CUDA 推理、模型加载、Gradio 服务

代码编辑在 Windows 工作区完成，服务启动时自动同步到 WSL 运行目录。输出目录 `H:\Ai\Qwen3TTS\outputs` 是唯一真源，WSL 通过 `/mnt/h/` 挂载写入同一位置。

## 核心组件

### `scripts/voice_design_web.py`

主应用入口，Gradio WebUI，包含 5 个功能标签页：

- **VoiceDesign**：文本 + instruction → wav（指令式语音设计）
- **Base Clone**：文本 + 参考音频 + 参考文本 → wav（语音克隆）
- **Base Clone + LRC**：同上，额外生成 LRC 时间轴
- **Batch Base Clone**：Excel A 列批量生成 wav
- **Input 总表 + 音频**：从 `input/` 中的业务表格批量生成 wav + LRC 写回汇总表

### `whisper_align_tool/whisper_align.py`

Whisper 强制对齐后端，负责：

- 加载并缓存 stable_whisper 对齐模型
- 执行 forced alignment（已知文本 + 音频 → LRC）
- LRC 分段策略：标点优先分割 → 贪心合并 → 硬切分
- 时间戳按字符数比例分配
- 支持 10 种语言（zh/en/ja/ko/de/fr/ru/pt/es/it + auto）

### 验证脚本

- `scripts/validate_voice_design.py`：验证 VoiceDesign 模型路径、CUDA、输出写入
- `scripts/validate_base_clone.py`：验证 Base Clone 模型 + 参考音频

## 模型

三个模型文件缓存于 `/root/projects/Qwen3TTS/.cache/models/`：

- `Qwen3-TTS-12Hz-1.7B-VoiceDesign` — 指令式语音设计
- `Qwen3-TTS-12Hz-1.7B-Base` — 语音克隆基座
- `Qwen3-TTS-Tokenizer-12Hz` — 12Hz 音频 tokenizer

## 启动方式

Windows PowerShell 管理员执行：

```
powershell -ExecutionPolicy Bypass -File H:\Ai\Qwen3TTS\scripts\start_voice_design_web.ps1
```

启动脚本自动完成：WSL 代码同步、IP 刷新、端口转发 (7860)、防火墙规则、WSL Gradio 服务启动。

默认访问地址：`http://127.0.0.1:7860`

## 开发约定

- 新增输出默认写入 `H:\Ai\Qwen3TTS\outputs`
- WebUI 下载文件必须在 `allowed_paths` 范围内
- 修改 LRC 行为时需同时验证单条页和批量汇总页
- 修改代码后需重新运行 PowerShell 启动脚本以同步到 WSL

## 相关链接

- [[cuda-toolkit-安装与路径管理]] — CUDA 环境配置
- [[pytorch]] — 推理框架基础
