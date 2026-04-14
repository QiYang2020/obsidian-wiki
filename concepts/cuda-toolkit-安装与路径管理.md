---
title: CUDA Toolkit 安装与路径管理
created: 2026-04-11
updated: 2026-04-11
type: concept
tags: [cuda, nvidia, windows, environment, devops]
sources:
  - raw/inbox/chatgpt_personal_backup_2026-04-10_md/CUDA安装与路径管理_69bb58e4-28f4-83ab-8fa9-54fc1ab04014_20260319_100209.md
---

# CUDA Toolkit 安装与路径管理

## 核心结论

- CUDA Toolkit **不必装在系统盘**，可自由选择安装目录（如 `D:\CUDA\CUDA\v12.3`）
- 删除后可重新安装到其他盘，只要环境变量正确即可
- CUDA 支持**多版本共存**，通过切换 `CUDA_PATH` 控制使用哪个版本

## 安装位置

默认路径：`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\vXX.X`

这只是 NVIDIA 安装器的默认设定，并非强制要求。安装时选择 **Custom Installation** 即可修改路径。

## 环境变量配置

安装到非系统盘后，需手动设置：

| 变量 | 值 |
|------|-----|
| `CUDA_PATH` | `D:\CUDA\CUDA\v12.3` |
| `PATH`（追加） | `D:\CUDA\CUDA\v12.3\bin` |
| `PATH`（追加） | `D:\CUDA\CUDA\v12.3\libnvvp` |

验证命令：`nvcc -V`

## 多版本共存

支持同时安装多个版本（如 v11.8 和 v12.3），通过 `CUDA_PATH` 环境变量切换。不同框架可能绑定特定 CUDA 版本（如 [[pytorch]]、TensorFlow），需注意兼容性。

## 迁移注意事项

- **动态查找 CUDA 的项目**（推荐）：只需改环境变量，工程自动适配
- **硬编码路径的项目**：需修改代码或用环境变量"模拟"旧路径
- 删除前确认是否有强依赖当前版本的框架或编译产物

## 相关页面

- [[pytorch]] — 深度学习框架，不同版本绑定特定 CUDA
- [[environment-variable-management]] — 环境变量管理通用实践
