---
title: GZUCM_VRVideo 交互系统
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [Unity, VR, XR Interaction, 抓取系统, 按钮交互, 材质切换]
sources:
  - /home/admin/wiki/raw/assets/GZUCM_VRVideo/Assets/Scripts/GrabAttachReturn.cs
  - /home/admin/wiki/raw/assets/GZUCM_VRVideo/Assets/Scripts/ButtonInteraction.cs
  - /home/admin/wiki/raw/assets/GZUCM_VRVideo/Assets/Scripts/CanvasController.cs
---

# GZUCM_VRVideo 交互系统

交互系统是 GZUCM_VRVideo 项目的用户输入处理核心，基于 Unity XR Interaction Toolkit 实现抓取、悬停、选择等 VR 交互功能。

## 系统组成

### 1. GrabAttachReturn（抓取返回系统）
**文件**: `GrabAttachReturn.cs`

**核心功能**:
- 记录物体原始位置和旋转
- 抓取时取消动画
- 释放时平滑返回原位

**工作流程**:
```
物体初始化 → 记录原始位置/旋转
     ↓
抓取事件 → transform.DOKill() → 取消进行中的动画
     ↓
释放事件 → DOMove() + DORotateQuaternion() → 平滑返回原位
```

**关键特性**:
- **DOTween 动画**: 使用 DOTween 实现平滑动画
- **防抖处理**: 检查 `args.isCanceled` 防止误触
- **内存管理**: 在 OnDestroy 中移除事件监听

### 2. ButtonInteraction（按钮交互系统）
**文件**: `ButtonInteraction.cs`

**核心功能**:
- 实现 IPointerEnterHandler/IPointerExitHandler 接口
- 控制按钮 Image 显示/隐藏
- 管理二级菜单显示

**交互逻辑**:
```
指针进入 → 显示按钮 Image → 显示二级菜单
     ↓
指针离开 → 隐藏按钮 Image → 隐藏二级菜单
```

**状态管理**:
- 检查按钮 interactable 状态
- 根据状态设置颜色
- 控制二级菜单显隐

### 3. CanvasController（Canvas 控制器）
**文件**: `CanvasController.cs`

**核心功能**:
- 处理 XR 选择和悬停事件
- 控制媒体显示
- 管理材质切换

**XR 事件**:
- `OnSelectEnter()`: 选择物体时触发媒体显示
- `OnHoverEntered()`: 悬停时切换到 Hover 材质
- `OnHoverExited()`: 离开时恢复 Trigger 材质
- `OnSelectExited()`: 选择结束时的处理

## 交互事件流

### 抓取交互
```
XRGrabInteractable → selectEntered → HandleGrab()
     ↓
XRGrabInteractable → selectExited → HandleRelease()
     ↓
DOTween 动画 → 平滑返回原位
```

### 悬停交互
```
XR Interactable → hoverEntered → OnHoverEntered()
     ↓
切换材质 → Hover_Mat → 视觉反馈
     ↓
XR Interactable → hoverExited → OnHoverExited()
     ↓
恢复材质 → Trigger_Mat → 恢复默认状态
```

### 选择交互
```
XR Interactable → selectEntered → OnSelectEnter()
     ↓
获取 InteractableData → 查询数据 → 显示媒体
     ↓
XR Interactable → selectExited → OnSelectExited()
```

## 关键算法

### 1. 抓取返回动画
```csharp
private void HandleRelease(SelectExitEventArgs args)
{
    // 防抖处理
    if (args.isCanceled) return;
    
    // 平滑返回原位
    transform.DOMove(originalPosition, 1f).SetEase(Ease.OutSine);
    transform.DORotateQuaternion(originalRotation, 1f).SetEase(Ease.OutSine);
}
```

### 2. 材质切换
```csharp
public void OnHoverEntered(HoverEnterEventArgs args)
{
    GameObject hoverObject = args.interactableObject.transform.gameObject;
    MeshRenderer outline = hoverObject.GetComponent<MeshRenderer>();
    outline.material = Hover_Mat;
}

public void OnHoverExited(HoverExitEventArgs args)
{
    GameObject hoverObject = args.interactableObject.transform.gameObject;
    MeshRenderer outline = hoverObject.GetComponent<MeshRenderer>();
    outline.material = Trigger_Mat;
}
```

### 3. 按钮状态管理
```csharp
public void OnPointerEnter(PointerEventData eventData)
{
    if (!buttonToControl.interactable) return;
    
    if (buttonImage != null)
    {
        buttonImage.enabled = true;
    }
    
    if (secondMenuButtons != null)
    {
        secondMenuButtons.SetActive(true);
    }
}
```

## 配置指南

### 1. 抓取系统配置
1. **GrabAttachReturn**: 挂载在可抓取物体上
2. **XRGrabInteractable**: 确保物体有此组件
3. **DOTween**: 确保项目已导入 DOTween

### 2. 按钮交互配置
1. **ButtonInteraction**: 挂载在按钮上
2. **Button**: 确保有 Button 组件
3. **Image**: 配置按钮 Image 组件
4. **secondMenuButtons**: 拖入二级菜单引用

### 3. Canvas 控制器配置
1. **CanvasController**: 挂载在 Canvas 控制物体上
2. **材质配置**: 设置 Trigger_Mat 和 Hover_Mat
3. **XR 事件**: 在 XR Interactable 中配置事件

## 交互反馈设计

### 视觉反馈
1. **材质切换**: 悬停时改变材质
2. **按钮高亮**: 悬停时显示按钮 Image
3. **菜单显示**: 悬停时显示二级菜单

### 动画反馈
1. **抓取动画**: 抓取时取消返回动画
2. **返回动画**: 释放时平滑返回原位
3. **UI 动画**: 可集成 DOTween 实现 UI 动画

## 高级功能

### 1. 多层级交互
- 支持父物体和子物体交互
- 支持交互优先级
- 支持交互冲突解决

### 2. 交互条件
- 支持交互前置条件
- 支持交互权限控制
- 支持交互状态检查

### 3. 交互历史
- 记录交互历史
- 支持撤销操作
- 支持交互重放

## 调试方法

### 1. 抓取调试
- 检查 XRGrabInteractable 配置
- 验证事件监听是否正确
- 监控 DOTween 动画状态

### 2. 悬停调试
- 检查材质引用
- 验证事件触发
- 监控材质切换

### 3. 按钮调试
- 检查按钮 interactable 状态
- 验证事件绑定
- 监控 UI 状态变化

## 常见问题

### 1. 抓取不工作
- 检查 XRGrabInteractable 组件
- 验证事件监听绑定
- 检查 DOTween 引用

### 2. 材质不切换
- 检查材质引用
- 验证 MeshRenderer 组件
- 检查事件触发

### 3. 按钮无响应
- 检查 Button 组件
- 验证事件绑定
- 检查 interactable 状态

## 扩展可能性

### 1. 新交互类型
- 支持手势交互
- 支持语音交互
- 支持眼动追踪

### 2. 交互增强
- 支持力反馈
- 支持声音反馈
- 支持粒子效果

### 3. 交互分析
- 记录交互数据
- 分析用户行为
- 优化交互设计

## 相关页面

- [[gzucm-vrvideo-unity-project]] — 主项目页面
- [[gzucm-vrvideo-media-system]] — 媒体展示系统
- [[gzucm-vrvideo-teleport-system]] — 传送系统
- [[gzucm-vrvideo-ui-system]] — UI 系统