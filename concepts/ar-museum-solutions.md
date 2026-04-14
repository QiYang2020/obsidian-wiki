---
title: AR 博物馆与手势交互方案
created: 2026-04-11
updated: 2026-04-11
type: concept
tags: [ar, museum, hand-gesture, comfyui]
sources:
  - _staging/ar-67ea3adb-30f8-800d-a476-27083989ed9f-20250331-8987496eb4ca.md
  - _staging/ar-6981b41b-e01c-83a5-8e66-8ff03d887527-20260203-ee860168c87c.md
  - _staging/static-hand-gesture-696352e0-8ce8-8321-8d30-3236-0699385fe089.md
---

# AR 博物馆与手势交互方案

AR 在博物馆场景的落地方案，以及手势识别在 XR 交互中的应用。

## AR 博物馆方案商

市场上提供 AR 博物馆整体解决方案的公司：

1. **云观博**：
   - 基于 AR 的智慧导览系统
   - 已在近 500 家博物馆应用，包括近 50 家国家一级博物馆

2. **弥知科技（Kivicube）**：
   - AR 制作平台，支持开发者制作 AR 互动场景
   - 应用于虚拟展示和互动体验

3. **灵伴科技（Rokid）**：
   - AR 眼镜硬件+软件整体方案
   - 支持 XREAL、Rokid 等 AR 眼镜设备

4. **其他方案商**：亮风台、影创科技、nreal 等

## 手势识别（Static Hand Gesture）

Unity XR Hands 包提供手势识别功能，用于检测静态手势。

**应用场景**：
- MR 积木游戏中检测握拳、张开等手势
- 虚拟物体抓取控制
- 手势触发特定交互

**典型问题 — 黏手 Bug**：
- 手势结束后物体仍被抓取
- 原因：XRIT 选择状态机与手势事件时序冲突
- 解决：确保 `gesture_ended` 时调用 `XRInteractionManager.CancelInteractorSelection`

**手势识别流程**：
1. 配置 `StaticHandGesture` 组件
2. 定义手势形状（手指弯曲角度）
3. 订阅 `gesturePerformed` 和 `gestureEnded` 事件
4. 在事件中控制 `XRGrabInteractable` 的选择状态

## 相关页面

- [[xr-vr-ar-development]] — XR 核心开发框架（OpenXR、SteamVR、XRIT）
- [[indoor-navigation-positioning]] — 室内定位技术，可用于 AR 导航
- [[ai-image-generation]] — ComfyUI 工作流详细用法
