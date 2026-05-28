---
title: VRDragon 网络与比赛流程系统
created: 2026-05-28
updated: 2026-05-28
type: concept
tags: [Unity, Mirror, 网络同步, 比赛状态机, Pico, VR]
sources:
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Docs/VR龙舟多人竞技_技术文档.md
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Docs/Scene_VRMatchSix_GameLogic.md
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Assets/DragonBoat/Scripts/Server/
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Assets/DragonBoat/Scripts/Client/PlayerNetworkController.cs
---

# VRDragon 网络与比赛流程系统

该系统负责 VRDragon_Multiplayer 的联机角色选择、客户端连接、玩家状态同步、上船分配、准备/开赛状态机，以及赛后返回等待的完整自动赛流程。

## 系统组成

### 1. 网络启动入口
**主要文件**: `DragonBoatNetworkLauncher.cs`, `CustomNetworkManager.cs`, `PlayerConnectionManager.cs`

**核心职责**:
- 根据运行环境自动调用 `StartServer()` 或 `StartClient()`
- 区分原工程 Editor 与 ParrelSync 克隆 Editor
- 维护单场景联机，不依赖 Mirror 默认的 offline/online scene 切换
- 玩家断线时释放船位、ready 状态，并在无人在线时复位比赛状态

**启动角色规则**:
```text
原工程 Unity Editor    -> Server
ParrelSync 克隆 Editor -> Client
Windows Player         -> Server
Android Player         -> Client
```

### 2. 客户端连接与重连
**地址来源**:
- ParrelSync Editor Client: `editorClientAddress`，默认 `localhost`
- Android Client: `Application.persistentDataPath/serverip.txt`
- Android 默认 IP: `192.168.10.56`

**重连机制**:
- `clientAutoReconnect` 控制自动重连开关
- 固定间隔重新读取地址并尝试连接
- 服务端晚于客户端启动时，客户端会持续轮询直到成功连接

### 3. 玩家状态机
**主要文件**: `PlayerNetworkController.cs`

**状态定义**:
```text
Waiting
Boarded
Ready
Racing
PostRaceLocked
PostRaceReturnAllowed
```

**SyncVar 关注点**:
- `displayName`
- `playerID`
- `assignedBoatIndex`
- `readyForRace`
- `raceState`
- `statusMessage`
- `paddleSide`

### 4. trigger 输入映射
**输入源**:
- PICO 左右手 `ActionBasedController.activateAction`
- Editor 测试键：`R`
- 触发阈值：`ReadValue<float>() > 0.75`

**边沿触发流程**:
```text
Waiting                -> CmdRequestBoardBoat()
Boarded / Ready        -> CmdToggleReadyForRace()
PostRaceReturnAllowed  -> CmdRequestReturnToWaiting()
```

系统只在本地玩家对象上做边沿检测，避免长按 trigger 连续跳过多个阶段。

## 自动比赛流程

### 1. 上船分配
**主要文件**: `MatchSceneController.cs`

**规则**:
- 玩家连接后默认停留在 `Waiting`
- 只有玩家显式 trigger 才会上船
- 服务端按 `boatSpawnPoints[0..3]` 顺序寻找第一条 `IsNPC == true` 的空船
- 成功上船后进入 `Boarded`
- 第 5 位在线玩家保持等待，不掉线
- 比赛倒计时、比赛中、结果阶段都拒绝新的上船请求

**座位选择**:
```text
优先 RightSeats/PlayerSeat
否则 RightSeats 第一个可用座位
再退回 LeftSeats 命名座位或第一个可用座位
```

### 2. 准备与开赛
**主要文件**: `MatchGameController.cs`

**开赛逻辑**:
- 只统计已上船玩家，不统计仍在等待态的在线玩家
- 无玩家上船时不会自动开赛
- 所有已上船玩家 ready 后启动 4 秒倒计时
- 倒计时结束后把已上船玩家切到 `Racing`
- 未被占用的船继续以 NPC 形式参赛

### 3. 赛后回流
**赛后窗口**:
- 全船冲线后玩家进入 `PostRaceLocked`
- 10 秒后切到 `PostRaceReturnAllowed`，可主动 trigger 回等待
- 30 秒后强制所有在线玩家回等待
- 下一位玩家再次上船时重新进入下一局流程

## 船位名称与玩家显示名

**名称配置文件**:
```text
Application.persistentDataPath/DragonBoat/BoatPlayerNames.json
```

**规则**:
- 4 个输入框对应 1~4 号船位
- 名字代表船位/角色，不一定等于设备持有人
- 空名回退到客户端 `displayName/playerID`
- 名称在成功上船时写入玩家显示名、船体归属和成绩记录

## 数据流

```text
本地 trigger 边沿
  -> PlayerNetworkController 发起 Command
  -> MatchSceneController 分配船位/回等待
  -> MatchGameController 检查 ready 并推进比赛阶段
  -> SyncVar / TargetRpc 同步玩家状态、座位与提示信息
  -> 赛后窗口开放或强制回流
```

## 验证重点

1. 原工程 Editor Play 自动起服务端，ParrelSync 克隆工程自动起客户端
2. 客户端进入后默认 Waiting；第一次 trigger 上船，第二次 trigger 准备
3. 等待态在线玩家不阻塞开赛；第 5 个玩家保持等待但不掉线
4. 服务端断线或玩家断线后，船位与 ready 状态可释放
5. 全船冲线后 10 秒开放自愿返回，30 秒强制回等待

## 相关页面

- [[vrdragon-multiplayer-unity-project]] — 项目总览
- [[vrdragon-boat-motion-system]] — 划桨推进与船体运动
- [[vrdragon-results-and-ops-system]] — 结果保存、排行榜与服务端运营
