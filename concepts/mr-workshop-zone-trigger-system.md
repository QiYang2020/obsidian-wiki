---
title: MR Workshop 区域触发系统
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [Unity, MR, 区域触发, 计时系统, JSON配置, 可视化]
sources:
  - /home/admin/wiki/raw/assets/MR_Workshop/Assets/MRInteraction/Script/Zone/
---

# MR Workshop 区域触发系统

区域触发系统是 MR_Workshop 项目的核心游戏机制，通过检测物体在指定区域内的停留时间来触发游戏事件。

## 系统架构

### 核心组件

#### 1. ZoneTrigger（区域触发器）
**文件**: `ZoneTrigger.cs`

**核心功能**:
- 检测物体进入、停留、离开区域
- 计时器管理（物体停留指定时间触发完成）
- 完成状态管理
- 可视化进度反馈

**状态机**:
```
未完成 → 物体进入 → 开始计时 → 达到时间 → 完成状态
   ↓         ↓         ↓         ↓         ↓
重置计时 ← 物体离开 ← 清空列表 ← 计时暂停 ← 触发事件
```

**关键字段**:
- `id`: 区域唯一标识
- `requiredSeconds`: 所需停留时间
- `validLayers`: 有效物体层级
- `IsComplete`: 完成状态

#### 2. ZoneGameManager（区域游戏管理器）
**文件**: `ZoneGameManager.cs`

**核心功能**:
- 管理所有区域触发器
- 检测所有区域完成条件
- 触发游戏结束事件

**工作流程**:
1. 场景加载时刷新所有 ZoneTrigger
2. 监听每个区域的完成事件
3. 检查所有区域是否都完成
4. 触发游戏结束逻辑

#### 3. ZoneRuntimeLoader（运行时加载器）
**文件**: `ZoneRuntimeLoader.cs`

**核心功能**:
- 从 JSON 文件加载区域配置
- 运行时动态生成区域
- 支持多场景切换

**JSON 数据格式**:
```json
{
  "version": 1,
  "zones": [
    {
      "id": "Z001",
      "scene": "PicoBuild01",
      "position": [x, y, z],
      "rotationEuler": [x, y, z],
      "size": [x, y, z],
      "requiredSeconds": 2.0
    }
  ]
}
```

#### 4. ZoneVisualMPB（区域可视化）
**文件**: `ZoneVisualMPB.cs`

**核心功能**:
- 使用 MaterialPropertyBlock 控制材质透明度
- 显示计时进度（从半透明到透明）
- 完成时隐藏区域

**可视化效果**:
- 初始状态: 半透明（startAlpha = 0.6）
- 计时过程: 逐渐变透明
- 完成状态: 完全透明（hideOnComplete = true）

#### 5. ZoneAuthoring（区域创作组件）
**文件**: `ZoneAuthoring.cs`

**核心功能**:
- 编辑器模式下的区域配置
- 自动配置 BoxCollider
- 用于静态区域创建

## 数据流

```
JSON配置 → ZoneRuntimeLoader → 生成ZoneTrigger → ZoneGameManager
   ↓
物体进入 → ZoneTrigger.StartTimer() → ZoneVisualMPB.SetProgress()
   ↓
计时完成 → ZoneTrigger.Complete() → ZoneGameManager.CheckAllComplete()
   ↓
所有完成 → ZoneGameManager.OnAllZonesCompleted() → 游戏结束
```

## 关键算法

### 1. 计时器管理
```csharp
void Update()
{
    if (_inside.Count > 0)
    {
        _timer += Time.deltaTime;
        _visual?.SetProgress(_timer / requiredSeconds);
        
        if (_timer >= requiredSeconds)
        {
            IsComplete = true;
            manager?.OnZoneCompleted(this);
        }
    }
}
```

### 2. 物体过滤
```csharp
bool IsValid(Collider col)
{
    int layer = col.gameObject.layer;
    return (validLayers.value & (1 << layer)) != 0;
}
```

### 3. 完成后触发
```csharp
private void OnEnterCompletedZone(Collider other)
{
    EventHandle.CallZoneComplectOnce();
    Debug.Log($"[Zone {id}] completed zone entered by: {other.name}");
}
```

## 配置指南

### 1. 场景设置
1. **ZoneTrigger**: 挂载在区域物体上
2. **ZoneVisualMPB**: 配置可视化效果
3. **ZoneGameManager**: 场景中放置一个管理器

### 2. JSON 配置
1. 在 `StreamingAssets` 目录放置 `zones.json`
2. 配置每个区域的位置、大小、时间
3. 设置 `validLayers` 过滤有效物体

### 3. 运行时加载
1. ZoneRuntimeLoader 自动加载 JSON
2. 根据当前场景过滤区域
3. 动态生成区域物体

## 高级功能

### 1. 区域撤销
- 物体离开已完成区域时撤销完成状态
- 重新进入时重新触发

### 2. 多物体支持
- 支持多个物体同时在一个区域
- 任一物体离开都可能触发撤销

### 3. 事件订阅
- 通过 `EventHandle` 订阅区域事件
- 支持一次性触发和重复触发

## 调试方法

### 1. 区域可视化
- 启用 `ZoneVisualMPB` 查看区域边界
- 观察透明度变化了解计时进度

### 2. 日志输出
- 查看 `[Zone]` 开头的日志
- 监控区域完成和撤销事件

### 3. 常见问题
- **区域不触发**: 检查 `validLayers` 配置
- **计时不准**: 调整 `requiredSeconds`
- **可视化异常**: 检查材质 Shader 属性

## 扩展可能性

### 1. 多阶段区域
- 支持多个完成阶段
- 不同阶段触发不同事件

### 2. 区域类型
- 添加不同形状（球形、圆柱形）
- 支持复杂区域组合

### 3. 动态调整
- 运行时修改区域属性
- 支持区域移动和变形

## 相关页面

- [[mr-workshop-unity-project]] — 主项目页面
- [[mr-workshop-hand-gesture-system]] — 手势交互系统
- [[mr-workshop-gameplay-system]] — 游戏逻辑系统
- [[mr-workshop-event-system]] — 事件通信系统