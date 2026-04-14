---
title: UE5 Development
created: 2026-04-11
updated: 2026-04-14
type: concept
tags: [UE5, Unreal Engine, Blueprint, Editor Tools, Media Player, Datasmith]
sources:
  - /home/admin/wiki/_staging/activate-ue5-naming-validator-05a3d5c3-206a-4521-24a5f87df007.md
  - /home/admin/wiki/_staging/ue5-3d2179c3-c330-4159-bae8-757a370a9540-2024041-dfac1d2f7d21.md
  - /home/admin/wiki/_staging/ue5-67ceac4a-2838-800d-8982-a26c31e31484-2025031-a0763fca9dc2.md
  - /home/admin/wiki/_staging/ue5-67ceac4a-2838-800d-8982-a26c31e31484-2025031-545ecc1b37ea.md
  - /home/admin/wiki/_staging/cbfa58e3-f90c-4437-99c4-8e17062abb45-20240511-09-53618751d948.md
  - /home/admin/wiki/_staging/cbfa58e3-f90c-4437-99c4-8e17062abb45-20240511-09-e81091dda0c1.md
  - /home/admin/wiki/_staging/electra-67a6be34-8f78-800d-a4d9-d17ce0e70dc3-202-01bb0a3f6a74.md
  - /home/admin/wiki/raw/assets/UE5_PanoramiCamera/
---

# UE5 Development

Unreal Engine 5（UE5）开发涉及蓝图交互、编辑器扩展、资源导入、媒体播放等多个方向。本页汇总相关实践经验。

## 蓝图交互制作

在UE5中使用蓝图制作交互时，核心流程包括：

- 使用 FrameController 和 ParameterController 管理场景参数
- 基于 Plane 组件尺寸动态调整 lining_W / lining_H，联动后续 Set 节点
- 通过蓝图函数拆分逻辑，保持上下文连贯性

## 命名约定检查器（Naming Validator）

激活UE5命名约定检查器（Naming Validator）用于确保资产命名符合项目规范。可在 Editor Preferences 中启用。

在蓝图间跨引用变量（如 Mat Group Name、Mat Name）时，需确保变量设置为 **公开（Public）**，通过蓝图引用获取实例后赋值。

## 自定义编辑器工具

UE5 提供两种主要的编辑器扩展方式：

**EUC（Editor Utility Component）**
- 创建自定义编辑器工具组件，将方法暴露到细节面板（Details Panel）
- 在编辑器模式下通过点击调用，适用于自动化流程、批量操作

**EUA（Editor Utility Actor）**
- 可放置在场景中的编辑器工具 Actor
- 作为编辑时单例工具使用，支持交互式操作

注意：UE5 没有官方预制体（Prefab）概念。可通过蓝图或自定义 C++ Actor 组件的方式，将静态网格体、灯光、碰撞体等组合为可复用对象。

## 导入外部内容文件

将外部导出的 Content 文件夹导入 UE5 空白项目：

1. 直接将文件夹复制到项目 Content 目录下
2. 重新打开项目，UE5 会自动扫描并导入资源

使用 **Datasmith** 导入资源时，烘焙流程中的关键点：

- 确保模型在 3D 建模软件（3ds Max / Blender / SketchUp）中具备至少两套 UV 映射
- 第一套 UV 用于材质贴图，第二套专门优化用于光照烘焙（Lightmap）
- 导入后在 Static Mesh Editor 中确认 UV 通道设置

## Electra 媒体播放器循环播放

UE5 的 Electra Media Player 实现视频循环播放：

- 调用 MediaPlayer 的 SetLooping 方法并勾选 Looping 参数
- Electra 内部通过 Seek 实现循环，因此 **不会触发 On End Reached 事件**
- 不同主机上表现可能不一致

**检测循环开始的方案：**
1. 使用 Event Tick 每帧获取播放时间（Get Time）
2. 检测时间回退（当前时间 < 上一帧时间）判断循环发生
3. 循环发生时打印日志或执行回调

## 相关页面

- [[panorendering-project]] — PanoRendering 全景相机渲染系统项目
- [[camera-point-system]] — 相机点管理系统
- [[frame-blueprint-system]] — 画框蓝图系统
- [[level-management-system]] — 展厅场景管理
- [[sequence-automation-system]] — 序列自动化系统
- [[unity-development-core]] — Unity 开发基础
- [[webgl-development]] — WebGL 跨平台发布
- [[xr-vr-ar-development]] — XR/VR/AR 开发
