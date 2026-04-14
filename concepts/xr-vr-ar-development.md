---
title: XR/VR/AR Development
created: 2026-04-11
updated: 2026-04-11
type: concept
tags:
  - xr
  - vr
  - ar
  - openxr
  - steamvr
  - hand-gesture
sources:
  - /home/admin/wiki/_staging/monado-openxr-67467cce-3940-800d-b692-95963715c4-76727e100f6d.md
  - /home/admin/wiki/_staging/steamvr-2-x-f7066030-70b0-4093-b6e4-bffa5ab20189-737a070d7bca.md
  - /home/admin/wiki/_staging/xr-interaction-toolkit-e262835c-ab8e-429a-b8bf-2-a0998b492513.md
  - /home/admin/wiki/_staging/xr-toolkit-unity-api-0dbdce37-0a9e-427b-af6b-2c8-c1bda4a2d47c.md
  - /home/admin/wiki/_staging/xrit-11-2-695f75da-8308-8323-8945-3f494c25f442-2-f20818f2fbc4.md
  - /home/admin/wiki/_staging/unity-xr-sdk-6d01bdd5-def1-4d3d-a287-a57a9538283-3a20f88a94bc.md
  - /home/admin/wiki/_staging/ar-67ea3adb-30f8-800d-a476-27083989ed9f-20250331-8987496eb4ca.md
  - /home/admin/wiki/_staging/ar-6981b41b-e01c-83a5-8e66-8ff03d887527-20260203-ee860168c87c.md
  - /home/admin/wiki/_staging/static-hand-gesture-696352e0-8ce8-8321-8d30-3236-0699385fe089.md
---

# XR/VR/AR Development

XR（Extended Reality）开发涵盖 VR、AR、MR 技术，涉及 OpenXR 运行时、交互工具包、手势识别等领域。本页汇总个人 XR 开发经验与技术要点。

## OpenXR 运行时

### Monado OpenXR
Monado 是开源 OpenXR 运行时，提供统一的 XR 设备接口。

**解决的核心问题**：
1. **跨设备兼容性**：一次开发，兼容 Oculus、HTC Vive、Pico 等多种硬件
2. **降低开发成本**：无需为每种设备编写特定驱动
3. **标准化接口**：遵循 OpenXR 规范，保证 API 一致性

**工作原理**：
- 提供统一的 OpenXR API 层
- 底层适配不同设备的驱动和 SDK
- 运行时处理设备发现、追踪、渲染等底层细节

**适用场景**：
- Linux 平台 XR 开发
- 开源项目和学术研究
- 多硬件兼容性需求

### SteamVR 2.x 开发（HTC VIVE）

SteamVR 2.x 是 Valve 的 VR 开发平台，主要用于 HTC VIVE 设备。

**核心组件**：
- **SteamVR Plugin**：Unity 插件，提供输入系统和追踪
- **SteamVR Input**：动作映射系统，支持手柄按钮、触摸板、扳机键
- **SteamVR_Render**：渲染管线管理

**输入处理示例**：
```csharp
// 侧键触发场景跳转
public SteamVR_Action_Boolean gripAction;

void Update()
{
    if (gripAction.GetStateDown(SteamVR_Input_Sources.RightHand))
    {
        SceneManager.LoadScene("TargetScene");
    }
}
```

**常见绑定**：
- 扳机键（Trigger）：选择、射击
- 侧键（Grip）：抓取、跳跃
- 菜单键（Menu）：暂停、设置
- 触摸板（Trackpad）：移动、导航

## Unity XR Interaction Toolkit (XRIT)

XRIT 是 Unity 官方的 XR 交互框架，提供标准化的交互组件。

### 核心架构
- **Interactor**：交互发起者（手部、控制器、射线）
- **Interactable**：可交互对象（可抓取、可按压）
- **InteractionManager**：管理所有交互的全局管理器
- **LocomotionProvider**：移动系统（传送、连续移动）

### 关键 API

**交互器类型**：
- `XRDirectInteractor`：直接接触交互
- `XRRayInteractor`：射线交互
- `XRGazeInteractor`：凝视交互

**可交互物体**：
- `XRGrabInteractable`：可抓取物体
- `XRSimpleInteractable`：简单交互（点击、悬停）
- `XRSocketInteractor`：插槽交互（物品放置）

**事件系统**：
```csharp
// 抓取事件监听
var grabInteractable = GetComponent<XRGrabInteractable>();
grabInteractable.selectEntered.AddListener(OnGrab);
grabInteractable.selectExited.AddListener(OnRelease);

void OnGrab(SelectEnterEventArgs args)
{
    Debug.Log("物体被抓取");
}

void OnRelease(SelectExitEventArgs args)
{
    Debug.Log("物体被释放");
}
```

### 版本演进

**XRIT 2.x**：
- 基础交互框架
- 支持 VR 和 AR
- 标准化输入系统

**XRIT 11.x**：
- 新增手势识别集成
- 物体组合交互
- 改进的 affordance 系统（视觉反馈）
- 性能优化和 Bug 修复

### 数据获取（XRIT 11.2）
从 XRIT 11.2 获取数据需关注：
- `XRInteractionManager` 的状态查询
- `XRBaseInteractor` 的选择状态
- `XRGrabInteractable` 的物理属性
- 网络同步时的数据可靠性（局域网 MQTT、TLS）

## AR 方案与手势识别

AR 博物馆方案商（云观博、Kivicube、Rokid 等）、Static Hand Gesture 手势识别（含黏手 Bug 修复）、ComfyUI AR 分析工作流等内容已拆分至独立页面：

→ [[ar-museum-solutions]]

## 跨页面参考

- [[ar-museum-solutions]] — AR 博物馆方案、手势识别、ComfyUI AR 工作流
- [[unity-development-core]] — Unity 开发基础，XRIT 在 Unity 中的应用
- [[indoor-navigation-positioning]] — 室内定位技术，可用于 AR 导航
