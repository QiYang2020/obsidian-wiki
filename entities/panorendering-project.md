---
title: PanoRendering UE5 项目
created: 2026-04-14
updated: 2026-04-14
type: entity
tags: [UE5, 全景相机, 画框系统, 展厅, Camera360]
sources:
  - /home/admin/wiki/raw/assets/UE5_PanoramiCamera/
---

# PanoRendering UE5 项目

PanoRendering 是基于 Unreal Engine 5.3 开发的全景相机渲染系统，主要用于虚拟展厅中的画框展示和全景相机路径管理。

## 项目概述

- **引擎版本**: UE5.3
- **主要功能**: 全景相机渲染、画框系统、展厅场景管理
- **核心插件**: Camera360v2、VaRest、MoviePipelineMaskRenderPass
- **开发语言**: C++ + 蓝图 + Python 脚本

## 项目结构

```
UE5_PanoramiCamera/
├── Content/
│   └── Tools/           # 主要工具系统
│       ├── CameraPoint/ # 相机点管理
│       ├── Frame_Blueprint/ # 画框蓝图V1
│       ├── Frame_BlueprintV2/ # 画框蓝图V2
│       ├── LEVEL/       # 展厅场景
│       ├── Model/       # 3D模型
│       ├── Sequence/    # 序列自动化
│       └── MS_material/ # 材质管理
├── Plugins/
│   └── Camera360v2/     # 360相机插件
└── Source/              # C++源码
```

## 核心系统

1. **[[camera-point-system]]**: 相机点管理系统，负责创建、导出、加载相机点数据
2. **[[frame-blueprint-system]]**: 画框蓝图系统，管理画框的材质、模型、动画
3. **[[level-management-system]]**: 展厅场景管理，包含G04展厅等场景
4. **[[sequence-automation-system]]**: 序列自动化系统，通过Python脚本从JSON配置生成相机序列

## 数据流

```
CameraPoint → JSON配置文件 → Python脚本 → LevelSequence
     ↓
Frame_Blueprint → 画框管理 → 材质/模型/动画
     ↓
LEVEL → 展厅场景 → 渲染输出
```

## 相关页面

- [[ue5-development]] — UE5 开发基础
- [[camera-point-system]] — 相机点管理系统
- [[frame-blueprint-system]] — 画框蓝图系统
- [[level-management-system]] — 展厅场景管理
- [[sequence-automation-system]] — 序列自动化系统