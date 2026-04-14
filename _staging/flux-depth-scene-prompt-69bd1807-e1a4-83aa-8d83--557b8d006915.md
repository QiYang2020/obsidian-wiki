---
title: Flux Depth Scene Prompt
source_id: flux-depth-scene-prompt-69bd1807-e1a4-83aa-8d83--557b8d006915
source_rel_path: raw/inbox/chatgpt_personal_backup_2026-04-10_1813_full_with_projects/Flux Depth Scene Prompt_69bd1807-e1a4-83aa-8d83-8bcf2103ac8d_20260320_174934.md
status: staged
---

# Flux Depth Scene Prompt

## Staging Digest
# Flux Depth Scene Prompt

## Initial user need
给一段用各种专业术语描绘场景风格的英文提示词。不要出现具体事物。要求色彩艳丽，真实风格。
要用于flux depth工作流的生图引导。

## Latest user clarification
mat1 and mat2 shapes cannot be multiplied (131072x64 and 128x3072)


TIPS: If you have any "Load CLIP" or "*CLIP Loader" nodes in your workflow connected to this sampler node make sure the correct file(s) and type is selected.

分析报错

## Latest assistant answer
这个报错本质上是一个**矩阵维度不匹配（shape mismatch）**问题，我们拆开来看：


## 🧠 一、报错核心含义

```
mat1 and mat2 shapes cannot be multiplied (131072x64 and 128x3072)
```

矩阵乘法要求：

> (A × B) · (C × D) → 必须满足 **B = C**

但现在是：

- mat1: **131072 × 64**
- mat2: **128 × 3072**

👉 中间维度 **64 ≠ 128 → 无法相乘 → 报错**


## 🔍 二、在 Flux / ComfyUI 中代表什么

这个错误**99% 出现在 CLIP / Text Encoder / Conditioning 阶段**，尤其是：

- 文本编码输出的 embedding 维度 ≠ 模型期望维度
- 或者 **模型和CLIP不匹配**


## ⚠️ 三

[... trimmed 1542 characters ...]

## Follow-up
- Expand this digest into a durable wiki page when the prompt budget is available.
- Preserve contradictions in `_meta/conflicts.md` if later sources disagree.
