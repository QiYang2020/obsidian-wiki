---
title: AI Image Generation
created: 2026-04-11
updated: 2026-04-11
type: concept
tags: [AI, Image Generation, ComfyUI, Flux, Stable Diffusion, FaceFusion, Digital Human, Prompt Engineering]
sources:
  - /home/admin/wiki/_staging/69240222-a3d4-8323-828d-fddedaac8bb3-20251124-14-925875e076d8.md
  - /home/admin/wiki/_staging/ai-67ce5dd1-4f04-800d-8055-8bea6c735178-20250310-1fe4b8237e5f.md
  - /home/admin/wiki/_staging/comfyui-unet-vae-clip-694a0fa4-ea8c-8324-8362-81-0b866d54d8a2.md
  - /home/admin/wiki/_staging/facefusion-69b910d9-6e6c-83a4-bb63-2e54804920bb--eb61e08b11b5.md
  - /home/admin/wiki/_staging/flux-depth-scene-prompt-69bd1807-e1a4-83aa-8d83--557b8d006915.md
  - /home/admin/wiki/_staging/697732f0-dd54-8324-a3a8-34f4e5148188-20260126-17-8636d1300212.md
  - /home/admin/wiki/_staging/688722df-0b3c-8333-afa2-b3c13fe6bdda-20250728-15-56a9fe2d5296.md
---

# AI Image Generation

AI 图像生成技术涵盖文本到图像、风格迁移、人脸替换、数字人等多个方向。本页整理相关工具链与实践经验。

## ComfyUI 工作流核心组件

以 Flux 模型为例的 ComfyUI 核心节点：

**UNET Loader** — 加载去噪网络模型
- 决定生成图像的基础能力和风格

**Dual CLIP Loader** — 双 CLIP 文本编码器加载
- Flux 使用双 CLIP 架构（CLIP-L + T5-XXL）
- 需确保 CLIP 类型与模型匹配

**VAE Loader** — 变分自编码器加载
- 负责图像的编码/解码
- 不匹配会导致输出图像颜色异常

**常见报错：**
- `mat1 and mat2 shapes cannot be multiplied (131072x64 and 128x3072)`
- 本质是矩阵维度不匹配，99% 出现在 CLIP / Text Encoder 阶段
- 原因：模型和 CLIP 不匹配，需检查 Load CLIP 节点的文件和类型选择

## Flux Depth 工作流

Flux Depth 用于基于深度图的场景生成：

- 使用专业术语描绘场景风格的英文提示词
- 要求色彩艳丽、真实风格时，重点描述：
  - 光照条件（dramatic lighting, golden hour）
  - 材质质感（subsurface scattering, volumetric fog）
  - 色彩理论（complementary colors, saturated palette）
  - 摄影参数（shallow DOF, anamorphic lens）

## 风格提案生成

使用 AI 生成积木玩具风格方案：

- 基于相同基础形状（长方体、正方体、拱形、圆柱）
- 探索极端视觉风格变体：
  - 纸艺 / 折叠纸板风格
  - 玻璃 + 液体填充风格
  - 粘土 / 橡皮泥手工风格
  - 霓虹轮廓 / Synthwave 风格

## FaceFusion 竞品分析

**FaceFusion 本质定位：工程化最强的开源换脸工具**

- 核心不是模型创新，而是 pipeline 整合（检测 → 对齐 → swap → enhancer → render）
- 工程化调度（batch / queue / headless）
- 类比：Stable Diffusion 里的 AUTOMATIC1111 + ControlNet

**竞品图谱（近两年）：**
- 侧重视频换脸/流式处理的业务落地视角
- 优先关注发布时间更新的竞品

## 数字人 AI 技术方案

博物馆场景下的 AI 数字人应用：

**背景：** 传统博物馆导览痛点
**建设目标：** AI 数字人解决方案

- 数字人优点：形象一致、24/7 可用、多语言支持、个性化互动
- AI 优点：智能问答、内容更新灵活、数据收集分析
- 应用场景：线下面对游客的数字助手（中医药博物馆）

## 戏台背景图需求

"戏面幻影墙"互动装置的 AI 生图 prompt：

```
A stunning and vibrant traditional Chinese opera stage background 
in 4K horizontal format. Grand red and gold opera stage with 
intricate traditional Chinese patterns, glowing lanterns, dramatic 
red curtains, mystical atmosphere. No characters or text.
```
- 尺寸：1792x1024
- 要求：无文字、无人物，仅舞台与文化元素

## 简单生图方案

快速出图的技术选型与流程简化方案，适合非技术人员快速上手。

## 相关页面

- [[3d-photogrammetry]] — 3D 重建与高斯溅射
- [[indoor-navigation-positioning]] — 室内导览中的数字人应用
