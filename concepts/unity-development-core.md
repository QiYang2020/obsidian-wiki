---
title: Unity Development Core
created: 2026-04-11
updated: 2026-04-11
type: concept
tags:
  - unity
  - game-development
  - networking
  - xr
  - ai
sources:
  - /home/admin/wiki/_staging/unity-68de1fa2-85a4-8326-b5b5-5811519a51bb-20251-eeda12921ee7.md
  - /home/admin/wiki/_staging/unity-2118e300-47de-4d0b-bb84-298ac63f9420-20231-23af4ad2df90.md
  - /home/admin/wiki/_staging/unity-25fb8db7-f74a-42e1-8d9a-c325d4dd6b90-20230-2ff647d9da96.md
  - /home/admin/wiki/_staging/unity-35abee02-3e5c-41f4-bcfc-f7c4f9129e6d-20231-9a8447546383.md
  - /home/admin/wiki/_staging/unity-95e769c9-eb02-44a8-8acf-7e2ed65c7bbb-20231-2dec63dbd10b.md
  - /home/admin/wiki/_staging/unity-da8945a5-68e5-416e-ae9b-e25e896a041e-20231-1b364a94440e.md
  - /home/admin/wiki/_staging/unity-sentis-ai-integration-79ab7d2c-da97-4127-a-851e2e5522cf.md
  - /home/admin/wiki/_staging/unity-socket-help-f8c59fc7-5aea-4115-ab9b-c5f85a-2ccea5e983bd.md
  - /home/admin/wiki/_staging/unity-689484c4-c84c-832c-b391-168e5bb46760-20250-749cef434e5c.md
  - /home/admin/wiki/_staging/unity-68ef76e8-c260-8324-9bda-b6419f1351c8-20251-c9a5e47c12da.md
  - /home/admin/wiki/_staging/svn-6df28148-129c-41d2-8a43-c55eb581c16d-2024040-da0e11dd653f.md
  - /home/admin/wiki/_staging/unity-0730f595-e707-4050-ab4a-713ddd68d5aa-20231-8fb6066196c4.md
  - /home/admin/wiki/_staging/unity-97ab6e9c-360e-4d1f-b128-0bac8c2941e5-20240-05c343d94224.md
  - /home/admin/wiki/_staging/leantouch-677a27c6-d964-800d-972c-1f06509153a3-2-ffa3ccaf4d73.md
---

# Unity Development Core

Unity 知识领域涵盖渲染管线、动画状态机、编辑器工具、网络编程、XR SDK 等。本页汇总个人 Unity 开发中的关键工具、模式与经验。

## 知识领域概述

Unity 开发涉及多个专业领域：
- **渲染管线**：URP/Built-in/自定义管线，Shader Graph，光照与后处理
- **动画系统**：Animator Controller，状态机，Timeline，Cinemachine
- **编辑器扩展**：Editor Window，Custom Inspector，ScriptableObject 工具链
- **网络编程**：Socket、HTTP、MQTT、Photon PUN、Netcode for GameObjects
- **XR SDK**：Unity XR Interaction Toolkit，OpenXR 插件，AR Foundation
- **AI 集成**：Unity Sentis 推理引擎，ML-Agents，本地模型部署
- **性能优化**：内存分析，Draw Call 合批，Asset Bundle 策略

## 关键工具与插件

### LeanTouch
移动端触摸交互库，支持旋转、缩放、拖拽。
- `LeanTouchInteraction` 脚本实现单指旋转、双指缩放、拖拽灵敏度控制
- 常见需求：模型围绕世界 Y 轴旋转而非自转
- 事件过滤：结合 `EventSystem.IsPointerOverGameObject()` 避免 UI 穿透

### Mesh 变形与减面
- **Mesh Deformation**：顶点操作实现陶坯捏制效果，通过 `Mesh.vertices` 实时修改
- **Polyfew**：减面插件，原理为边坍缩（edge collapse）算法，需注意法线重建问题
- **绘制脚本**：基于 `Texture2D` 的像素级绘制，`Graphics.CopyTexture` 注意格式匹配与尺寸兼容

### UniTask
异步编程替代协程，支持 `async/await`：
```csharp
async Task DownloadConfig()
{
    var www = UnityWebRequest.Get("http://example.com/config.json");
    await www.SendWebRequest();
    if (www.isNetworkError || www.isHttpError)
        Debug.LogError(www.error);
    else
        ProcessConfig(www.downloadHandler.text);
}
```

### AVPro
视频播放插件，尤其在 WebGL 平台需处理自动播放限制（用户交互触发）。

## 网络编程模式

### Socket 基础
Unity 中的网络编程主要指：
1. **多人游戏**：客户端/服务器通信，实时对战
2. **数据同步**：玩家位置、游戏状态同步
3. **外部服务接入**：REST API、WebSocket、MQTT

### 常见模式
- **TCP/UDP Socket**：低延迟通信，需处理粘包、断线重连
- **Photon PUN**：云服务简化多人联机，`PhotonView` + `IPunObservable`
- **Netcode for GameObjects**：Unity 官方网络框架，适合中小型项目
- **MQTT**：物联网场景，轻量级发布/订阅模型

### 示例：XR 中的网络抓取
```csharp
[RequireComponent(typeof(PhotonView))]
[RequireComponent(typeof(XRGrabInteractable))]
public class NetworkedGrabbing : MonoBehaviourPunCallbacks, IPunObservable
{
    private XRGrabInteractable grabInteractable;
    
    public void OnPhotonSerializeView(PhotonStream stream, PhotonMessageInfo info)
    {
        if (stream.isWriting)
            stream.Send(grabInteractable.isSelected);
        else
            grabInteractable.isSelected = (bool)stream.ReceiveNext();
    }
}
```

## 项目结构规范

典型 Unity 项目目录结构：
```
Assets/
├── Scripts/          # 游戏逻辑脚本
├── Prefabs/          # 预制体
├── Materials/        # 材质球
├── Textures/         # 贴图
├── Animations/       # 动画文件
├── Plugins/          # 第三方插件
├── Editor/           # 编辑器扩展
├── Resources/        # 运行时加载资源
├── StreamingAssets/  # 流式资源
└── Scenes/           # 场景文件
```

SVN 版本控制时需忽略：
- `Library/`、`Temp/`、`obj/`、`Build/`、`Logs/`
- 配置 `.svnignore` 见 [[unity-svn-文件清理]]

## Unity XR Interaction Toolkit 基础

### 核心组件
- **XRBaseInteractor** / **XRBaseInteractable**：交互基础抽象类
- **XRGrabInteractable**：可抓取物体
- **XRDirectInteractor**：直接接触交互
- **XRController**：手柄输入映射
- **XRInteractorLineVisual**：射线可视化

### 常用 API
- `XRGrabInteractable.selectEntered`：抓取开始事件
- `XRBaseInteractor.isSelectActive`：交互器激活状态
- `XRInteractionManager`：全局交互管理器

### 版本差异
- XRIT 2.x：基础交互框架，支持 VR/AR
- XRIT 11.x：新增手势识别、物体组合交互、改进的 affordance 系统
- 详细数据获取见 [[xr-vr-ar-development]]

## Unity Sentis AI 集成

Sentis 是 Unity 的本地 AI 推理引擎，支持 ONNX 模型导入。

### 核心流程
1. **模型导入**：将 ONNX 模型拖入 Unity 项目
2. **运行时推理**：通过 `Worker` 执行模型前向传播
3. **输入输出**：将游戏数据转换为模型张量格式

### 应用场景
- 实时图像识别（物体检测、手势识别）
- 文本分类与情感分析
- 游戏 AI 决策（如棋类游戏评估）

### 示例：棋类 AI
```csharp
void ComputerMove()
{
    // 1. 翻转棋盘状态（从电脑视角）
    var flippedBoard = FlipBoard(currentBoard);
    
    // 2. 转换为模型输入张量
    var inputTensor = new TensorFloat(new TensorShape(1, 8, 8, 12), boardData);
    
    // 3. 执行推理
    worker.Schedule(inputTensor);
    var outputTensor = worker.PeekOutput() as TensorFloat;
    
    // 4. 解析最佳走法
    var bestMove = ParseBestMove(outputTensor);
    ApplyMove(bestMove);
}
```

## 跨页面参考

- [[xr-vr-ar-development]] — XR/VR/AR 开发详解，OpenXR 运行时，手势识别
- [[webgl-development]] — Unity WebGL 构建与部署，AVPro 视频播放策略
- [[ue5-development]] — UE5 蓝图与编辑器工具，可对比 Unity 编辑器扩展
