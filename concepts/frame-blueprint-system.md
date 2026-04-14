---
title: Frame Blueprint 画框蓝图系统
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [UE5, 画框, 蓝图, 材质管理, 数据流]
sources:
  - /home/admin/wiki/raw/assets/UE5_PanoramiCamera/Content/Tools/Frame_Blueprint/
  - /home/admin/wiki/raw/assets/UE5_PanoramiCamera/Content/Tools/Frame_BlueprintV2/
---

# Frame Blueprint 画框蓝图系统

Frame Blueprint 是 UE5 项目中的画框管理系统，用于在虚拟展厅中管理画框的材质、模型、动画和数据流。系统有两个版本，V2 是简化重构版。

## 系统版本

### Frame_Blueprint (V1)
第一代画框系统，包含完整的上下游数据流和材质管理。

**核心组件：**
- **Frame_Blueprint** (195KB): 主画框蓝图
- **Frame_Stream** (378KB): 画框数据流
- **UpStream** (300KB): 上游数据流
- **DownStream** (634KB): 下游数据流（最大组件）
- **MatStream** (78KB): 材质数据流
- **Frame_Ani** (304KB): 画框动画系统
- **Luminous_Blueprint** (192KB): 发光画框蓝图
- **Manager** (26KB): 画框管理器

### Frame_BlueprintV2 (V2)
第二代画框系统，重构简化，使用数据资产方式。

**核心组件：**
- **PrimaryFrame** (34KB): 主画框组件
- **DataAssetsTool** (78KB): 数据资产工具
- **FrameModel** (373KB): 画框模型管理

## 数据流架构

### V1 数据流
```
UpStream (上游数据)
    ↓
Frame_Stream (画框数据流)
    ↓
DownStream (下游数据)
    ↓
MatStream (材质数据流)
    ↓
Frame_Ani (动画系统)
```

### V2 数据流
```
DataAssetsTool (数据资产)
    ↓
PrimaryFrame (主画框)
    ↓
FrameModel (模型管理)
```

## 材质系统

### 材质管理
- **Material/**: 画框材质库
  - Luminous_Material: 发光材质
  - PaintingMaterial: 绘画材质
- **Test_Mat/**: 测试材质库（30+ 种材质）
  - 金属材质: alloy_black, alloy_gray, alloy_white
  - 颜色材质: lan000 (蓝), huangse000 (黄), hongse000 (红)
  - 特殊材质: baitouming (半透明), jinshubaise_000 (金属白)

### 材质数据
- **Data/MaterialLibrary**: 材质库管理
- **Data/GlobalMaterialLibrary**: 全局材质库
- **Data/MaterialUpdaterUtility**: 材质更新工具

## 模型系统

### 模型管理
- **Model/ModelDataGroup**: 模型数据组
- **Model/SculptureStream**: 雕塑数据流

### 模型文件
- **Model/FBX/Frame/**: 画框模型
  - Frame_A_fix_: 画框A修复版
  - m_frame: 画框材质
  - m_painting: 绘画材质
- **Model/FBX/ZhanTing/**: 展厅模型
  - G04/: G04展厅模型
  - G09/: G09展厅模型

## 动画系统

- **Frame_Ani**: 画框动画控制器
- **Data/ActorToData**: Actor到数据转换
- **Data/FrameData**: 画框数据
- **Data/SetFrameData**: 设置画框数据

## 与 [[camera-point-system]] 的集成

1. **Frame_Point**: 画框点管理，与相机点系统联动
2. **数据共享**: 画框数据和相机点数据共享数据结构
3. **路径规划**: 画框系统为相机路径提供约束

## 使用场景

1. **展厅画框管理**: 批量管理展厅中的画框
2. **材质切换**: 快速切换画框材质
3. **动画控制**: 控制画框的显示动画
4. **数据导出**: 导出画框数据用于其他系统

## 相关页面

- [[panorendering-project]] — 主项目页面
- [[camera-point-system]] — 相机点管理系统
- [[level-management-system]] — 展厅场景管理