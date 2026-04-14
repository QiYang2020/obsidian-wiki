---
title: 学习XR interaction toolkit
source_id: xr-interaction-toolkit-e262835c-ab8e-429a-b8bf-2-a0998b492513
source_rel_path: raw/inbox/chatgpt_personal_backup_2026-04-10_night/学习XR interaction toolkit_e262835c-ab8e-429a-b8bf-279a6ce08d5b_20230918_140621.md
status: staged
---

# 学习XR interaction toolkit

## Staging Digest
# 学习XR interaction toolkit

## Initial user need
https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@2.3/manual/index.html
文档是全英文的，我需要中文的理解，用通俗易懂的解释，结合举例说明，帮助我理解学习XR interaction toolkit

## Latest user clarification
这个代码是不是把一些非活动状态的物体的render也算进去了？非活动状态的物体是不参与渲染的吧？那我不需要统计它们

## Latest assistant answer
您是对的。默认情况下，`Object.FindObjectsOfType<Renderer>()` 会返回所有的 `Renderer`，包括那些附属于非活动状态（Inactive）的 GameObjects 的 `Renderer`。如果您只想统计活动状态的 GameObjects 的材质球，我们需要稍作修改。

以下是修改后的代码，它只会统计活动状态的 GameObjects 的材质球：

```csharp
using UnityEngine;
using UnityEditor;
using System.Collections.Generic;

public class MaterialCountTool
{
    [MenuItem("Tools/Count Unique Materials")]
    private static void CountUniqueMaterials()
    {
        // 使用 HashSet 来存储唯一的材质球
        HashSet<Material> uniqueMaterials = new HashSet<Material>();

        //

[... trimmed 705 characters ...]

## Follow-up
- Expand this digest into a durable wiki page when the prompt budget is available.
- Preserve contradictions in `_meta/conflicts.md` if later sources disagree.
