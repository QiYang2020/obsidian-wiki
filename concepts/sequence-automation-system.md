---
title: Sequence Automation 序列自动化系统
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [UE5, Python脚本, 序列自动化, LevelSequence, JSON配置]
sources:
  - /home/admin/wiki/raw/assets/UE5_PanoramiCamera/Content/Tools/Sequence/
---

# Sequence Automation 序列自动化系统

Sequence Automation 是 UE5 项目中的序列自动化系统，通过 Python 脚本从 JSON 配置文件自动生成 LevelSequence，实现相机路径的自动化创建。

## 系统组成

### 核心组件

1. **CreateLevelSequenceFromTemplate.py**: 主要脚本，从JSON配置创建LevelSequence
2. **old_CreateLevelSequenceFromTemplate.py**: 旧版本脚本
3. **TemplateSequence.uasset**: 序列模板文件
4. **ExampleLevelSequence.uasset**: 示例序列
5. **Camera360_Hall0002Sequence.uasset**: 相机360展厅002序列

### 配置文件

1. **0802_MoviePipelinePrimaryConfig.uasset**: 电影管道主配置
2. **Pending_MoviePipelinePrimaryConfig.uasset**: 待处理电影管道配置

## 工作流程

### 1. 准备JSON配置文件
JSON配置文件格式：
```json
{
  "config": [
    {
      "frame": 0,
      "position": {"x": 0, "y": 0, "z": 0},
      "rotation": {"pitch": 0, "yaw": 0, "roll": 0}
    },
    {
      "frame": 1,
      "position": {"x": 100, "y": 0, "z": 0},
      "rotation": {"pitch": 0, "yaw": 0, "roll": 0}
    }
  ]
}
```

### 2. 运行Python脚本
在UE5编辑器中运行Python脚本：
1. 打开UE5编辑器
2. 打开Python控制台
3. 运行 `CreateLevelSequenceFromTemplate.py` 脚本

### 3. 脚本执行流程
1. **加载模板**: 加载 `TemplateSequence` 作为模板
2. **检查目标**: 检查目标序列是否已存在，如果存在则删除
3. **复制序列**: 从模板复制创建新序列
4. **读取配置**: 读取JSON配置文件，支持多种编码格式
5. **查找轨道**: 查找相机绑定和Transform轨道
6. **设置范围**: 根据配置设置序列时间范围
7. **添加关键帧**: 为每个配置点添加位置关键帧
8. **保存序列**: 保存序列到Content目录

### 4. 关键帧设置
- **插值模式**: 使用 `RCIM_CONSTANT`（常量插值）
- **关键帧间隔**: 每个配置点对应一个关键帧
- **最后一帧处理**: 确保最后一帧与前一帧相同，避免循环问题

## 脚本版本对比

### 旧版本 (old_CreateLevelSequenceFromTemplate.py)
- **配置路径**: `D:\fxy\Test\Frame_Tool\json\Hall0018_idXYZ.json`
- **级别名称**: `Hall0018_Show001`
- **关键帧逻辑**: 每个配置点对应2帧，只使用偶数帧

### 新版本 (CreateLevelSequenceFromTemplate.py)
- **配置路径**: `D:\fxy\Test\FrameTool\json\2025\0326\Frame_Camera360\Hall002_idXYZ_Seq.json`
- **级别名称**: `Camera360_Hall0002`
- **关键帧逻辑**: 直接使用配置中的帧号，更简洁

## 与其他系统的集成

### 与 [[camera-point-system]] 的集成
- JSON配置文件由 CameraPoint 系统导出
- 相机点数据转换为序列关键帧
- 实现从静态点到动态路径的转换

### 与 [[frame-blueprint-system]] 的集成
- 序列中的相机路径可以驱动画框动画
- 画框的显示时机可以与相机路径同步

### 与 [[level-management-system]] 的集成
- 序列在特定展厅场景中播放
- 相机路径受展厅布局约束

## 使用场景

1. **相机路径自动化**: 自动创建相机飞行路径
2. **展厅导览**: 创建展厅自动导览序列
3. **渲染序列**: 为渲染输出创建相机序列
4. **批量处理**: 批量创建多个展厅的相机序列

## 扩展可能性

1. **多相机支持**: 支持多个相机同时创建序列
2. **动画集成**: 集成画框动画到相机序列
3. **实时预览**: 在编辑器中实时预览相机路径
4. **批量导出**: 批量导出多个展厅的序列

## 相关页面

- [[panorendering-project]] — 主项目页面
- [[camera-point-system]] — 相机点管理系统
- [[frame-blueprint-system]] — 画框蓝图系统
- [[level-management-system]] — 展厅场景管理