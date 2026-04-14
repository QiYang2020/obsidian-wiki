---
title: Unity Sentis AI Integration
source_id: unity-sentis-ai-integration-79ab7d2c-da97-4127-a-851e2e5522cf
source_rel_path: raw/inbox/chatgpt_personal_backup_2026-04-10_md/Unity Sentis AI Integration_79ab7d2c-da97-4127-aa00-94e47b59ebfa_20231206_101736.md
status: staged
---

# Unity Sentis AI Integration

## Staging Digest
# Unity Sentis AI Integration

## Initial user need
unity sentis，目前新发布的AI辅助包，请协助我理解学习。
你可以先通过网络资料全面了解一下unity sentis

## Latest user clarification
详细说明应用ai模型的那一部分，尤其是实现原理。

## Latest assistant answer
应用AI模型的部分主要集中在`ComputerMove()`函数中，这是游戏逻辑的核心部分，用于在玩家的每一步之后由AI决定电脑对手的行动。下面详细说明这部分的代码和实现原理：

### 应用AI模型 - `ComputerMove()`
1. **翻转棋盘**：
   - 由于神经网络模型是从当前玩家的角度来训练的，所以在AI计算之前，需要将棋盘状态翻转，以确保模型可以从电脑玩家的视角进行评估。

2. **执行

[... trimmed 38 characters ...]

## Follow-up
- Expand this digest into a durable wiki page when the prompt budget is available.
- Preserve contradictions in `_meta/conflicts.md` if later sources disagree.
