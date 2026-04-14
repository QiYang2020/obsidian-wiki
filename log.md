# Wiki Log

## [2026-04-10] create | Wiki initialized
- Initialized base structure for llm-wiki skill

## [2026-04-11] update | Personal knowledge schema bootstrap
- Tailored `SCHEMA.md` for personal long-term knowledge ingestion
- Added `_meta/topic-map.md` and `_meta/conflicts.md`
- Updated `index.md` to expose meta navigation pages

## [2026-04-11] ingest | CUDA安装与路径管理
- Source: `raw/inbox/chatgpt_personal_backup_2026-04-10_md/CUDA安装与路径管理_69bb58e4-28f4-83ab-8fa9-54fc1ab04014_20260319_100209.md`
- Created: `concepts/cuda-toolkit-安装与路径管理.md`
- Content: CUDA Toolkit 非系统盘安装、环境变量配置、多版本共存、迁移流程

## [2026-04-11] ingest | Unity SVN 文件清理
- Source: `raw/inbox/chatgpt_personal_backup_2026-04-10_md/Unity/Unity SVN 文件清理_67ea5661-34cc-800d-9b12-fd828c573227_20250331_164625.md`
- Created: `concepts/unity-svn-文件清理.md`
- Content: Unity 工程上传 SVN 时可忽略的文件夹（Library/Temp/obj/Build/Logs）及 .svnignore 配置建议

## [2026-04-11] lint | Index hygiene & broken link triage
- Added `adb-multi-device-management` to `index.md`, updated page count to 8
- Updated `topic-map.md` with Android/MR/XR and CUDA theme sections
- Documented broken wikilinks (`pytorch`, `environment-variable-management`) in `conflicts.md` — pages not yet created

## [2026-04-11] lint | Deterministic wiki hygiene
- Updated: `_meta/conflicts.md`
- Notes: tracked 5 broken wikilink reference(s) in conflicts

## [2026-04-11] lint | Deterministic wiki hygiene
- Updated: `_meta/conflicts.md`
- Notes: tracked 9 broken wikilink reference(s) in conflicts

## [2026-04-11] lint | Deterministic wiki hygiene
- Updated: `_meta/conflicts.md`
- Notes: tracked 3 broken wikilink reference(s) in conflicts

## [2026-04-11] ingest | UE5 Development cluster
- Sources: 7 staging files (Activate UE5 Naming Validator, UE5蓝图交互制作, UE5自定义编辑器工具 x2, 导入外部内容文件 x2, Electra循环播放问题)
- Created: `concepts/ue5-development.md`
- Content: Blueprint interaction, naming validator, Editor Utility tools (EUC/EUA), Datasmith import with UV2, Electra looping via Seek detection

## [2026-04-11] ingest | WebGL Development cluster
- Sources: 5 staging files (HTML页面积木渲染, WebGL画面适配, 大蜡丸 WebGL项目逻辑理解, WebGL开发文档要点, 广陈皮 WebGL)
- Created: `concepts/webgl-development.md`
- Content: Unity WebGL stack (URP/AVPro/Shader), HTML container layout, 3D interaction flow management, brick rendering, IIS deployment docs

## [2026-04-11] ingest | AI Image Generation cluster
- Sources: 7 staging files (简单生图方案, 数字人AI技术方案, ComfyUI UNET VAE CLIP, 锐评FaceFusion竞品分析, Flux Depth Scene Prompt, 风格提案, 戏台背景图需求)
- Created: `concepts/ai-image-generation.md`
- Content: ComfyUI workflow (UNET/CLIP/VAE), Flux Depth prompting, FaceFusion analysis, digital human for museum, style proposals

## [2026-04-11] ingest | Indoor Navigation & Positioning cluster
- Sources: 4 staging files (智能语音定位设备, 室内导览需求与技术, 室内导览定位技术对比, 蓝牙信标安装评估)
- Created: `concepts/indoor-navigation-positioning.md`
- Content: BLE Beacon vs WiFi RTT vs UWB vs visual SLAM comparison, 1000-unit cost budget, smart voice device specs

## [2026-04-11] ingest | 3D Photogrammetry cluster
- Sources: 3 staging files (倾斜摄影, 照片墙应用实时更新, 转换ply为spz)
- Created: `concepts/3d-photogrammetry.md`
- Content: Oblique photography output formats, PLY→SPZ conversion with gsbox, Unity photo wall real-time updates

## [2026-04-11] ingest | Technical Documentation cluster
- Sources: 3 staging files (技术交底书构成模块, 操作手册结构整理, 流程图大纲生成)
- Created: `concepts/technical-documentation.md`
- Content: Patent disclosure module structure, operation manual writing principles, flowchart outline generation

## [2026-04-11] update | Index and topic map for 6 new clusters
- Updated: `index.md` — page count 8→14, added 6 concept entries (alphabetical)
- Updated: `_meta/topic-map.md` — 6 new theme sections (UE5, WebGL, AI Image Gen, Indoor Nav, 3D Photogrammetry, Tech Docs)

## [2026-04-11] ingest | Unity Development Core and XR/VR/AR Development clusters
- Sources: 14 Unity staging files, 9 XR/VR/AR staging files
- Created: `concepts/unity-development-core.md`, `concepts/xr-vr-ar-development.md`
- Content: Unity knowledge domains, LeanTouch/Polyfew/UniTask, socket networking, project structure, XRIT basics, Sentis AI; OpenXR runtime, SteamVR 2.x, XRIT API, hand gesture recognition, AR museum solutions
- Updated: `index.md` — page count 14→16, added 2 concept entries
- Updated: `_meta/topic-map.md` — added XR/VR/AR and Unity Development Core sections

## [2026-04-11] ingest | 杂项开发笔记（剩余 18 个 staging 文件汇总）
- Sources: 10 个有知识价值的 staging 文件（Shader 原理、PlayCanvas→glTF、无限滚动、场景状态机、UI 相机、旋转修正、科技热点、智慧农业、龙舟课程、VE 比赛流程）
- Created: `concepts/misc-development-notes.md`
- 跳过（不单独建页）: 问题4 (x2, 重复基础问题)、创造者与技术探索者 (个人画像)、绘图和图像处理功能、捕获错误解决、无法访问链接、模型JSON处理、Somalia Trade History (翻译任务)
- 所有 71 个 staging 文件已处理完成

## [2026-04-11] stub | 创建断链 stub 页面
- Created: `concepts/environment-variable-management.md`, `concepts/pytorch.md`
- 解决 conflicts.md 中记录的 2 个 broken wikilinks
- Updated: `index.md` (page count 17→19), `conflicts.md` (cleared open items)

## [2026-04-11] archive | 归档已处理 staging 文件
- Moved: 71 个文件从 `_staging/` → `_staging/_processed/`

## [2026-04-11] split | 拆分 xr-vr-ar-development 页面
- Created: `concepts/ar-museum-solutions.md`（AR 博物馆方案、手势识别、ComfyUI AR 工作流）
- Trimmed: `concepts/xr-vr-ar-development.md`（210→~170 行）
- Updated: `index.md` (page count 19→20)

## [2026-04-11] git | 初始化 Git 仓库并推送到 GitHub
- Remote: https://github.com/QiYang2020/obsidian-wiki
- Branch: main
- 包含: wiki 结构、15 个概念页、71 个已处理 staging 文件、raw inbox（AIGuidedTourStory/Qwen3TTS/HunyuanWorld-Mirror/facefusion/chatgpt backups）

## [2026-04-11] ingest | Qwen3TTS 项目
- Source: `raw/inbox/Qwen3TTS/` (README.md, ENGINEERING.md, scripts/, whisper_align_tool/)
- Created: `entities/qwen3tts.md`
- Content: Qwen3-TTS 本地语音合成 + Whisper 强制对齐 LRC 工具链，Windows+WSL 双层架构，Gradio WebUI，语音设计/克隆/批量/LRC 五合一
- Updated: `index.md` (page count 22→23)

## [2026-04-11] ingest | HunyuanWorld-Mirror 项目实体
- Source: `raw/inbox/HunyuanWorld-Mirror/deploy_user_docs/` (11 files)
- Created: `entities/hunyuanworld-mirror.md`
- Content: 腾讯混元前馈 3D 重建模型，多模态先验提示架构，同时输出点云/深度/法线/相机/3DGS，PyTorch + gsplat 技术栈
- Links: 3d-photogrammetry, ai-image-generation, pytorch

## [2026-04-11] ingest | FaceFusion 项目实体
- Source: `raw/inbox/facefusion/project_usage_runtime_pack/` (22 files)
- Created: `entities/facefusion.md`
- Content: 开源人脸操作平台，ONNX Runtime 多 provider 推理，face_swapper/enhancer 等处理器，Gradio UI + 作业管理系统
- Links: ai-image-generation, ar-museum-solutions, cuda-toolkit-安装与路径管理
- Updated: `index.md` (page count 20→22, added 2 entity entries)

## [2026-04-11] ingest | AIGuidedTourStory 项目分析
- Source: `raw/inbox/AIGuidedTourStory/`
- Created: `entities/aiguidedtourstory.md`
- Content: Gradio 博物馆导览故事生成应用，5 阶段技能管线（风格判断→丰富介绍→趣味初版→主线故事→终版输出），OpenAI-compatible Responses 协议接入
- Updated: `index.md` (page count 20→21, added Entities section)

## [2026-04-12] lint | Deterministic wiki hygiene
- Updated: `index.md`, `_meta/conflicts.md`
- Notes: tracked 2 broken wikilink reference(s) in conflicts; tracked 71 duplicate-name cluster(s) in conflicts

## [2026-04-13] lint | Deterministic wiki hygiene
- Updated: `index.md`, `_meta/conflicts.md`
- Notes: tracked 2 broken wikilink reference(s) in conflicts; tracked 71 duplicate-name cluster(s) in conflicts

## [2026-04-14] lint | Deterministic wiki hygiene
- Updated: `index.md`, `_meta/conflicts.md`
- Notes: tracked 2 broken wikilink reference(s) in conflicts; tracked 71 duplicate-name cluster(s) in conflicts

## [2026-04-14] ingest | PanoRendering UE5 项目系统
- Source: `raw/assets/UE5_PanoramiCamera/Content/Tools/`
- Created: 
  - `entities/panorendering-project.md` (主项目实体页)
  - `concepts/camera-point-system.md` (相机点管理系统)
  - `concepts/frame-blueprint-system.md` (画框蓝图系统)
  - `concepts/level-management-system.md` (展厅场景管理系统)
  - `concepts/sequence-automation-system.md` (序列自动化系统)
- Content: UE5.3 全景相机渲染系统，包含相机点管理、画框蓝图V1/V2、展厅场景管理、Python序列自动化脚本
- Updated: `index.md` (added 5 new pages), `_meta/topic-map.md` (added UE5开发 section)
- Systems: CameraPoint (17 components), Frame_Blueprint (9 components), Frame_BlueprintV2 (3 components), LEVEL (G04展厅), Sequence (Python自动化)

## [2026-04-14] ingest | MR Workshop Unity 项目交互系统
- Source: `raw/assets/MR_Workshop/Assets/MRInteraction/Script/`
- Created:
  - `entities/mr-workshop-unity-project.md` (主项目实体页)
  - `concepts/mr-workshop-hand-gesture-system.md` (手势交互系统)
  - `concepts/mr-workshop-zone-trigger-system.md` (区域触发系统)
  - `concepts/mr-workshop-gameplay-system.md` (游戏逻辑系统)
  - `concepts/mr-workshop-event-system.md` (事件通信系统)
- Content: Unity MR 交互项目，Pico 手势识别、区域计时触发、积木生成与计数、蓝图搭建系统
- Updated: `index.md` (176→181 pages), `_meta/topic-map.md` (added MR Workshop section)
- Systems: HandPoseGrabber (手势抓取), ZoneTrigger (区域触发), GrabSpawn (生成系统), TextCounterManager (计数管理), EventHandle (事件通信)

## [2026-04-14] compare | UE5 与 Unity MR 项目对比分析
- Source: `raw/assets/UE5_PanoramiCamera/`, `raw/assets/MR_Workshop/`
- Created: `comparisons/ue5-unity-mr-projects.md`
- Content: 对比两个 MR 项目的架构设计、交互系统、数据流、性能优化
- Updated: `index.md` (181→182 pages, added Comparisons section)

## [2026-04-14] ingest | GZUCM_VRVideo Unity 项目交互系统
- Source: `raw/assets/GZUCM_VRVideo/Assets/Scripts/`
- Created:
  - `entities/gzucm-vrvideo-unity-project.md` (主项目实体页)
  - `concepts/gzucm-vrvideo-media-system.md` (媒体展示系统)
  - `concepts/gzucm-vrvideo-teleport-system.md` (传送系统)
  - `concepts/gzucm-vrvideo-interaction-system.md` (交互系统)
  - `concepts/gzucm-vrvideo-ui-system.md` (UI 系统)
- Content: Unity VR 视频播放项目，Pico 平台支持，媒体展示、传送系统、交互式菜单、背景音乐控制
- Updated: `index.md` (182→187 pages), `_meta/topic-map.md` (added GZUCM VRVideo section)
- Systems: InteractableData (交互数据), CanvasController (媒体显示), TeleportManager (传送), GrabAttachReturn (抓取返回), MenuUI (菜单)
