---
title: GZUCM_VRVideo Unity 项目
created: 2026-04-14
updated: 2026-04-14
type: entity
tags: [Unity, VR, 视频播放, Pico, 交互系统, 媒体展示]
sources:
  - /home/admin/wiki/raw/assets/GZUCM_VRVideo/Assets/Scripts/
---

# GZUCM_VRVideo Unity 项目

GZUCM_VRVideo 是基于 Unity 开发的 VR 视频播放项目，主要面向 Pico 设备，实现了媒体展示、传送系统、交互式菜单等功能。

## 项目概述

- **引擎版本**: Unity (URP 渲染管线)
- **目标平台**: Pico VR 设备
- **核心功能**: VR 视频/图片展示、传送系统、交互式菜单、媒体播放控制
- **主要依赖**: Unity XR Interaction Toolkit、PICO Platform SDK、DOTween

## 项目结构

```
GZUCM_VRVideo/
├── Assets/
│   ├── Scripts/           # 核心脚本
│   │   ├── InteractableData.cs      # 交互数据组件
│   │   ├── InteractableDataContainer.cs # 数据容器
│   │   ├── DataManager.cs           # 数据管理器
│   │   ├── DataModel.cs             # 数据模型
│   │   ├── CanvasController.cs      # Canvas 控制器（媒体显示）
│   │   ├── TeleportManager.cs       # 传送管理器
│   │   ├── GrabAttachReturn.cs      # 抓取返回系统
│   │   ├── ButtonInteraction.cs     # 按钮交互系统
│   │   ├── MenuUI.cs                # 菜单 UI 系统
│   │   ├── BackgroundMusicController.cs # 背景音乐控制
│   │   └── Bei.cs                   # 备用脚本
│   ├── Plugins/           # 插件（DOTween）
│   └── ...                # 其他资源
├── Packages/              # 包管理
└── ProjectSettings/       # 项目配置
```

## 核心系统架构

### 1. **[[GZUCM_VRVideo媒体展示系统]]**: 媒体展示系统
- InteractableData: 交互数据组件
- DataManager: 数据管理器
- CanvasController: 媒体显示控制器
- 支持图片和视频两种媒体类型

### 2. **[[GZUCM_VRVideo传送系统]]**: 传送系统
- TeleportManager: 传送管理器
- 支持基于标签的传送
- 集成确认对话框

### 3. **[[GZUCM_VRVideo交互系统]]**: 交互系统
- GrabAttachReturn: 抓取返回系统
- ButtonInteraction: 按钮交互系统
- 基于 XR Interaction Toolkit

### 4. **[[GZUCM_VRVideo UI系统]]**: UI 系统
- MenuUI: 菜单 UI 系统
- BackgroundMusicController: 背景音乐控制
- 支持多级菜单和提示框

## 数据流架构

```
JSON 数据 → DataManager → InteractableDataContainer
     ↓
交互触发 → InteractableData → CanvasController
     ↓
媒体显示 → 图片/视频播放 → 背景音乐控制
     ↓
传送系统 → TeleportManager → 位置移动
```

## 技术特点

1. **数据驱动媒体**: 通过 JSON 配置媒体内容和类型
2. **跨平台支持**: 支持 Android (Pico) 和编辑器模式
3. **异步资源加载**: 使用协程异步加载图片和视频
4. **DOTween 动画**: 平滑的 UI 和物体动画
5. **XR 交互集成**: 完整的 XR Interaction Toolkit 集成

## 相关页面

- [[GZUCM_VRVideo媒体展示系统]] — 媒体展示系统详解
- [[GZUCM_VRVideo传送系统]] — 传送系统详解
- [[GZUCM_VRVideo交互系统]] — 交互系统详解
- [[GZUCM_VRVideo UI系统]] — UI 系统详解
- [[MR_Workshop Unity项目]] — MR Workshop 项目对比
- [[Unity开发核心]] — Unity 开发核心
- [[XR、VR、AR开发]] — XR/VR/AR 开发