---
title: WebGL Development
created: 2026-04-11
updated: 2026-04-11
type: concept
tags: [WebGL, Unity, HTML, JavaScript, 3D Rendering, Video Player, Shader]
sources:
  - /home/admin/wiki/_staging/html-69706fbf-2b9c-8323-b9c1-ebbd8dd21d1f-202601-61bd55ad8e1c.md
  - /home/admin/wiki/_staging/webgl-0ee56949-dd58-4145-b354-193b9443cd0c-20231-5945ca3b4461.md
  - /home/admin/wiki/_staging/webgl-0f769cd5-f062-4217-8632-694401497d12-20230-f7b8cef16e56.md
  - /home/admin/wiki/_staging/webgl-d61cc2e3-5e31-46f5-a949-a36e228cd963-20230-d637b5a60603.md
  - /home/admin/wiki/_staging/webgl-a48bbbdf-901f-4de9-ae11-d6d45506ce66-20231-91cca4158466.md
---

# WebGL Development

基于 Unity 的 WebGL 开发涉及跨平台构建、HTML 容器适配、视频播放策略、Shader 兼容性等多个技术维度。

## Unity WebGL 项目核心技术栈

**常见技术关键词：**
- URP（Universal Render Pipeline）渲染管线
- AVPro / VideoPlayer WebGL 视频播放（尤其自动播放限制）
- URP Water Shader 兼容性（Shader Variant / Graphics Settings）
- 室内光照优化（GI / Light Probe / AO / Probe Ambient Occlusion）
- Animator Trigger + Clip 时长控制 + hasTriggeredAnimation 防二次触发
- InteractionManager 多步骤流程控制（UI + 模型联动）
- 射线点击识别模型触发动画

## 画面适配

WebGL 的 HTML 容器适配要点：

- 使用 CSS Flexbox 居中 Unity 容器：`display: flex; justify-content: center; align-items: center`
- 设置 `#unity-container` 宽高为 100% 或具体尺寸
- 处理不同设备的分辨率与纵横比
- TemplateData 中的 CSS 和 favicon 配置

**常见问题：**
- Unity 包依赖错误（如 PICO XR SDK 缺失）导致项目无法打开
- 需手动修改 Packages/manifest.json 或重新导入依赖

## 3D 互动流程管理

以"广陈皮"项目为例的 WebGL 3D 互动流程：

- 基于 InteractionManager 实现多步骤流程控制
- UI 与 3D 模型联动
- 射线检测（Raycast）识别模型点击
- Animator Trigger 驱动动画，Clip 时长控制结束回调
- hasTriggeredAnimation 防止二次触发

## HTML 页面积木渲染

使用纯 HTML/JS 在浏览器中渲染积木结构：

- 定义积木类型（正方体、长方体等）与数量
- 使用 Three.js 或类似库渲染 3D 积木
- 鼠标拖动旋转观察
- 注意积木间体积导致的重合问题
- 参考 bricks_preview_cdn 的尺寸定义

## WebGL 开发文档要点

Unity WebGL 应用的开发文档应包含：

1. **项目概述** — 功能说明、技术选型
2. **用户界面与交互** — UI 架构、交互流程
3. **部署与维护** — 重点内容
   - 打包后的 WebGL 应用部署在 IIS 上
   - 局域网内使用多种类型设备打开网页测试
   - 操作步骤及意义说明

## 相关页面

- [[ue5-development]] — UE5 开发
- [[unity-development-core]] — Unity 开发基础
- [[xr-vr-ar-development]] — XR/VR/AR 开发
