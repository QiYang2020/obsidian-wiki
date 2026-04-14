---
title: Level Management 展厅场景管理系统
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [UE5, 展厅, 场景管理, G04, Datasmith]
sources:
  - /home/admin/wiki/raw/assets/UE5_PanoramiCamera/Content/Tools/LEVEL/
  - /home/admin/wiki/raw/assets/UE5_PanoramiCamera/Content/Project/
---

# Level Management 展厅场景管理系统

Level Management 是 UE5 项目中的展厅场景管理系统，用于管理虚拟展厅的布局、模型、材质和灯光。

## 系统组成

### 1. 展厅场景

#### G04 展厅
**位置**: `LEVEL/OpenExhibition/G04/`

**模型文件**:
- **D_Side** (18KB): 展厅侧面
- **DaPengChe_Mat** (26KB): 大篷车材质
- **HuaDuo_Mat** (25KB): 花朵材质
- **HuoShenGuo_Mat** (22KB): 火参果材质
- **LaBa_Mat** (25KB): 喇叭材质
- **Toy_Mat** (17KB): 玩具材质
- **TuZi_Mat** (23KB): 兔子材质
- **YuTouRen_Mat** (25KB): 鱼头人材质

**展厅结构**:
- **baiA01** (19KB): 白色A01结构
- **fangban_01** (22KB): 方板结构
- **zhuozi_01** (21KB): 桌子结构
- **toy** (303KB): 玩具模型

**大型立牌模型**:
- 兔子立牌 (6.4MB)
- 喇叭立牌 (7.6MB)
- 大篷车 (7.9MB)
- 火参果立牌 (4.6MB)
- 花朵立牌 (7.3MB)
- 鱼头人立牌 (8.3MB)

### 2. 项目场景

#### Hall001, Hall002, Hall003
**位置**: `Content/Project/`

**结构**:
- **Hall001/**: 展厅001
  - Show001/: 展示001
    - Level/: 关卡文件
- **Hall002/**: 展厅002
  - Show001/: 展示001
    - Datasmith/: Datasmith导入资源
      - wuliao/: 物料资源
      - 2tietu/: 2D贴图资源
      - project2/: 项目2资源
    - Level/: 关卡文件
    - IES/: IES灯光文件
- **Hall003/**: 展厅003
  - Show001/: 展示001
    - Datasmith/: Datasmith导入资源
      - 3_1/: 3.1资源
      - 3mentietu/: 3D面贴图资源
    - Level/: 关卡文件
    - IES/: IES灯光文件
    - Material/: 材质文件
    - Model/: 模型文件

### 3. 测试场景

#### Example_6_task_solution
**位置**: `LEVEL/Example_6_task_solution.umap`

用于测试任务解决方案的示例场景。

## Datasmith 工作流

### 资源导入流程
1. **3D建模**: 在 3ds Max / Blender / SketchUp 中创建模型
2. **UV设置**: 确保至少两套UV映射
   - 第一套UV: 材质贴图
   - 第二套UV: 光照烘焙（Lightmap）
3. **Datasmith导出**: 使用Datasmith导出资源
4. **UE5导入**: 在UE5中导入Datasmith资源
5. **资源整理**: 在UE5中整理资源到对应目录

### 目录结构规范
```
HallXXX/
├── ShowXXX/
│   ├── Datasmith/
│   │   ├── 资源名/
│   │   │   ├── Textures/
│   │   │   ├── Geometries/
│   │   │   └── Materials/
│   │   │       └── References/
│   ├── Level/
│   ├── IES/
│   ├── Material/
│   └── Model/
```

## 与其他系统的集成

### 与 [[frame-blueprint-system]] 的集成
- 展厅中的画框使用 Frame Blueprint 系统管理
- 画框的材质、模型、动画由 Frame Blueprint 控制
- 展厅场景为画框提供放置环境

### 与 [[camera-point-system]] 的集成
- 相机点放置在展厅场景中
- 相机路径受展厅布局约束
- 展厅场景为相机提供渲染环境

## 使用场景

1. **展厅搭建**: 快速搭建虚拟展厅
2. **资源管理**: 管理展厅中的各种资源
3. **灯光设置**: 设置展厅灯光和IES配置
4. **材质管理**: 管理展厅材质和贴图

## 相关页面

- [[panorendering-project]] — 主项目页面
- [[frame-blueprint-system]] — 画框蓝图系统
- [[camera-point-system]] — 相机点管理系统
- [[ue5-development]] — UE5 开发基础