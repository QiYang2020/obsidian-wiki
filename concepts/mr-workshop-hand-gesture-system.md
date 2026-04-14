---
title: MR Workshop 手势交互系统
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [Unity, MR, 手势识别, Pico, 抓取, XR Interaction Toolkit]
sources:
  - /home/admin/wiki/raw/assets/MR_Workshop/Assets/MRInteraction/Script/XR/Pico/
---

# MR Workshop 手势交互系统

手势交互系统是 MR_Workshop 项目的核心交互方式，通过 Pico 设备的手势识别功能实现无控制器的自然交互。

## 系统组成

### 1. HandPoseGrabber（手势抓取器）
**文件**: `HandPoseGrabber.cs`

**核心功能**:
- 监听手势识别事件（Gesture Performed/Ended）
- 在手势识别时自动抓取最近的可交互物体
- 支持手动交互模式（Manual Interaction）

**工作流程**:
```
手势识别 → GrabOnPose() → 遍历hovered列表 → 选择最近物体 → StartManualInteraction()
手势结束 → ReleaseOnPoseEnd() → EndManualInteraction()
```

**关键设计**:
- 只抓取带有 `XRGrabInteractable` 组件的物体
- 使用距离排序选择最近物体
- 防止重复抓取（grabbed != null 检查）

### 2. SeeThrough（透视功能）
**文件**: `SeeThrough.cs`

**核心功能**:
- 启动时自动开启 Pico 的透视功能
- 实现 MR（混合现实）效果

**实现**:
```csharp
PXR_Manager.EnableVideoSeeThrough = true;
```

### 3. GestureDebugLogger（手势调试器）
**文件**: `GestureDebugLogger.cs`

**核心功能**:
- 记录手势识别和结束事件
- 用于调试和开发阶段

**事件**:
- `OnGesturePerformed()`: 手势识别成功
- `OnGestureEnded()`: 手势结束

## 与 XR Interaction Toolkit 的集成

### 手势驱动抓取流程
1. **手势识别**: Pico SDK 识别特定手势（如捏合）
2. **事件触发**: 调用 `HandPoseGrabber.GrabOnPose()`
3. **物体选择**: 遍历 `directInteractor.interactablesHovered`
4. **手动交互**: 调用 `StartManualInteraction(best)`
5. **抓取完成**: 物体跟随手部移动

### 释放流程
1. **手势结束**: Pico SDK 检测手势结束
2. **事件触发**: 调用 `HandPoseGrabber.ReleaseOnPoseEnd()`
3. **手动释放**: 调用 `EndManualInteraction()`
4. **物理恢复**: 物体恢复物理行为

## 技术特点

### 1. 距离优先选择
```csharp
float sqr = (interactable.transform.position - directInteractor.transform.position).sqrMagnitude;
if (sqr < bestSqr)
{
    bestSqr = sqr;
    best = interactable;
}
```

### 2. 防重复抓取
```csharp
if (grabbed != null) return;
```

### 3. 手动交互模式
使用 `StartManualInteraction` 而不是自动交互，提供更精确的控制。

## 配置要求

### Unity 设置
1. **XR Interaction Toolkit**: 版本 2.3+
2. **PXR SDK**: Pico 设备专用 SDK
3. **XR Direct Interactor**: 配置在手部预制体上

### 场景设置
1. **HandPoseGrabber**: 挂载在手部物体上
2. **directInteractor**: 拖入 XR Direct Interactor 组件
3. **SeeThrough**: 挂载在场景根物体上

## 调试方法

### 1. 手势日志
- 查看控制台 `[Gesture] PERFORMED` 和 `[Gesture] ENDED`
- 确认手势识别是否正常

### 2. 抓取调试
- 取消注释 `HandPoseGrabber` 中的调试代码
- 查看 hovered 列表和抓取过程

### 3. 常见问题
- **无法抓取**: 检查物体是否有 `XRGrabInteractable` 组件
- **抓取错误物体**: 调整物体距离或层级过滤
- **手势不识别**: 检查 PXR SDK 配置

## 扩展可能性

### 1. 多手势支持
- 添加不同手势类型（捏合、抓握、指向）
- 实现手势优先级系统

### 2. 手势反馈
- 添加 haptic 反馈
- 实现手势进度可视化

### 3. 手势学习
- 添加手势训练模式
- 支持自定义手势

## 相关页面

- [[mr-workshop-unity-project]] — 主项目页面
- [[mr-workshop-zone-trigger-system]] — 区域触发系统
- [[mr-workshop-gameplay-system]] — 游戏逻辑系统
- [[mr-workshop-event-system]] — 事件通信系统