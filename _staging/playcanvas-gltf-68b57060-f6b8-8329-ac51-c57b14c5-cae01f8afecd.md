---
title: PlayCanvas转换为glTF
source_id: playcanvas-gltf-68b57060-f6b8-8329-ac51-c57b14c5-cae01f8afecd
source_rel_path: raw/inbox/chatgpt_personal_backup_2026-04-10_md/Unity/PlayCanvas转换为glTF_68b57060-f6b8-8329-ac51-c57b14c57bf9_20250901_180731.md
status: staged
---

# PlayCanvas转换为glTF

## Staging Digest
# PlayCanvas转换为glTF

## Initial user need
我打算使用unity开发一个应用，根据业务逻辑，把指定的play canvas的发布模型转换为gltf，在转换并加载完成后呈现三维模型到应用中。
说一下你的思考。假设目前已有某个play canvas格式的模型json。

## Latest user clarification
加入一些消息，有插件可以在运行时加载GLTF，但是我们要梳理明白，运行时model.json转换为gltf的流程、临时可以存在哪里，怎么被使用。
https://github.com/KhronosGroup/UnityGLTF?tab=readme-ov-file

## Latest assistant answer
好的，我们把**运行时从封装的 model.json 转换→加载 glTF**这条链路，梳理成能落地的一整套流程：去哪儿转、临时放哪儿、插件怎么用，目标是“**尽快把

[... trimmed 247 characters ...]

## Follow-up
- Expand this digest into a durable wiki page when the prompt budget is available.
- Preserve contradictions in `_meta/conflicts.md` if later sources disagree.
