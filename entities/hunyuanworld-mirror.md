# HunyuanWorld-Mirror

> 腾讯混元团队开发的多功能前馈 3D 世界重建模型，单次前向传播即可同时生成多种 3D 表示。

## 概述

HunyuanWorld-Mirror（论文名 WorldMirror）是一个统一的前馈神经网络，用于全面的 3D 几何预测。它整合多种几何先验（相机位姿、校准内参、深度图），在单次推理中同时输出：

- **点云**（3D 点图 + 置信度）
- **多视图深度图**
- **相机参数**（位姿 + 内参）
- **表面法线**
- **3D 高斯溅射**（3DGS）

在点云重建、新视角合成、深度估计、相机位姿估计、表面法线预测等任务上均达到 SOTA 水平。

## 架构

由两个核心组件构成：

1. **多模态先验提示（Any-Prior Prompting）**：将校准内参、相机位姿、深度等先验通过轻量编码层转化为结构化 token，支持任意先验子集输入。
2. **通用几何预测头**：统一架构处理从相机估计到点图回归、法线估计和新视角合成的全套 3D 重建任务。

训练分两阶段：Stage 1 训练先验、点图、相机、深度和法线；Stage 2 专门训练 3D 高斯溅射头。

## 技术栈

| 层面 | 技术 |
|------|------|
| 深度学习框架 | [[pytorch]] 2.4 (CUDA 12.4) |
| 训练框架 | PyTorch Lightning 2.5+、Hydra 配置 |
| 3DGS 渲染 | gsplat |
| Web 演示 | Gradio |
| 视频处理 | OpenCV、MoviePy、FFmpeg |
| 模型格式 | SafeTensors（Hugging Face 分发） |
| 点云处理 | Open3D、trimesh、pycolmap |
| 运行环境 | Python 3.10、Conda（推荐 WSL2 Ubuntu） |

## 使用方式

### 推理入口
- `infer.py` — 核心推理：输入图像/视频目录，输出点云、深度、法线、相机参数、3DGS
- `hunyuan_pipeline.py` — 批处理管道：串联推理 + 3DGS 优化一键执行
- `app.py` / `web_ui_lan/app.py` — Gradio 交互式演示，支持局域网访问

### 典型流程
1. 准备输入图像（jpg/png/webp）或视频
2. 运行推理生成初始 3D 点云和高斯初始化
3.（可选）通过 gsplat 进行 3DGS 后期优化
4. 导出 COLMAP 格式或 PLY 点云供 [[3d-photogrammetry]] 工具链使用

### 模型获取
模型权重托管于 Hugging Face（`tencent/HunyuanWorld-Mirror`），支持离线本地加载。

## 部署要点

- 推荐 Windows + WSL2 环境，Conda 环境名 `hyw`
- 模型可离线放置于 `ckpts/` 目录避免网络依赖
- 局域网访问需配置 Windows `portproxy` 端口转发（7860）
- 3DGS 优化较慢，建议仅在需要高质量渲染时启用

## 性能亮点

在 7-Scenes、NRGBD、DTU 等数据集上，配合全部先验（相机+深度+内参）时：
- 点云重建 Acc 0.018 / Comp 0.023（远优于 VGGT、π³ 等方法）
- 新视角合成 PSNR 22.30（Re10K），超越 FLARE、AnySplat

## 相关链接

- 论文：WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting (arXiv:2510.10726)
- 模型：https://huggingface.co/tencent/HunyuanWorld-Mirror
- 在线 Demo：https://huggingface.co/spaces/tencent/HunyuanWorld-Mirror

## 关联

- 与 [[3d-photogrammetry]] 共享 PLY 点云格式和 gsplat 渲染管线
- 与 [[ai-image-generation]] 同属腾讯混元 AI 生态
- 与 [[pytorch]] 深度绑定，依赖 CUDA 加速推理
