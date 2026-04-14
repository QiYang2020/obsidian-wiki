---
title: MR Workshop 游戏逻辑系统
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [Unity, MR, 游戏逻辑, 抓取生成, 计数系统, 蓝图搭建]
sources:
  - /home/admin/wiki/raw/assets/MR_Workshop/Assets/MRInteraction/Script/Gameplay/
  - /home/admin/wiki/raw/assets/MR_Workshop/Assets/MRInteraction/Script/ScriptableObject/
---

# MR Workshop 游戏逻辑系统

游戏逻辑系统是 MR_Workshop 项目的核心玩法实现，包含积木生成、计数管理、蓝图搭建等游戏机制。

## 系统组成

### 1. GrabSpawn（抓取生成系统）
**文件**: `GrabSpawn.cs`

**核心功能**:
- 抓取物体时记录原始位置
- 释放时在原位生成替身
- 支持无限补货机制

**工作流程**:
```
抓取 → 记录位置 → 释放 → 生成替身 → 设置替身状态
   ↓
替身设置 → 静止状态 → 延迟启用抓取 → 忽略碰撞 → 恢复物理
```

**关键特性**:
- **无限补货**: 每次抓取都生成新替身
- **延迟启用**: 替身生成后 1.5 秒才能抓取
- **物理控制**: 抓取时无重力，释放后冻结 1.5 秒
- **碰撞忽略**: 新旧物体间忽略碰撞

### 2. Grab_SpawnOnly（只生成不抓取）
**文件**: `Grab_SpawnOnly.cs`

**核心功能**:
- 与 GrabSpawn 类似，但只生成不抓取
- 用于"Home"物品，抓取后生成新物品
- 支持计数系统集成

**区别**:
- 只生成一次（spawnedOnce 标志）
- 生成后禁用自身脚本
- 集成 CountBehavior 和 TextCounterManager

### 3. CountBehavior（计数行为）
**文件**: `CountBehavior.cs`

**核心功能**:
- 跟踪物品被抓取和掉落
- 与计数系统交互
- 支持数量门控（gateByCount）

**状态管理**:
```
Home物品 → 被抓取 → 计数-1 → 标记为非Home
掉落检测 → 超出边界 → 计数+1 → 销毁物体
```

**门控机制**:
- 数量为 0 时禁用抓取
- 数量恢复时重新启用
- 防止在计数为 0 时抓取

### 4. TextCounter（文本计数器）
**文件**: `TextCounter.cs`

**核心功能**:
- 显示和更新计数数值
- 支持增减操作
- 使用 TextMeshPro 显示

**接口**:
- `GetValue()`: 获取当前数值
- `Add(int delta)`: 增加或减少数值

### 5. TextCounterManager（计数管理器）
**文件**: `TextCounterManager.cs`

**核心功能**:
- 管理多个 TextCounter
- 处理计数事件
- 管理克隆物品命名

**核心机制**:
1. **计数管理**: 监听 CountDelta 事件，更新对应计数器
2. **命名池**: 为克隆物品分配递增编号
3. **碰撞门控**: 根据数量控制最新克隆的碰撞体
4. **编号回收**: 物品销毁时回收编号

**命名系统**:
```
Home物品: prefabname1, prefabname2, prefabname3...
克隆物品: 自动递增编号
回收机制: 栈结构，支持编号复用
```

### 6. HighMission（高处停留任务）
**文件**: `HighMission.cs`

**核心功能**:
- 检测物体在区域内停留时间
- 触发 UnityEvent
- 支持一次性触发和重复触发

**工作流程**:
```
物体进入 → 记录时间 → 检测停留 → 达到时间 → 触发事件
```

### 7. BlueprintAsset（蓝图资产）
**文件**: `BlueprintAsset.cs`

**核心功能**:
- 定义搭建蓝图的积木配置
- 支持多种积木类型
- 定义容差和对称规则

**积木类型**:
- RectBlock: 长方体
- CubeBlock: 正方体
- CylinderLong: 长圆柱
- Triangle: 三角形
- Arch: 拱形

## 数据流

```
手势抓取 → GrabSpawn → 生成替身 → CountBehavior → 计数更新
   ↓
计数事件 → EventHandle → TextCounterManager → UI更新
   ↓
区域触发 → ZoneTrigger → ZoneGameManager → 游戏结束
```

## 关键算法

### 1. 无限补货机制
```csharp
void OnRelease(SelectExitEventArgs _)
{
    if (!spawnedReplacementOnce && prefabSpawn != null)
    {
        spawnedReplacementOnce = true;
        var clone = Instantiate(prefabSpawn, preGrabPos + worldOffset, preGrabRot);
        SetupReplacement(clone);
    }
}
```

### 2. 数量门控
```csharp
void ApplyGate()
{
    if (!gateByCount || !isHomeItem) return;
    int v = TextCounterManager.Instance.GetValue(counterId);
    _col.enabled = (v > 0);
    grab.enabled = (v > 0);
}
```

### 3. 编号回收
```csharp
public void RecycleTakenName(string id, string takenFullName)
{
    // 解析编号
    // 如果有Home物品，改名为回收编号
    // 否则压入栈中等待下次使用
}
```

## 配置指南

### 1. 物品设置
1. **GrabSpawn**: 挂载在可抓取物品上
2. **prefabSpawn**: 拖入自身预制体
3. **CountBehavior**: 配置 counterId 和边界

### 2. 计数器设置
1. **TextCounter**: 挂载在 UI 文本上
2. **TextCounterManager**: 场景中放置一个管理器
3. **counters**: 拖入所有 TextCounter

### 3. 蓝图设置
1. **BlueprintAsset**: 创建 ScriptableObject
2. **pieces**: 配置积木列表
3. **tolerance**: 设置位置和旋转容差

## 调试方法

### 1. 计数调试
- 查看控制台计数变化日志
- 监控 TextCounter 数值变化

### 2. 生成调试
- 观察替身生成位置
- 检查延迟启用时间

### 3. 常见问题
- **计数不更新**: 检查 EventHandle 订阅
- **替身不生成**: 检查 prefabSpawn 配置
- **编号混乱**: 检查命名池逻辑

## 扩展可能性

### 1. 新积木类型
- 添加更多几何形状
- 支持复杂组合积木

### 2. 高级计数逻辑
- 支持多类型计数
- 实现组合条件

### 3. 蓝图验证
- 添加搭建完成检测
- 支持部分完成奖励

## 相关页面

- [[mr-workshop-unity-project]] — 主项目页面
- [[mr-workshop-hand-gesture-system]] — 手势交互系统
- [[mr-workshop-zone-trigger-system]] — 区域触发系统
- [[mr-workshop-event-system]] — 事件通信系统