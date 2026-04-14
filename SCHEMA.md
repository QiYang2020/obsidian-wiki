# Wiki Schema

## Domain
这个 wiki 用来积累个人长期知识资产，重点覆盖：
- ChatGPT 历史对话中沉淀下来的稳定知识点
- 项目经验、技术方案、术语解释、决策脉络
- 新旧观点冲突、重复主题归并、长期偏好与规范

## Conventions
- 原始资料只放在 `raw/`，保持不可变
- wiki 页面优先使用稳定、可读的文件名；能用英文 slug 就用英文 slug，中文更清晰时可直接使用中文名，但避免空格与杂乱符号
- 每个 wiki 页面尽量包含 frontmatter，至少写明 `title`、`updated`、`type`、`sources`
- 使用 `[[wikilinks]]` 做交叉引用；新增或大改页面时至少补 2 个相关链接
- 每次成功 ingest 后都要同步更新 `index.md` 和 `log.md`
- 对互相矛盾的结论，不静默覆盖；保留带日期和来源的双观点，并记录到 `_meta/conflicts.md`
- 高频主题要在 `_meta/topic-map.md` 里形成导航，不把相似知识散落成孤页

## Page Types
- `entities/`: 人、组织、产品、项目、工具、模型
- `concepts/`: 概念、方法、流程、规范、工作流
- `comparisons/`: 对比分析、方案权衡
- `queries/`: 值得保留的问题、总结、阶段性综合
- `_meta/`: 导航、冲突、维护页

## Page Thresholds
- 同一实体/概念在 2 个以上来源出现，或在单个来源中占核心位置时，考虑单独建页
- 只是顺带提到的名词，不单独建页，优先并入现有页面
- 明显重复的观点要合并到上层总结，不堆砌相似段落
- 页面超过约 200 行时，优先拆成子主题并互相链接

## Conflict Policy
当新信息与既有内容冲突时：
1. 先比较时间，较新的来源默认优先
2. 如果仍有实质冲突，同时保留双方说法与来源
3. 在相关页面和 `_meta/conflicts.md` 中记录冲突点与待确认事项
4. 需要人工判断时，明确标注 `review-needed`

## Memory Boundary
- Built-in memory 只保存长期稳定、跨任务有价值的信息
- 不把原始摘录、额度报错、一次性过程问题写入 memory
- 当 memory 接近 80% 容量时，先合并再新增
