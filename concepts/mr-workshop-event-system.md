---
title: MR Workshop 事件通信系统
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [Unity, MR, 事件系统, 解耦通信, 静态事件, 命名池]
sources:
  - /home/admin/wiki/raw/assets/MR_Workshop/Assets/MRInteraction/Script/Events/
  - /home/admin/wiki/raw/assets/MR_Workshop/Assets/MRInteraction/Script/Utils/
---

# MR Workshop 事件通信系统

事件通信系统是 MR_Workshop 项目的核心架构组件，通过静态事件实现系统间解耦通信，支持计数更新、区域完成等关键事件。

## 系统组成

### 1. EventHandle（事件中心）
**文件**: `EventHandle.cs`

**核心功能**:
- 定义全局静态事件
- 提供事件触发方法
- 实现系统间解耦通信

**事件列表**:
```csharp
public static event Action<string, int> CountDelta;  // 计数变化事件
public static event Action ZoneComplectOnce;          // 区域完成事件
```

**触发方法**:
```csharp
public static void CallCountDelta(string id, int delta)
{
    CountDelta?.Invoke(id, delta);
}

public static void CallZoneComplectOnce()
{
    ZoneComplectOnce?.Invoke();
}
```

### 2. CloneNamePool（克隆名称池）
**文件**: `CloneNamePool.cs`

**核心功能**:
- 管理克隆物体的编号分配
- 支持编号回收和复用
- 使用栈结构实现后进先出

**核心机制**:
1. **编号分配**: 优先使用回收的编号，否则递增分配
2. **编号回收**: 物体销毁时回收编号
3. **名称解析**: 从物体名称解析编号

**数据结构**:
```csharp
static readonly Dictionary<string, Stack<int>> pool = new();      // 编号栈
static readonly Dictionary<string, HashSet<int>> inPool = new();  // 防重复
static readonly Dictionary<string, int> next = new();             // 下一个编号
```

**接口**:
- `Allocate(string id)`: 分配新编号
- `Release(string id, int index)`: 回收编号
- `TryParseIndex(string name, out int index)`: 解析名称中的编号

## 事件类型

### 1. CountDelta（计数变化事件）
**触发时机**:
- 物品被抓取时: `CallCountDelta(counterId, -1)`
- 物品掉落时: `CallCountDelta(counterId, +1)`

**订阅者**:
- `TextCounterManager`: 更新 UI 计数
- `CountBehavior`: 应用数量门控
- 其他需要响应计数变化的系统

**事件参数**:
- `string id`: 计数器标识
- `int delta`: 变化量（正数增加，负数减少）

### 2. ZoneComplectOnce（区域完成事件）
**触发时机**:
- 物体进入已完成区域时

**订阅者**:
- 游戏逻辑系统
- UI 系统
- 音效系统

## 通信架构

### 发布-订阅模式
```
事件发布者 → EventHandle → 事件订阅者
     ↓           ↓           ↓
CountBehavior → CountDelta → TextCounterManager
ZoneTrigger → ZoneComplectOnce → 游戏逻辑系统
```

### 解耦优势
1. **系统独立**: 各系统只依赖事件接口
2. **灵活扩展**: 新系统可轻松订阅现有事件
3. **易于维护**: 修改一个系统不影响其他系统

## 关键算法

### 1. 编号分配算法
```csharp
public static int Allocate(string id)
{
    InitIfNeeded(id, 0);
    
    if (pool[id].Count > 0)
    {
        int v = pool[id].Pop();
        inPool[id].Remove(v);
        return v;
    }
    
    int n = next[id];
    next[id] = n + 1;
    return n;
}
```

### 2. 编号回收算法
```csharp
public static void Release(string id, int index)
{
    if (index <= 0) return;
    InitIfNeeded(id, 0);
    
    if (inPool[id].Contains(index)) return;  // 防重复
    
    pool[id].Push(index);
    inPool[id].Add(index);
}
```

### 3. 名称解析算法
```csharp
public static bool TryParseIndex(string name, out int index)
{
    index = 0;
    if (string.IsNullOrEmpty(name)) return false;
    if (!name.StartsWith("clone")) return false;
    return int.TryParse(name.Substring(5), out index);
}
```

## 使用指南

### 1. 订阅事件
```csharp
void OnEnable()
{
    EventHandle.CountDelta += OnCountDelta;
}

void OnDisable()
{
    EventHandle.CountDelta -= OnCountDelta;
}

void OnCountDelta(string id, int delta)
{
    // 处理计数变化
}
```

### 2. 触发事件
```csharp
// 计数变化
EventHandle.CallCountDelta("brick", -1);

// 区域完成
EventHandle.CallZoneComplectOnce();
```

### 3. 使用命名池
```csharp
// 分配编号
int num = CloneNamePool.Allocate("brick");
gameObject.name = "clone" + num;

// 回收编号
if (CloneNamePool.TryParseIndex(gameObject.name, out int index))
{
    CloneNamePool.Release("brick", index);
}
```

## 最佳实践

### 1. 事件命名
- 使用清晰的动作描述（如 CountDelta）
- 避免过于通用的名称（如 OnEvent）

### 2. 参数设计
- 保持参数简单（基本类型）
- 避免传递复杂对象

### 3. 订阅管理
- 在 OnEnable 订阅，在 OnDisable 取消
- 避免内存泄漏

### 4. 错误处理
- 检查事件是否为空
- 处理异常情况

## 调试方法

### 1. 事件日志
```csharp
void OnCountDelta(string id, int delta)
{
    Debug.Log($"CountDelta: id={id}, delta={delta}");
}
```

### 2. 命名池调试
```csharp
Debug.Log($"Pool count: {pool[id].Count}");
Debug.Log($"Next number: {next[id]}");
```

### 3. 常见问题
- **事件不触发**: 检查订阅和触发时机
- **编号冲突**: 检查防重复逻辑
- **内存泄漏**: 确保取消订阅

## 扩展可能性

### 1. 新事件类型
- 添加更多游戏事件
- 支持事件优先级

### 2. 事件历史
- 记录事件历史
- 支持事件回放

### 3. 条件事件
- 支持条件触发
- 实现事件组合

## 相关页面

- [[mr-workshop-unity-project]] — 主项目页面
- [[mr-workshop-hand-gesture-system]] — 手势交互系统
- [[mr-workshop-zone-trigger-system]] — 区域触发系统
- [[mr-workshop-gameplay-system]] — 游戏逻辑系统