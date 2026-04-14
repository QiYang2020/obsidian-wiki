---
title: CameraPoint 相机点管理系统
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [UE5, 相机点, 全景相机, 导出工具, 蓝图]
sources:
  - /home/admin/wiki/raw/assets/UE5_PanoramiCamera/Content/Tools/CameraPoint/
---

# CameraPoint 相机点管理系统

CameraPoint 是 UE5 项目中的相机点管理系统，用于在虚拟展厅中创建、管理、导出和加载相机点位数据。

## 系统组成

### 核心工具

1. **ExportTool** (227KB): 主要导出工具，将相机点数据导出为JSON格式
2. **ExportTool_24** (226KB): 24帧版本的导出工具
3. **ExportTool_Camera360** (549KB): 360相机专用导出工具，功能最完整
4. **LoadTool** (189KB): 加载工具，从JSON文件导入相机点数据
5. **Old_LoadTool** (183KB): 旧版加载工具
6. **PointCreate** (286KB): 相机点创建工具，可视化创建相机点位
7. **PointManager** (94KB): 相机点管理器，管理多个相机点
8. **CameraPoint** (33KB): 基础相机点组件

### 辅助工具

1. **SkipFrame** (216KB): 跳帧处理工具，用于优化相机路径
2. **Frame_Point** (143KB): 画框点管理，与画框系统联动
3. **ToCamera** (99KB): 数据转换工具，将点数据转换为相机数据
4. **BP_EditorTicker** (45KB): 编辑器时钟，用于实时更新
5. **BPI_EditorTick** (8KB): 编辑器时钟接口

### 数据结构

1. **PointStruct** (4KB): 相机点数据结构
2. **PanoStruct** (5KB): 全景数据结构
3. **MappingStruct** (3KB): 映射数据结构

## 工作流程

### 1. 创建相机点
- 使用 **PointCreate** 工具在场景中放置相机点
- 设置每个点的位置、旋转、FOV等参数
- 通过 **PointManager** 管理多个相机点

### 2. 导出数据
- 使用 **ExportTool_Camera360** 导出相机点数据
- 支持导出为JSON格式，包含位置、旋转、帧号等信息
- 可配置导出帧率、起始帧、结束帧等参数

### 3. 加载数据
- 使用 **LoadTool** 从JSON文件加载相机点数据
- 自动在场景中重新创建相机点
- 支持批量加载和增量加载

### 4. 路径优化
- 使用 **SkipFrame** 进行跳帧处理，优化相机路径
- 通过 **Frame_Point** 与画框系统联动
- 使用 **ToCamera** 将点数据转换为相机数据

## 数据格式

导出的JSON文件格式：
```json
{
  "config": [
    {
      "frame": 0,
      "position": {"x": 0, "y": 0, "z": 0},
      "rotation": {"pitch": 0, "yaw": 0, "roll": 0}
    },
    ...
  ]
}
```

## 与其他系统的集成

- **[[frame-blueprint-system]]**: 通过 Frame_Point 与画框系统联动
- **[[sequence-automation-system]]**: 导出的JSON数据用于生成LevelSequence
- **Camera360v2插件**: 使用插件的全景相机功能

## 相关页面

- [[panorendering-project]] — 主项目页面
- [[frame-blueprint-system]] — 画框蓝图系统
- [[sequence-automation-system]] — 序列自动化系统