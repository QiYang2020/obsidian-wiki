---
title: GZUCM_VRVideo 传送系统
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [Unity, VR, 传送系统, 标签传送, 确认对话框, XR交互]
sources:
  - /home/admin/wiki/raw/assets/GZUCM_VRVideo/Assets/Scripts/TeleportManager.cs
---

# GZUCM_VRVideo 传送系统

传送系统是 GZUCM_VRVideo 项目的核心导航功能，通过基于标签的传送机制实现 VR 环境中的快速位置移动。

## 系统组成

### 1. TeleportManager（传送管理器）
**文件**: `TeleportManager.cs`

**核心功能**:
- 管理传送目的地配置
- 处理传送确认流程
- 控制菜单显示/隐藏
- 集成输入系统

**关键组件**:
```csharp
public InputActionReference Open_Btn;      // 打开菜单的输入动作
public XROrigin xrRig;                    // XR Rig 引用
public List<TeleportDestination> destinations; // 传送目的地列表
public GameObject Menu;                   // 菜单 UI
public GameObject TipsPage;               // 提示页面
```

### 2. TeleportDestination（传送目的地）
**文件**: `TeleportManager.cs` (内部类)

**数据结构**:
```csharp
[System.Serializable]
public class TeleportDestination
{
    public Button button;  // 触发传送的按钮
    public string tag;     // 目标物体的标签
}
```

## 传送流程

### 1. 菜单打开
```
输入动作触发 → OpenMenu() → 切换菜单显示状态
```

### 2. 目的地选择
```
按钮点击 → OpenTips(tag) → 显示确认对话框
```

### 3. 传送确认
```
确认按钮点击 → ChangeScene() → TeleportToTag(tag) → 位置移动
```

### 4. 传送取消
```
取消按钮点击 → Cancle() → 隐藏提示框，显示菜单
```

## 关键算法

### 1. 基于标签的传送
```csharp
public void TeleportToTag(string tag)
{
    GameObject targetLocation = GameObject.FindGameObjectWithTag(tag);
    if (targetLocation != null)
    {
        xrRig.transform.position = targetLocation.transform.position;
    }
    else
    {
        Debug.LogWarning("No GameObject found with tag: " + tag);
    }
}
```

### 2. 动态按钮事件绑定
```csharp
void Start()
{
    // 为每个目的地添加按钮点击事件
    foreach (var destination in destinations)
    {
        destination.button.onClick.AddListener(delegate { OpenTips(destination.tag); });
    }
}
```

### 3. 输入系统集成
```csharp
void Awake()
{
    // 绑定输入动作事件
    Open_Btn.action.performed += OpenMenu;
}
```

## UI 控制逻辑

### 菜单状态管理
```csharp
public void OpenMenu(InputAction.CallbackContext context)
{
    // 切换菜单显示状态
    Menu.SetActive(!Menu.activeSelf);
    if (Menu.activeSelf)
    {
        TipsPage.SetActive(false);
    }
}
```

### 提示框管理
```csharp
void OpenTips(string tag)
{
    GameObject targetLocation = GameObject.FindGameObjectWithTag(tag);
    if (targetLocation != null)
    {
        string objectName = targetLocation.name;
        TargetName = tag;
        TipsPage.SetActive(true);
        Menu.SetActive(false);
        Tips_text.text = "确定传送到 " + objectName + " 吗?";
    }
}
```

## 配置指南

### 1. 场景设置
1. **TeleportManager**: 场景中放置一个管理器
2. **xrRig**: 拖入 XR Origin 引用
3. **destinations**: 配置传送目的地列表

### 2. 目的地配置
1. **创建传送点**: 在场景中放置空物体作为传送目标
2. **设置标签**: 为每个传送点设置唯一标签
3. **配置按钮**: 在 UI 中创建对应按钮
4. **关联配置**: 将按钮和标签添加到 destinations 列表

### 3. 输入配置
1. **InputActionReference**: 配置打开菜单的输入动作
2. **XR Input**: 配置手柄按钮映射

## 交互流程示例

### 完整传送流程
1. **用户按下菜单按钮** → 打开传送菜单
2. **选择目的地** → 显示确认对话框
3. **确认传送** → 移动到目标位置
4. **自动关闭菜单** → 返回 VR 场景

### 取消流程
1. **选择目的地** → 显示确认对话框
2. **取消传送** → 关闭提示框，返回菜单

## 高级功能

### 1. 多级菜单支持
- 支持嵌套菜单结构
- 支持返回上级菜单
- 支持菜单状态记忆

### 2. 传送动画
- 可集成 DOTween 实现平滑传送
- 支持传送特效
- 支持传送音效

### 3. 传送限制
- 支持传送冷却时间
- 支持传送条件检查
- 支持传送权限控制

## 调试方法

### 1. 传送调试
- 检查标签是否正确设置
- 验证传送点位置
- 监控传送事件日志

### 2. UI 调试
- 检查按钮事件绑定
- 验证 UI 显示状态
- 监控 UI 交互日志

### 3. 常见问题
- **无法传送**: 检查标签和传送点配置
- **菜单不显示**: 检查 UI 引用和状态
- **输入无响应**: 检查 InputAction 配置

## 扩展可能性

### 1. 传送类型扩展
- 支持瞬移传送
- 支持平滑传送
- 支持传送动画

### 2. 传送条件
- 支持解锁条件
- 支持冷却时间
- 支持资源消耗

### 3. 传送历史
- 记录传送历史
- 支持快速传送
- 支持收藏传送点

## 相关页面

- [[gzucm-vrvideo-unity-project]] — 主项目页面
- [[gzucm-vrvideo-media-system]] — 媒体展示系统
- [[gzucm-vrvideo-interaction-system]] — 交互系统
- [[gzucm-vrvideo-ui-system]] — UI 系统