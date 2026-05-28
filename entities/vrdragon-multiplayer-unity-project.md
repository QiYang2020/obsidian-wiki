---
title: VRDragon Multiplayer Unity 项目
created: 2026-05-28
updated: 2026-05-28
type: entity
tags: [Unity, VR, 多人联机, Mirror, Pico, 龙舟]
sources:
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Docs/
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Assets/DragonBoat/Scripts/
---

# VRDragon Multiplayer Unity 项目

VRDragon_Multiplayer 是一个基于 Unity + Mirror 的 VR 龙舟多人竞速项目，主场景为 `Scene_VRMatchSix`。系统面向 Windows 服务端与 Android PICO 客户端，围绕“等待 → 上船 → 准备 → 自动开赛 → 划桨竞速 → 排行榜 → 连续下一局”的自动比赛流程构建。

## 项目概述

- **引擎/框架**: Unity、Mirror、KcpTransport
- **目标平台**: Windows 服务端、Android PICO 头显、ParrelSync Editor 测试客户端
- **主玩法**: 4 条龙舟自动赛；最多 4 名玩家上船，空船自动作为 NPC 参赛
- **核心交互**: trigger 上船、trigger 准备、划桨触水推进、赛后 trigger 返回等待
- **主要持久化**: 船体参数 JSON、船位名称 JSON、比赛结果 JSON

## 项目结构

```text
VRDragon_Multiplayer/
├── Assets/
│   ├── DragonBoat/
│   │   ├── Scenes/                 # 主场景 Scene_VRMatchSix
│   │   ├── Scripts/
│   │   │   ├── Client/             # 客户端输入、UI、座位同步、划桨检测
│   │   │   ├── Server/             # 比赛流程、船体控制、结果保存、运行时调参
│   │   │   └── Struct/             # 成绩结构体
│   │   ├── Resources/              # 龙头资源等运行时加载资源
│   │   └── Prefabs/                # 玩家、船体、UI 等预制体
│   ├── Mirror/                     # Mirror 联机框架
│   └── MirrorExamplesVR/           # VR 联机示例/参考资源
├── Docs/                           # 游戏逻辑、现场流程、技术文档
├── Packages/ ProjectSettings/      # Unity 工程配置
└── Temp/ obj/                      # 构建与缓存产物
```

## 核心系统架构

### 1. [[vrdragon-network-and-matchflow-system]]
- `DragonBoatNetworkLauncher`：按运行环境自动选择 Server/Client 角色
- `CustomNetworkManager`：维持单场景联机流程，处理断线后的状态释放
- `PlayerConnectionManager`：玩家连接注册与默认身份管理
- `MatchSceneController` / `MatchGameController`：上船分配、准备、倒计时、开赛、赛后回流

### 2. [[vrdragon-boat-motion-system]]
- `DragonBoatController`：统一处理玩家船与 NPC 船的推进模型
- `PaddleHitDetector`：检测船桨触水并上报划桨请求
- `ServerBoatMotionTuningRuntime`：服务端运行时调参、参数保存/恢复
- `BoatMotionTuning`：默认参数资产与 JSON 配置桥梁

### 3. [[vrdragon-results-and-ops-system]]
- `FinishLineTrigger`：服务端终点触发器
- `JsonResultUtility`：比赛成绩保存到 JSON
- `RaceRankingUIManager`：最新一场与总榜展示
- `ServerRaceDashboard` / `ServerCameraDirector` / `RaceArtSyncManager`：服务端看板、观赛镜头、完赛气氛与连续赛复位

## 自动比赛流程

```text
客户端进入 Waiting
  -> trigger 请求上船
  -> 服务端按 boatSpawnPoints 顺序分配空船
  -> 玩家进入 Boarded
  -> trigger 切换 Ready
  -> 所有已上船玩家 Ready
  -> 4 秒倒计时
  -> 比赛开始，玩家/NPC 共同划桨推进
  -> 4 条船分别冲线并记录成绩
  -> 全船冲线后保存结果 JSON 并展示排行榜
  -> 10 秒后允许玩家主动回等待
  -> 30 秒后强制在线玩家回等待
  -> 系统复位并等待下一局
```

## 技术特点

1. **环境感知启动**：原工程 Editor 自动起服务端，ParrelSync 克隆工程自动起客户端
2. **显式上船机制**：玩家连接后默认等待，只有主动 trigger 才会上船，不阻塞其他玩家开赛
3. **玩家/NPC 共用推进模型**：玩家划桨与 NPC 自动桨都统一进入 `DragonBoatController.QueueStroke()`
4. **服务端权威调参与裁决**：船速、冲量、阻尼、NPC 节奏和比赛阶段都由服务端决定
5. **连续比赛复位**：支持赛后窗口、自主返回、强制复位与下一局自动衔接
6. **现场运营友好**：服务端带运行看板、排行榜、船位名配置、运动参数面板与观赛相机

## 关键持久化文件

- `Application.persistentDataPath/DragonBoat/BoatMotionTuning.json`
- `Application.persistentDataPath/DragonBoat/BoatPlayerNames.json`
- `Application.persistentDataPath/RaceResults/{yyyyMMdd_HHmmss}.json`
- Android 客户端服务端地址：`Application.persistentDataPath/serverip.txt`

## 相关页面

- [[vrdragon-network-and-matchflow-system]] — 网络启动、上船分配、状态机与自动开赛流程
- [[vrdragon-boat-motion-system]] — 划桨检测、船体推进、NPC 运动与运行时调参
- [[vrdragon-results-and-ops-system]] — 冲线、成绩保存、排行榜、服务端运营 UI 与相机
- [[unity-development-core]] — Unity 开发核心
- [[xr-vr-ar-development]] — XR/VR/AR 开发
