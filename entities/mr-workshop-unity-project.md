---
title: MR_Workshop Unity 项目
created: 2026-04-14
updated: 2026-04-14
type: entity
tags: [Unity, MR, 交互, Pico, 手势识别, 区域系统]
sources:
  - /home/admin/wiki/raw/assets/MR_Workshop/Assets/MRInteraction/Script/
---

# MR_Workshop Unity 项目

MR_Workshop 是基于 Unity 开发的混合现实（MR）交互项目，主要面向 Pico 设备，实现了手势识别、区域触发、积木搭建等交互功能。

## 项目概述

- **引擎版本**: Unity (URP 渲染管线)
- **目标平台**: Pico MR 设备
- **核心功能**: 手势抓取、区域触发、积木生成与计数、蓝图搭建
- **主要依赖**: Unity XR Interaction Toolkit、PXR SDK、TextMeshPro

## 项目结构

```
MR_Workshop/
├── Assets/
│   └── MRInteraction/
│       ├── Script/           # 核心代码
│       │   ├── XR/Pico/     # Pico 手势交互
│       │   ├── Zone/        # 区域触发系统
│       │   ├── Gameplay/    # 游戏逻辑
│       │   ├── Events/      # 事件系统
│       │   ├── Utils/       # 工具类
│       │   └── ScriptableObject/ # 数据资产
│       ├── Scene/           # 场景文件
│       └── ...              # 其他资源
├── Packages/                # 包管理
└── ProjectSettings/         # 项目配置
```

## 核心系统架构

### 1. **[[mr-workshop-hand-gesture-system]]**: 手势交互系统
- HandPoseGrabber: 手势抓取核心
- SeeThrough: MR 透视功能
- GestureDebugLogger: 手势调试

### 2. **[[mr-workshop-zone-trigger-system]]**: 区域触发系统
- ZoneTrigger: 区域触发器核心
- ZoneGameManager: 区域游戏管理器
- ZoneRuntimeLoader: 运行时区域加载
- ZoneVisualMPB: 区域可视化

### 3. **[[mr-workshop-gameplay-system]]**: 游戏逻辑系统
- GrabSpawn: 抓取生成系统
- CountBehavior: 计数行为
- TextCounterManager: 文本计数管理
- HighMission: 高处停留任务

### 4. **[[mr-workshop-event-system]]**: 事件通信系统
- EventHandle: 全局事件中心
- CloneNamePool: 克隆名称池

## 数据流架构

```
手势识别 → HandPoseGrabber → XRGrabInteractable
     ↓
区域触发 → ZoneTrigger → ZoneGameManager → 游戏结束判断
     ↓
积木生成 → GrabSpawn → CountBehavior → TextCounterManager
     ↓
事件通信 → EventHandle → 各系统响应
```

## 技术特点

1. **手势驱动交互**: 使用 Pico 手势识别驱动抓取，不依赖物理控制器
2. **区域计时触发**: 物体在区域内停留指定时间触发完成
3. **动态积木生成**: 抓取后自动生成替身，支持无限补货
4. **JSON 数据驱动**: 区域配置支持 JSON 文件运行时加载
5. **事件解耦**: 使用静态事件实现系统间通信

## 相关页面

- [[mr-workshop-hand-gesture-system]] — 手势交互系统详解
- [[mr-workshop-zone-trigger-system]] — 区域触发系统详解
- [[mr-workshop-gameplay-system]] — 游戏逻辑系统详解
- [[mr-workshop-event-system]] — 事件通信系统详解
- [[unity-development-core]] — Unity 开发核心
- [[xr-vr-ar-development]] — XR/VR/AR 开发