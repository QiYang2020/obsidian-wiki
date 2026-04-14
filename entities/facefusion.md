# FaceFusion

> Industry leading face manipulation platform — 开源人脸替换与增强平台，支持图片和视频处理。

## 概述

FaceFusion 是一个功能丰富的人脸操作平台，提供人脸替换（face swapping）、人脸增强（face enhancement）、表情编辑、年龄修改、唇形同步等多种处理能力。支持 Web UI 交互模式、命令行 headless 模式和批量作业模式。

项目以 ONNX Runtime 为核心推理引擎，支持多种硬件加速后端（CUDA、TensorRT、DirectML、CoreML、OpenVINO 等），可在 Windows、macOS、Linux 上运行。

## 架构

### 核心分层
```
facefusion.py (入口)
  → core.py (CLI 路由)
    → run → uis/core.py (Gradio Web UI)
    → headless-run → process_headless()
    → batch-run → process_batch()
    → job-* → job_manager / job_runner (作业系统)
```

### 关键模块
- **execution.py** — ONNX Runtime 执行 provider 解析与组装（CUDA/TensorRT/DirectML/CoreML/OpenVINO/QNN/CPU）
- **inference_manager.py** — 推理 session 创建、复用和清理
- **state_manager.py** — CLI/UI 运行时状态维护
- **config.py / facefusion.ini** — 启动预设配置
- **processors/** — 模块化处理器（face_swapper、face_enhancer、age_modifier、lip_syncer 等）
- **workflows/** — image_to_image、image_to_video 处理流程

### 推理链路
输入 source（参考人脸）+ target（目标图片/视频）→ 人脸检测（RetinaFace）→ 人脸特征点（2DFAN4）→ 人脸分割（XSeg）→ 处理器执行（swap/enhance 等）→ 输出合成结果

## 技术栈

| 层面 | 技术 |
|------|------|
| 推理引擎 | ONNX Runtime（多 provider） |
| 加速方案 | CUDA、TensorRT（NVIDIA）、DirectML（Windows）、CoreML（macOS）、OpenVINO（Intel） |
| Web UI | Gradio |
| 视频处理 | FFmpeg |
| 音频处理 | kim_vocal_2（语音提取） |
| 人脸检测 | RetinaFace |
| 人脸特征点 | 2DFAN4 |
| 人脸分割 | XSeg 3 |
| 配置管理 | INI 文件 + CLI 参数 |
| 运行环境 | Python 3.10+、Miniconda（Windows 原生推荐） |

## 使用方式

### 启动模式
- `python facefusion.py run` — Web UI 交互模式（默认 7860 端口）
- `python facefusion.py headless-run` — 命令行无界面模式
- `python facefusion.py batch-run` — 批量处理模式
- `python facefusion.py job-*` — 完整的作业管理系统（创建/提交/运行/重试）

### 核心处理器
- **face_swapper** — 人脸替换（HyperSwap 等模型）
- **face_enhancer** — 人脸增强/修复（GPEN BFR 等模型）
- **age_modifier** — 年龄修改
- **expression_restorer** — 表情恢复
- **face_editor** — 面部编辑（眼神、嘴型、头部姿态）
- **lip_syncer** — 唇形同步
- **frame_enhancer** — 帧增强
- **frame_colorizer** — 帧着色
- **background_remover** — 背景移除

### 配置预设
通过 `facefusion.ini` 固化启动参数，包括：
- 输出路径、检测模型、处理模型选择
- 执行 provider（CUDA/TensorRT）
- 内存策略、线程数
- 视频编码器（h264_nvenc）和质量预设

## 部署要点

- 推荐 Windows 原生部署（非 WSL），使用 Miniconda 本地环境
- 局域网访问通过 Windows `portproxy` 实现（18065 → 7860）
- 模型存放在 `.assets/models`，支持手动预置避免重复下载
- `facefusion.ini` 是启动预设，UI 中修改的参数不会自动回写
- 支持 TensorRT 引擎缓存，首次推理较慢后续加速明显

## 许可证

OpenRAIL-AS（开放负责任 AI 许可）

## 关联

- 在 [[ai-image-generation]] 中被分析为 AI 换脸/数字人方案的核心工具之一
- 与 [[ar-museum-solutions]] 的数字人应用场景相关
- 依赖 [[cuda-toolkit-安装与路径管理]] 中的 CUDA 环境配置
