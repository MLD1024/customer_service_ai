# AI 客服开源项目对比与选型建议

调研日期：2026-07-23

## 结论

不建议推倒当前项目后直接照搬某一个仓库。推荐采用：

> 当前项目作为对话与业务流程底座，TGO 作为客服产品蓝图，OpenAI Demo 作为 Agent 编排参考，KoalaQA 作为中文知识运营参考，TenTix 作为 MCP 扩展参考。

如果必须只选一个项目作为整体参考，选择 `tgoai/tgo`；如果只学习 Agent Pipeline，选择 `openai/openai-cs-agents-demo`。

## 当前项目定位

当前项目已经具备较完整的 AI 客服对话内核：

- Python、FastAPI、LangGraph
- LLM 将自然语言转换为 Command/DSL
- Flow、Slots、Domain、Action 驱动可控的多轮业务流程
- DialogueStateTracker 和 Dialogue Stack 管理会话状态
- RAG、GraphRAG、自定义 Retriever
- REST、WebSocket、Socket.IO、CLI 和 Inspect 页面
- JSON/MySQL Tracker Store
- 已有人工转接命令和状态帧

它尤其适合订单查询、物流、退款、售后申请等要求流程可控、能够调用企业 API 的交易型客服。

主要缺口在产品层，而不是对话内核：坐席工作台、会话排队与分配、完整人工接管、工单、多渠道适配、知识库运营后台、质量评估、监控审计、多租户和权限。

## 对比矩阵

| 维度 | 当前项目 | OpenAI CS Agents Demo | TGO | KoalaQA | TenTix |
|---|---|---|---|---|---|
| 核心定位 | 对话框架/业务 Flow 内核 | 官方客服 Agent 示例 | 完整 AI 客服平台 | 中文 AI 售后社区与自助问答 | AI 原生客服与 MCP 平台 |
| 技术栈契合度 | 基准：Python/FastAPI | 高，Python 与 Agents SDK | 中，偏 TypeScript 产品栈 | 中低，偏 TypeScript 应用栈 | 中低，偏 TypeScript 应用栈 |
| 可控业务流程 | 强 | 中，偏 Agent 自主决策 | 中到强 | 弱到中，偏问答与社区 | 中，偏工具和知识调用 |
| Agent 编排 | LangGraph + Policy + Command | 强，官方 handoff/tool/guardrail 范式 | 强，面向客服 Agent 团队 | 中 | 强调 MCP 和工具扩展 |
| RAG/知识库 | 已有基础能力 | 示例级 | 平台级 | 强，中文知识问答和运营突出 | 强调知识库与 MCP |
| 人工接管 | 有内核状态，缺完整闭环 | 有 handoff 思路，非坐席平台 | 更适合作为完整产品参考 | 不是核心优势 | 可参考产品交互，成熟度需验证 |
| 多渠道 | 有 Channel 抽象，缺生产 Adapter | 非重点 | 重点参考项 | 非核心优势 | 可参考集成方式 |
| 工单/坐席后台 | 缺失 | 缺失 | 四者中最值得参考 | 偏社区和自助服务 | 可参考 AI 原生界面 |
| 中文场景 | 可定制 | 一般 | 可本地化 | 最强 | 可本地化 |
| 直接二开成本 | 已有代码，无迁移成本 | 高，需补产品体系 | 中到高，需接受其技术栈 | 高，产品目标不同 | 高，需评估成熟度和栈差异 |
| 最适合借鉴 | 继续作为核心底座 | Agent 路由、handoff、guardrails、evals | 产品架构、渠道、坐席、运营后台 | 知识库、自助服务、中文运营 | MCP、插件化工具接入 |

## 四个项目的优缺点

### 1. openai/openai-cs-agents-demo

优点：

- OpenAI 官方示例，Agent、工具调用、路由和 handoff 的表达较清晰。
- Star 明显领先，学习资料和社区关注度高。
- Python 技术方向与当前项目接近，适合做小范围原型验证。
- 适合补充 guardrails、tracing、evals 和多 Agent 协作思路。

缺点：

- 本质是 Demo，不是可直接交付的客服平台。
- 坐席、排队、工单、多渠道、租户、权限和运营后台需要自行建设。
- Agent 自主决策方式不能直接替代当前项目的确定性业务 Flow。

建议借鉴：Agent handoff、tool calling、guardrails、trace/eval 设计。

不建议照搬：把所有交易流程都改造成自由 Agent 对话。

### 2. tgoai/tgo

优点：

- 四个项目中与“完整 AI 客服产品”的目标最接近。
- 更适合观察 Agent、RAG、多渠道、客服管理后台等模块如何组合。
- 可作为坐席工作台、会话管理、渠道接入和产品信息架构的主要参照。
- 近期仍有更新，产品视角比 SDK Demo 完整。

缺点：

- 技术栈与当前 Python 内核不完全一致，直接迁移会增加维护成本。
- 平台能力较多，整体 Fork 后再改可能比按模块吸收更重。
- Star 和生态规模远低于 OpenAI 官方示例，关键模块仍需代码级验证。

建议借鉴：产品分层、坐席与会话工作台、多渠道 Adapter、知识库后台、运营配置。

不建议照搬：为了统一技术栈而重写当前成熟的 Flow、Slots、Tracker 和 Action 内核。

### 3. chaitin/KoalaQA

优点：

- 中文场景契合度最高，适合知识问答、售后社区和自助服务。
- 可重点参考知识沉淀、搜索、问答展示和用户反馈闭环。
- 更新活跃，适合观察中文知识运营产品的功能设计。

缺点：

- 更像 AI 售后社区/知识问答产品，不是交易型多轮客服引擎。
- 订单、退款、物流等强业务流程仍需要当前项目的 Flow 和 Action。
- 直接 Fork 会让产品形态偏向社区，未必符合在线客服工作台目标。

建议借鉴：知识库运营、中文检索、自助问答、答案反馈和社区沉淀。

不建议照搬：用问答社区模型承载全部客服业务流程。

### 4. labring/tentix

优点：

- MCP 和 AI 原生客服方向鲜明，适合参考工具和外部系统的标准化接入。
- 对构建插件市场、业务工具注册和动态能力扩展有启发。
- 可以帮助当前 Action 体系逐步兼容 MCP Server。

缺点：

- 社区体量和成熟度低于 OpenAI Demo，生产能力需要更深入验证。
- 技术栈和产品抽象与当前项目存在迁移成本。
- MCP 解决的是工具接入标准，不等于完整的客服流程、坐席和工单体系。

建议借鉴：MCP Client、工具注册、权限隔离、插件生命周期和知识接入。

不建议照搬：仅靠 MCP 代替 Domain、Flow、Tracker 等业务编排能力。

## 推荐建设路线

### 路线 A：继续演进当前项目（推荐）

1. 保留 `Domain + Flow + Slots + Tracker + Action`，作为交易型客服核心。
2. 参考 TGO 增加会话中心、坐席工作台、队列路由、工单和渠道 Adapter。
3. 参考 OpenAI Demo 完善 Agent handoff、guardrails、trace 和 evals。
4. 参考 KoalaQA 建设知识采集、切片、审核、发布、反馈和命中分析后台。
5. 参考 TenTix 为现有 Action 增加 MCP Adapter，而不是立即替换 Action API。

这条路线能最大化复用现有代码，并保持关键业务流程的确定性和可审计性。

### 路线 B：直接 Fork TGO

适合条件：希望尽快获得一个完整产品外壳，团队接受 TGO 的技术栈，并且当前项目尚未承载大量业务 Flow。

代价：需要迁移现有 Domain、Slots、Action、Tracker 和 LangGraph 逻辑；如果重新实现这些能力，短期看启动快，长期可能出现双套编排模型和较高维护成本。

## 最终选型

- 只选一个整体产品参考：`tgoai/tgo`
- 只选一个 Agent 技术参考：`openai/openai-cs-agents-demo`
- 中文知识库和自助售后参考：`chaitin/KoalaQA`
- MCP 和插件扩展参考：`labring/tentix`
- 实际开发底座：继续使用当前项目

推荐的组合不是“四个项目都抄”，而是每个项目只吸收它最成熟的一层，避免引入四套重叠架构。

## 资料来源与限制

- GitHub 仓库：<https://github.com/openai/openai-cs-agents-demo>
- GitHub 仓库：<https://github.com/tgoai/tgo>
- GitHub 仓库：<https://github.com/chaitin/KoalaQA>
- GitHub 仓库：<https://github.com/labring/tentix>
- 当前项目 README、源码结构和 `graphify-out/GRAPH_REPORT.md`
- 候选项目要求为 2025-01-01 至调研日创建；Star 和更新时间为调研快照，会随时间变化。
- 调研期间 GitHub 连接出现重置，未能完成四个仓库的本地浅克隆。因此对 Fork 成本和生产成熟度的判断属于架构预评估，正式选型前应再做 PoC、许可证、安全和部署审计。
