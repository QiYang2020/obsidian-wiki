---
title: VRDragon 船体运动与调参系统
created: 2026-05-28
updated: 2026-05-28
type: concept
tags: [Unity, 船体运动, 划桨, NPC, 调参, Mirror]
sources:
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Docs/VR龙舟多人竞技_技术文档.md
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Docs/Scene_VRMatchSix_GameLogic.md
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Assets/DragonBoat/Scripts/Server/DragonBoatController.cs
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Assets/DragonBoat/Scripts/Server/ServerBoatMotionTuningRuntime.cs
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Assets/DragonBoat/Scripts/Client/PaddleHitDetector.cs
---

# VRDragon 船体运动与调参系统

该系统负责检测玩家划桨、统一驱动玩家船与 NPC 船的推进、限制船速与赛道方向，并通过服务端运行时面板即时调整运动手感。

## 系统组成

### 1. 划桨输入检测
**主要文件**: `PaddleHitDetector.cs`

**作用**:
- 检测船桨进入 `Water` 标签碰撞体
- 对本地划桨设置 `0.35s` 冷却
- 本地触水后发起 `CmdSpawnWaterSplash()` 与 `CmdPaddlePush()`

**限制条件**:
- 只有本地玩家对象处理输入
- 服务端只有在 `raceStarted` 且玩家状态为 `Racing` 时才接受推进请求

### 2. 船体推进核心
**主要文件**: `DragonBoatController.cs`

**统一入口**:
```text
DragonBoatController.QueueStroke(strokeQuality)
```

**推进模型**:
- 玩家划桨质量固定为 `1.0`
- NPC 根据运行时配置按频率循环提交随机桨力
- 实际推进在 `FixedUpdate()` 中统一以 `ForceMode.Impulse` 施加
- 推进方向取 `-transform.forward` 的水平投影
- 船体速度限制在赛道方向，角速度会被清零
- 滑行手感通过 Rigidbody `drag` 与冲量参数联合控制

### 3. NPC 自动划桨
**主要文件**: `MatchGameController.cs`, `DragonBoatController.cs`

**行为特征**:
- 未被玩家占用的船保持 `IsNPC == true`
- 倒计时结束后启动 NPC 划桨循环
- NPC 桨频、最小/最大桨力都来自服务端运行时参数
- 因为玩家与 NPC 共享推进模型，所以现场调参会同时影响两类船体

## 服务端运行时调参

### 1. 运行时面板
**主要文件**: `ServerBoatMotionTuningRuntime.cs`

**特点**:
- 仅服务端角色启用
- `M` 键显示/隐藏 `ServerMotionTuningCanvas`
- 可即时应用到 `MatchGameController` 与 4 条船
- 客户端与 Android 端不读取这些参数，也不展示该面板

### 2. 配置文件
```text
Application.persistentDataPath/DragonBoat/BoatMotionTuning.json
```

首次启动若 JSON 不存在，会从 `BoatMotionTuning_Default.asset` 生成默认值并落盘。

### 3. 面板操作
- **应用**：立即应用当前输入，不写文件
- **保存**：应用并写入 `BoatMotionTuning.json`
- **重载**：重新读取 JSON 并应用
- **恢复默认**：从默认资产恢复，再写入 JSON
- **保存名称 / 重载名称**：操作 `BoatPlayerNames.json`

### 4. 关键参数
- `coastDrag`
- `strokeImpulse`
- `minStrokeInterval`
- `maxForwardSpeed`
- 低速补偿开关 / 完整补偿速度 / 淡出速度 / 补偿倍率
- NPC 桨频
- NPC 桨力下限 / 上限

## 数据流

```text
玩家桨触水
  -> PaddleHitDetector 本地检测
  -> CmdPaddlePush()
  -> 服务端校验比赛状态
  -> DragonBoatController.QueueStroke(1.0)
  -> FixedUpdate() 施加推进冲量

NPC 自动循环
  -> MatchGameController 定时触发
  -> DragonBoatController.QueueStroke(randomQuality)
  -> FixedUpdate() 施加推进冲量
```

## 连续比赛复位

下一局开始前，系统会：
- 恢复船体初始位置、旋转、速度、角速度和刚体参数
- 取消旧的完赛停止协程
- 清空历史划桨请求
- 把船重新置为 NPC
- 再次应用当前 `BoatMotionTuning.json` 中的运行时参数

这使得“上一局改过的手感”可以延续到下一局，而不会因为场景复位丢失。

## 验证重点

1. 玩家触水后船体只在比赛中被推进
2. NPC 船能在无玩家占用时正常自动参赛
3. 修改 `coastDrag` / `strokeImpulse` 后立即可观察到手感变化
4. 连续两局之间，船体位置和状态能复位，但当前调参仍然保持生效
5. 船速被限制在赛道方向，不出现异常横漂或持续旋转

## 相关页面

- [[vrdragon-multiplayer-unity-project]] — 项目总览
- [[vrdragon-network-and-matchflow-system]] — 网络启动与比赛状态机
- [[vrdragon-results-and-ops-system]] — 冲线结果、排行榜与现场运营
