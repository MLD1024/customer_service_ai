# GitHub AI 客服开源项目调研

调研日期：2026-07-23

## 筛选口径

- 方向：LLM 客服、AI Agent 客服、RAG 知识库、多渠道客服和人工接管。
- 严格时间范围：GitHub 搜索使用 `created:>=2025-01-01`，即仓库创建于 2025-01-01 至调研当天。
- 排序：优先 Star 数，其次参考最近更新时间和与当前项目的功能相似度。
- Star 和更新时间是调研当天的 GitHub 页面快照，后续会变化。

## 严格候选

| 排名 | 项目 | Star | 最近更新 | 技术/定位 | 结论 |
|---|---|---:|---|---|---|
| 1 | [openai/openai-cs-agents-demo](https://github.com/openai/openai-cs-agents-demo) | 约 6.5k | 2025-12-18 | Python、OpenAI Agents SDK、客服 Agent 示例 | Star 断层领先，最适合研究 Agent 编排、工具调用和客服流程；更偏官方示例，不是完整客服平台。 |
| 2 | [tgoai/tgo](https://github.com/tgoai/tgo) | 548 | 2026-04-28 | TypeScript、LLM 编排、RAG、多渠道客服 | 与当前项目目标最接近，适合重点研究完整平台结构和 Agent 团队编排。 |
| 3 | [chaitin/KoalaQA](https://github.com/chaitin/KoalaQA) | 533 | 2026-07-15 | TypeScript、AI 售后社区、问答、搜索、自助服务 | 中文场景契合度高，近期仍活跃，适合研究知识库、自助服务和运营端。 |
| 4 | [labring/tentix](https://github.com/labring/tentix) | 407 | 2026-06-04 | TypeScript、AI 原生客服、MCP、知识库 | 适合研究 MCP 扩展、知识库和 AI 原生客服产品形态。 |
| 5 | [evolution-foundation/evo-crm-community](https://github.com/evolution-foundation/evo-crm-community) | 223 | 2026-07-21 | AI 客服、CRM、WhatsApp、Pipeline | 最近更新非常活跃，适合研究 CRM、消息渠道和 Pipeline 集成；功能范围比当前项目更宽。 |
| 6 | [huabeitech/agent-desk](https://github.com/huabeitech/agent-desk) | 174 | 2026-06-30 | Go、Helpdesk、AI-first、人工接管、知识库 | 适合研究 AI 与人工客服协同、工单和生产化 Helpdesk 结构。 |
| 7 | [haoyiyin/basjoo](https://github.com/haoyiyin/basjoo) | 148 | 2026-06-17 | Python、FastAPI、Next.js、RAG、pgvector | 技术栈与当前 Python/FastAPI 项目接近，代码迁移和架构对照成本较低。 |
| 8 | [Hesper-Labs/owly](https://github.com/Hesper-Labs/owly) | 110 | 2026-04-14 | TypeScript、WhatsApp、Email、电话客服 | 适合研究多渠道接入，Star 和近期活跃度略低于前几项。 |

## 补充候选

以下项目创建时间也在严格范围内，但 Star 暂未达到第一梯队：

| 项目 | Star | 最近更新 | 参考价值 |
|---|---:|---|---|
| [traveler-leon/smart-customer-service-system](https://github.com/traveler-leon/smart-customer-service-system) | 98 | 2025-11-05 | 中文项目，LangGraph、MCP、静态/动态知识问答和 API 业务办理。 |
| [chattermate/chattermate.chat](https://github.com/chattermate/chattermate.chat) | 74 | 2026-07-22 | Python、AI Chatbot、人工接管、Shopify/Slack、可视化工作流；更新很活跃。 |
| [handsomestWei/customer-service-ai-agent](https://github.com/handsomestWei/customer-service-ai-agent) | 61 | 2026-05-26 | Python、LangGraph、多智能体客服，适合小范围阅读 Agent 流程实现。 |

## 推荐阅读顺序

1. `openai-cs-agents-demo`：学习清晰、官方的客服 Agent 编排基线。
2. `tgo`：对照完整 AI 客服平台、RAG、多渠道和 Agent 团队架构。
3. `KoalaQA`：重点看中文知识问答、自助服务和运营体系。
4. `basjoo`：重点看与当前项目接近的 FastAPI、RAG 和 pgvector 工程实现。
5. `agent-desk`：补充人工接管、Helpdesk 和生产运维设计。

## 最终建议

- 若只选一个用于学习 Agent Pipeline：优先 `openai/openai-cs-agents-demo`。
- 若只选一个作为完整产品架构参考：优先 `tgoai/tgo`。
- 若重点面向中文客服和知识库：优先 `chaitin/KoalaQA`。
- 若希望复用 Python/FastAPI 技术经验：优先 `haoyiyin/basjoo`，并结合 OpenAI 官方示例的 Agent 编排。

## 一手来源

- [GitHub：2025 年后创建的 AI 客服仓库，按 Star 排序](https://github.com/search?q=created%3A%3E%3D2025-01-01+%28customer+support+OR+customer+service%29+%28AI+OR+LLM+OR+agent%29&type=repositories&s=stars&o=desc)
- [GitHub：2025 年后创建且带 customer-support Topic 的 AI 仓库](https://github.com/search?q=created%3A%3E%3D2025-01-01+topic%3Acustomer-support+AI&type=repositories&s=stars&o=desc)
- [GitHub：2025 年后创建的 Customer Service LLM 仓库](https://github.com/search?q=created%3A%3E%3D2025-01-01+customer+service+LLM&type=repositories&s=stars&o=desc)
