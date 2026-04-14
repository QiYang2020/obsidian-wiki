---
title: AIGuidedTourStory
created: 2026-04-11
updated: 2026-04-11
type: entity
tags: [gradio, ai-storytelling, museum, pipeline, python, openai-compatible]
sources:
  - /home/admin/wiki/raw/inbox/AIGuidedTourStory/
---

# AIGuidedTourStory

## 概述

AI Guided Tour Story 是一个面向博物馆/展览场景的 AI 导览故事生成工具。用户输入展品清单（Excel 表格或 JSON），系统通过 5 阶段技能管线自动输出趣味导览文案、主线故事和每件展品的趣味介绍终版。

当前冻结版本为 `stage-0.1`，设计为局域网部署的 [[gradio]] Web 应用。

## 技术栈

- **Python** — 主运行时
- **Gradio** — Web UI 框架，提供多标签页入口（JSON 一键模式 / 简洁模式 / 专家模式 / Responses API 管理）
- **pandas** — 表格数据清洗与阶段结果整理
- **openpyxl** — Excel 模板创建、工作簿复制与多工作表写出
- **openai SDK** — 优先使用 `client.responses` 接口；不支持时自动回退到 `requests` HTTP 调用
- **requests** — Responses API 的 HTTP fallback

## 架构

```
app.py (Gradio 入口)
  ├── story_pipeline.py (StorySkillPipeline)
  │     ├── Skill 01: 故事类型与风格判断
  │     ├── Skill 02: 丰富展品书面介绍
  │     ├── Skill 03: 趣味介绍初版
  │     ├── Skill 04: 主线故事生成
  │     └── Skill 05: 趣味介绍终版
  └── providers/
        ├── OpenAICompatibleResponsesClient
        ├── ResponsesProviderConfig
        └── tool resolution (web_search, web_extractor, code_interpreter)
```

模型接入统一走 OpenAI-compatible Responses 协议，`provider / base_url / model / api_key` 均可替换，不绑定单一厂商。内置预设包含 Qwen Responses API（DashScope）。

## 五阶段技能管线

| 阶段 | 技能 | 功能 |
|------|------|------|
| 01 | 故事类型与风格判断 | 根据用户初始文本判断故事类型（悬疑/儿童/史诗/通用），生成 StoryStyleProfile |
| 02 | 丰富展品书面介绍 | 结合馆方简介与网络检索，补全时代、用途、人物、材料等资料卡 |
| 03 | 趣味介绍初版 | 将客观简介改写为"从局部到整体"的趣味导览初版文案 |
| 04 | 主线故事生成 | 按展品顺序将单件介绍串成连续可听的导览主线 |
| 05 | 趣味介绍终版 | 识别主线承接关系，为每件展品生成业务最终趣味介绍 |

每阶段可独立触发，支持断点续跑。Skill 02 支持 `web_search` / `web_extractor` / `code_interpreter` 工具透传（是否生效取决于 provider 响应）。

## 输入输出

**输入方式：**
- 表格模式：读取 `input/` 下 `.xlsx` / `.csv`，最小必填列 `展品名称`
- JSON 一键模式：读取 `input/Json/*.json`，消费 `activity.name`、`tourPoints[].name`、`tourPoints[].artworkDescription`

**输出：**
- Excel 工作簿（首个 sheet 为业务最终输出，后续 sheet 记录阶段结果）
- 表格模式额外输出 `.json` sidecar

## 关键目录

- `app.py` — Gradio UI 组装与事件绑定
- `story_pipeline.py` — 核心管线与 5 阶段技能实现
- `providers/` — OpenAI-compatible Responses 调用层与工具透传
- `app_versions/stage-0.1/skills/` — 当前冻结版本的技能文档
- `input/` — 表格/JSON 输入源
- `output/` — 结果文件输出
- `data/` — 本地配置、缓存与 API 状态

## 当前状态

- 版本：`stage-0.1`（冻结）
- 开发阶段：核心管线与多模式 UI 已完成，支持本地规则 fallback 和 LLM Responses 增强
- 已知边界：JSON 模式搜索补全结果不回写原始文件；provider 不可用时联网步骤被拦截
- 业务流程图：`docs/business_flow.markmap.md`、`docs/simple_mode_manual.markmap.md`

## 交叉引用

- [[ai-image-generation]] — 同属 AI 生成类工具链，AIGuidedTourStory 专注文本叙事而非图像
- [[ar-museum-solutions]] — 博物馆场景关联，AIGuidedTourStory 生成导览文案，AR 方案提供交互呈现
- [[technical-documentation]] — 项目文档结构可参考技术文档写作规范
