---
title: 杂项开发笔记
created: 2026-04-11
updated: 2026-04-11
type: concept
tags: [unity, shader, webgl, playcanvas, misc]
sources:
  - _staging/shader-696dfdd0-dccc-8326-81a4-455ab3c52a3b-2026-a4fe45c98682.md
  - _staging/playcanvas-gltf-68b57060-f6b8-8329-ac51-c57b14c5-cae01f8afecd.md
  - _staging/6775e7db-5150-800d-831b-2f0e2357b8f6-20250102-09-bfe68ec4a81a.md
  - _staging/transition-logic-trbleshooting-48e0f336-37a1-4-beba4be159af.md
  - _staging/ui-74785af6-f450-48f5-81f0-0437715bea28-20231016-9ee118b24b8c.md
  - _staging/6895c071-fd90-832d-bcee-5a5cfc9fe61b-20250808-17-eb50171c9d32.md
  - _staging/68fde96c-3374-8323-8b08-0d686ab6d09f-20251026-17-bb4f19fedb1e.md
  - _staging/cff2037f-3c27-4f4f-95d1-f49ffdc38486-20230712-16-e362b8ea5ad9.md
  - _staging/ve-682aa7b4-52f0-800d-afbf-0cda2e5163a0-20250519-41054fcd737b.md
  - _staging/123a4068-a321-46af-967f-807a7e709f48-20231117-19-a246c11ee642.md
---

# 杂项开发笔记

不属于主要主题集群的一次性对话和知识点汇总。每条记录保留核心要点，不展开长篇论述。

## Shader 工作原理（Amplify Shader Editor）

使用 Amplify Shader Editor 时，需要先理解示例 shader 的输入/输出管线再改造：
- 区分 Vertex Shader（顶点变换）和 Fragment Shader（像素着色）阶段
- ASE 节点图中的 Main Texture、Normal Map、Metallic/Smoothness 对应 Standard Shader 的 PBR 通道
- 改造时先确定目标渲染效果属于哪个 PBR 通道，再对应修改节点图
- 相关：[[unity-development-core]] 中的渲染管线知识

## PlayCanvas → glTF 转换思路

将 PlayCanvas 发布的模型 JSON 转换为 glTF 格式并在 Unity 中加载：
- PlayCanvas 发布格式为自定义 JSON（含层级、材质引用、动画数据）
- 转换路径：PlayCanvas JSON → 解析场景树 → 导出 glTF 2.0（.gltf/.glb）
- Unity 端可用 UnityGLTF 或自定义 Loader 加载 glTF
- 注意坐标系差异（PlayCanvas 右手系 vs Unity 左手系）和缩放因子
- 相关：[[webgl-development]] 中的 3D 互动流程

## 无限滚动（ScrollView）实现

Unity 中基于 ScrollRect 的无限滚动核心逻辑：
- 监听 ScrollRect.onValueChanged 回调
- 当 content 位置超出阈值时，将首/尾元素移至对端并更新数据
- 关键：用 RectTransform.anchoredPosition 判断边界，而非 content size
- 配合 Object Pool 复用 UI 元素避免 GC

## 场景状态机 Transition 调试

SceneState 的 InitializeTransitions 中，用 `transition.SetCondition(() => currentStep == stepIndex)` 作为关卡条件时：
- 闭包捕获的 `stepIndex` 是循环变量，需用局部副本避免所有 transition 绑定同一值
- 修正：`int capturedStep = stepIndex; transition.SetCondition(() => currentStep == capturedStep);`
- 这是 C# 闭包经典陷阱

## Unity HDRP UI 相机问题

HDRP 项目中专用 UI Camera 影响主画面的常见原因：
- UI Camera 的 Output 需设置为 Render Texture，再通过 Canvas Overlay 叠加
- 不要让 UI Camera 和 Main Camera 同时输出到 Screen
- 或者直接用 Screen Space - Overlay Canvas，无需单独 UI Camera
- 相关：[[unity-development-core]]

## 修正旋转方向（上下左右反转）

模型控制中旋转方向反了（抬头变低头）：
- 通常是输入轴映射与旋转轴不匹配
- 检查 `transform.Rotate()` 或 `Quaternion.Euler()` 的正负号
- 打包后崩溃但编辑器正常 → 可能是编辑器特有 API（如 `EditorGUILayout`）在 Runtime 被裁剪

## 智慧农业物联网平台

大宗农产品信息交流 Web 平台的技术要点：
- 前端：视频流实时预览（HLS/RTMP 转 WebRTC）
- IoT 接入：全景摄像头 + 云台摄像头，支持反向控制（PTZ）、夜视
- 数据层：农产品信息、地块信息、监控数据的时序存储
- 后台：设备管理、告警规则、数据报表

## 龙舟元宇宙课程设计

VR 龙舟竞速课程设计框架：
- 学习目标：团队协作、传统文化认知、运动技能
- 技术路线：Unity + XR Interaction Toolkit + 多人同步
- 场景设计：虚拟河道、观众区域、计分系统
- 相关：[[xr-vr-ar-development]]、[[unity-development-core]]

## VE 多人龙舟比赛流程

线下 VR 龙舟比赛现场配置：
- 设备：5 个电视（1 个服务端解说大屏 + 4 个投射 VR 画面）、主控区
- 流程：选手入场 → 设备检查 → 比赛开始 → 实时计分 → 颁奖
- 技术栈：Unity 多人网络 + 服务端解说视角 + 大屏 UI
