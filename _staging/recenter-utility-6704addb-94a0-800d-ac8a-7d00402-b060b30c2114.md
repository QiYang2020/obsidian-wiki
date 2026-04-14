---
title: Recenter Utility 代码分析
source_id: recenter-utility-6704addb-94a0-800d-ac8a-7d00402-b060b30c2114
source_rel_path: raw/inbox/chatgpt_personal_backup_2026-04-10_md/Recenter Utility 代码分析_6704addb-94a0-800d-ac8a-7d00402e6ac9_20241008_115819.md
status: staged
---

# Recenter Utility 代码分析

## Staging Digest
# Recenter Utility 代码分析

## Initial user need
理解并分析下面的代码。
using EZXR.Glass.SixDof;
using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Wheels.Unity;

namespace EZXR.Glass.Runtime
{
    public static class RecenterUtility
    {
        public enum Space
        {
            /// <summary>
            /// 身体坐标系（人站立时胸口朝向的方向为z，重力反方向为y，身体

[... trimmed 6783 characters ...]

## Latest user clarification
阅读并理解下面代码，说说如何禁用右手的呼出系统菜单。
using EZXR.Glass.Runtime;
using EZXR.Glass.Inputs;
using EZXR.Glass.MiraCast;
using EZXR.Glass.Recording;
using EZXR.Glass.SixDof;
using System;
using System.Collections;
using UnityEngine;
#if USE_LOCALIZATION
using UnityEngine.Localization;
using UnityEngine.Localization.Settings;
#endif

namespace EZXR.Glass.Runtime
{
    [ScriptExecutionOrder(-3000)]

[... trimmed 14451 characters ...]

##

[... trimmed 415 characters ...]

## Follow-up
- Expand this digest into a durable wiki page when the prompt budget is available.
- Preserve contradictions in `_meta/conflicts.md` if later sources disagree.
