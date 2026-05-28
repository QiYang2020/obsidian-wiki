---
title: VRDragon 结果展示与现场运营系统
created: 2026-05-28
updated: 2026-05-28
type: concept
tags: [Unity, 排行榜, 结果保存, 运营, 观赛相机, 音效特效]
sources:
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Docs/VR龙舟多人竞技_技术文档.md
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Docs/Scene_VRMatchSix_GameLogic.md
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Assets/DragonBoat/Scripts/Server/FinishLineTrigger.cs
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Assets/DragonBoat/Scripts/Server/JsonResultUtility.cs
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Assets/DragonBoat/Scripts/Server/RaceRankingUIManager.cs
  - /home/admin/wiki/raw/assets/VRDragon_Multiplayer/Assets/DragonBoat/Scripts/Server/RaceArtSyncManager.cs
---

# VRDragon 结果展示与现场运营系统

该系统覆盖比赛冲线判定、成绩 JSON 保存、排行榜刷新、服务端看板、观赛相机切换、完赛气氛与强制复位，是 VRDragon_Multiplayer 面向线下运营的关键支撑层。

## 系统组成

### 1. 冲线与完赛判定
**主要文件**: `FinishLineTrigger.cs`, `MatchGameController.cs`

**规则**:
- 终点触发器只在服务端记录结果
- `finishedBoats` 防止同一条船重复记分
- 首船冲线只记录成绩和触发表现，不自动提前结束整局
- 只有 4 条船全部冲线后，才进入完整赛后窗口

### 2. 成绩保存
**主要文件**: `JsonResultUtility.cs`

**保存路径**:
```text
Application.persistentDataPath/RaceResults/{yyyyMMdd_HHmmss}.json
```

**固定字段**:
- `match name`: `AutoMatch_{timestamp}`
- `game name`: `AutoRace`

**命名规则**:
- 玩家船优先使用当前船位名称
- 若船位名为空，则回退到客户端 `displayName/playerID`
- NPC 船写为 `NPC_1` ~ `NPC_4`

### 3. 排行榜展示
**主要文件**: `RaceRankingUIManager.cs`

**当前主流程**:
- 全船冲线后调用 `ShowLatestGameRankingPanel()`
- `Q` 强制复位后也展示最近一场已保存成绩
- 总榜逻辑仍存在，但会过滤 NPC 成绩

### 4. 服务端运营看板
**主要文件**: `ServerRaceDashboard`（场景绑定）

**展示内容**:
- 比赛阶段
- 在线/上船/准备人数
- 自愿返回窗口倒计时（10 秒）
- 强制返回等待倒计时（30 秒）
- 4 条船状态
- 本场排名

**操作方式**:
- `M` 键显示/隐藏 `AutoRaceDashboard`
- 与 `ServerMotionTuningCanvas` 一起由服务端控制

### 5. 观赛相机切换
**主要文件**: `ServerCameraDirector`（场景绑定）

**切换规则**:
```text
等待 / 倒计时            -> ServerGuideCamera
比赛开始至首船冲线前      -> Pano_Camera 跟踪领先船
首船冲线后未全员完赛      -> ServerGuideCamera
全船冲线后短暂展示结果    -> FinishCamera
开放返回窗口或 Q 强制复位 -> RankingCamera
下一局首个玩家上船        -> 回到导览等待视角
```

### 6. 艺术与气氛同步
**主要文件**: `RaceArtSyncManager.cs`

**负责内容**:
- 倒计时音效与鼓点同步
- 终点对象显示/隐藏
- 完赛加油音效、结束音效、特效
- 船员 `WIN/LOSE/EndGame` 动画同步
- 下一局前统一清理动画 trigger 并恢复初始状态

## 赛后窗口与强制复位

### 1. 全船冲线后
- 停止比赛并进入 `postRaceActive`
- 保存结果 JSON
- 刷新最新一场排行榜
- 玩家进入 `PostRaceLocked`
- 10 秒后开放 `PostRaceReturnAllowed`
- 30 秒后强制在线玩家回等待

### 2. `Q` 强制复位
用于有船长时间未冲线时的人工干预：
- 所有在线玩家直接回等待
- 船体、NPC、终点、相机、艺术效果复位
- 排行榜继续显示最近一场已完成成绩
- 镜头停留在 `RankingCamera`，直到下一位玩家上船

## 数据流

```text
FinishLineTrigger
  -> MatchGameController.OnBoatReachedFinish()
  -> 记录每条船名次与成绩
  -> 全船完赛后 JsonResultUtility 落盘
  -> RaceRankingUIManager 刷新最新一场排行榜
  -> RaceArtSyncManager / ServerCameraDirector 推进赛后演出
  -> 10s/30s 回流窗口控制下一局衔接
```

## 验证重点

1. 首船冲线不会提前结束整局，4 条船都需记成绩
2. 全船冲线后会生成新的结果 JSON 文件
3. 排行榜展示的是最近一场结果，强制复位后仍可继续展示
4. `M` 可稳定切换服务端看板与调参面板
5. 相机能按比赛阶段在 Guide / Pano / Finish / Ranking 间切换
6. 下一局开始前音效、特效、终点对象和动画状态都能正确清理

## 相关页面

- [[vrdragon-multiplayer-unity-project]] — 项目总览
- [[vrdragon-network-and-matchflow-system]] — 网络与比赛状态机
- [[vrdragon-boat-motion-system]] — 划桨推进与运行时调参
