---
title: PyTorch
created: 2026-04-11
updated: 2026-04-11
type: concept
tags: [deep-learning, framework]
sources:
  - concepts/cuda-toolkit-安装与路径管理.md
---

# PyTorch

> Stub page — 待补充详细内容

## 概述

PyTorch 是由 Meta（Facebook）开发的开源深度学习框架，广泛用于研究和生产环境。

## 核心组件

- **torch**：张量计算和自动微分
- **torch.nn**：神经网络模块
- **torch.optim**：优化器
- **torchvision / torchaudio / torchtext**：领域专用库

## 安装与 CUDA 依赖

- PyTorch 版本与 CUDA Toolkit 版本需匹配
- 安装时通过 `--index-url` 指定 CUDA 版本（如 `cu121`、`cu118`）
- 也可以安装 CPU-only 版本

## 相关页面

- [[cuda-toolkit-安装与路径管理]] — PyTorch 依赖的 CUDA 环境配置
