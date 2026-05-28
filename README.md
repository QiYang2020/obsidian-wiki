# 个人知识库

这是一个持续更新的个人技术知识库，围绕 XR / VR / AR、Unity、UE5、AI 生成与平台项目整理技术要点、项目拆解与交叉关联文档。

## 内容结构

### 核心概念
- **UE5 开发**：全景相机渲染、蓝图系统、展厅场景管理、序列自动化
- **Unity 开发**：MR 交互、VR 视频播放、网络联机、WebGL 适配
- **XR / VR / AR**：交互框架、设备接入、空间计算、体验设计
- **AI / ML**：图像生成、语音合成、字幕对齐、3D 重建

### 文档目录
- `concepts/`：技术概念、系统拆解与方法总结
- `entities/`：具体项目、平台、工具或系统总览
- `comparisons/`：方案或项目之间的对比分析
- `_meta/`：导航页与知识组织辅助页面

## 项目介绍

1. **PanoRendering (UE5)**  
   全景相机渲染系统，涵盖 CameraPoint、Frame Blueprint、Level Management、Sequence Automation 等模块。

2. **MR_Workshop (Unity)**  
   面向 MR 交互场景的 Unity 项目，包含手势识别、区域触发、事件通信与游戏逻辑。

3. **GZUCM_VRVideo (Unity)**  
   VR 视频播放与交互项目，包含媒体展示、传送、UI 菜单与交互控制。

4. **VRDragon_Multiplayer (Unity)**  
   基于 Mirror + KcpTransport 的 VR 多人龙舟项目，涉及比赛流程、船体运动、结果展示与现场运营。

5. **AIGroupChat**  
   单活动 AI 群聊导览剧本系统，覆盖管理端读取、静态剧本生成与运行时回复。

6. **LightUP_AItourPoint_API**  
   面向讲解点内容生成的 API 链路，包含 speechText、instruction、ttsText、音频生成与 LRC 对齐。

## 技术亮点

### 架构设计
- 模块化系统拆分
- 数据驱动配置
- 事件解耦通信
- 多系统协作流程

### 交互与运行机制
- 手势识别与抓取交互
- 区域触发与状态控制
- 媒体播放与 UI 联动
- 语音、字幕与生成链路整合

## 文档内链接

- [[知识库索引]] — 知识库总入口
- [[主题图谱]] — 按主题聚合的重要导航页
- [[PanoRendering UE5项目]]
- [[MR_Workshop Unity项目]]
- [[GZUCM_VRVideo Unity项目]]
- [[VRDragon多人龙舟Unity项目]]
- [[AIGroupChat群聊导览剧本系统]]
- [[LightUP讲解点AI生成API]]

## 相关链接

- [Obsidian](https://obsidian.md/)
- [Unity XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.0/manual/index.html)
- [Unreal Engine Documentation](https://docs.unrealengine.com/)
