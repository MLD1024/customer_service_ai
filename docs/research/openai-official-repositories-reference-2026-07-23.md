# OpenAI 官方 GitHub 仓库参考指南

调研日期：2026-07-23

数据来源：OpenAI GitHub 组织公开仓库、GitHub REST API、各仓库官方 README。

## 结论

OpenAI 官方仓库数量很多，不建议只按 Star 阅读。对一般 AI 应用开发，最值得优先关注的是：

1. `openai-cookbook`：API 使用模式和场景示例总入口。
2. `openai-python` / `openai-node`：官方 SDK 和 Responses API 的真实接口设计。
3. `openai-agents-python` / `openai-agents-js`：Agent、工具、MCP、handoff、guardrails、trace 和语音 Agent。
4. `evals` / `simple-evals`：LLM 应用评测体系。
5. `openai-realtime-agents` / `openai-realtime-console`：实时语音和低延迟多模态交互。
6. `openai-structured-outputs-samples`：结构化输出和可靠业务协议。
7. `openai-apps-sdk-examples` / ChatKit 示例：AI 应用 UI 和嵌入式聊天产品。
8. `codex` / `skills` / `plugins` / `symphony`：编码 Agent、技能、插件和并行任务编排。

对于当前 `atguigu_ai` 项目，最高优先级是：

> `openai-agents-python` + `openai-cookbook` + `simple-evals` + `openai-realtime-agents` + `openai-structured-outputs-samples`

## 一、API 与基础 SDK

| 仓库 | 用途 | 参考价值 |
|---|---|---|
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | OpenAI API 示例和指南 | 最适合查找 RAG、工具调用、Responses API、Prompt、评测和多模态示例 |
| [openai/openai-python](https://github.com/openai/openai-python) | Python 官方 SDK | 当前 Python 项目首选；重点看 Responses API、流式响应、错误处理和 Realtime API |
| [openai/openai-node](https://github.com/openai/openai-node) | JavaScript/TypeScript 官方 SDK | Web、Node.js 和全栈应用首选 |
| [openai/openai-java](https://github.com/openai/openai-java) | Java 官方 SDK | Spring Boot 或 Java 企业系统集成参考 |
| [openai/openai-go](https://github.com/openai/openai-go) | Go 官方 SDK | 高并发服务和 Go 后端参考 |
| [openai/openai-dotnet](https://github.com/openai/openai-dotnet) | .NET 官方 SDK | C#/.NET 应用参考 |
| [openai/openai-openapi](https://github.com/openai/openai-openapi) | OpenAI API 的 OpenAPI 描述 | 生成客户端、了解协议和网关封装时有用 |
| [openai/openai-cli](https://github.com/openai/openai-cli) | 官方 API CLI | 命令行调用和自动化脚本参考 |
| [openai/tiktoken](https://github.com/openai/tiktoken) | 高性能 Tokenizer | Token 预算、上下文裁剪、成本估算和文本切片参考 |

新项目建议优先使用 Responses API。官方 Python SDK README 已明确将 Responses API 作为与 OpenAI 模型交互的主要 API。

## 二、Agent 与工作流

| 仓库 | 用途 | 最值得参考的部分 |
|---|---|---|
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | Python 多 Agent 框架 | Tools、MCP、handoff、guardrails、sessions、tracing、Realtime Agents |
| [openai/openai-agents-js](https://github.com/openai/openai-agents-js) | TypeScript 多 Agent 与语音 Agent 框架 | Web/Node Agent、语音 Agent、工具和 handoff |
| [openai/openai-cs-agents-demo](https://github.com/openai/openai-cs-agents-demo) | 客服 Agent 示例 | 客服路由、专业 Agent 分工、人工转接和业务工具调用 |
| [openai/openai-realtime-agents](https://github.com/openai/openai-realtime-agents) | Realtime API 高级语音 Agent 示例 | 低延迟语音、多 Agent 路由、状态和事件流 |
| [openai/swarm](https://github.com/openai/swarm) | 轻量多 Agent 编排教育框架 | 适合理解 Agent 和 handoff 的早期设计，不建议作为新生产项目首选 |

`openai-agents-python` 的 README 明确覆盖函数工具、MCP、托管工具、handoff、guardrails、sessions、tracing 和 Realtime Agents。它是当前 Python Agent 方向最值得精读的官方仓库。

## 三、实时语音与多模态

| 仓库 | 用途 | 参考价值 |
|---|---|---|
| [openai/openai-realtime-agents](https://github.com/openai/openai-realtime-agents) | Realtime API Agent Demo | 语音客服、电话助手、实时销售助手的首选参考 |
| [openai/openai-realtime-console](https://github.com/openai/openai-realtime-console) | Realtime API 调试控制台 | 事件、音频流、会话参数和工具调用调试参考 |
| [openai/openai-realtime-twilio-demo](https://github.com/openai/openai-realtime-twilio-demo) | Realtime 与 Twilio 电话集成 | 电话机器人和呼叫中心接入参考 |
| [openai/realtime-voice-component](https://github.com/openai/realtime-voice-component) | 实时语音 UI 组件 | Web 端语音交互组件参考 |
| [openai/openai-realtime-embedded](https://github.com/openai/openai-realtime-embedded) | 嵌入式设备使用 Realtime API | IoT、硬件终端和设备语音助手参考 |
| [openai/openai-fm](https://github.com/openai/openai-fm) | Speech API 演示 | 语音合成产品和音色试听界面参考 |
| [openai/whisper](https://github.com/openai/whisper) | 开源语音识别模型 | 本地转写、离线 ASR 和语音数据处理参考 |

## 四、AI 应用、UI 与 ChatKit

| 仓库 | 用途 | 参考价值 |
|---|---|---|
| [openai/openai-apps-sdk-examples](https://github.com/openai/openai-apps-sdk-examples) | Apps SDK 示例应用 | ChatGPT 内应用、工具 UI 和交互式结果展示参考 |
| [openai/apps-sdk-ui](https://github.com/openai/apps-sdk-ui) | Apps SDK UI 组件 | 官方应用组件和界面规范参考 |
| [openai/openai-chatkit-starter-app](https://github.com/openai/openai-chatkit-starter-app) | ChatKit 起步应用 | 快速搭建嵌入式聊天界面 |
| [openai/openai-chatkit-advanced-samples](https://github.com/openai/openai-chatkit-advanced-samples) | ChatKit 高级示例 | 复杂消息、工具结果和产品化交互参考 |
| [openai/chatkit-js](https://github.com/openai/chatkit-js) | ChatKit JavaScript SDK | 自定义聊天前端集成参考 |
| [openai/openai-responses-starter-app](https://github.com/openai/openai-responses-starter-app) | Responses API 起步应用 | 新式对话应用的端到端结构参考 |
| [openai/openai-structured-outputs-samples](https://github.com/openai/openai-structured-outputs-samples) | Structured Outputs 示例 | JSON Schema、类型安全返回和业务协议可靠性参考 |
| [openai/openai-quickstart-python](https://github.com/openai/openai-quickstart-python) | Python 快速开始 | 初学和最小 API 示例 |
| [openai/openai-quickstart-node](https://github.com/openai/openai-quickstart-node) | Node.js 快速开始 | Node/Web 初学示例 |

## 五、计算机操作与自动化 Agent

| 仓库 | 用途 | 参考价值 |
|---|---|---|
| [openai/openai-cua-sample-app](https://github.com/openai/openai-cua-sample-app) | Computer Using Agent 示例 | 浏览器/桌面操作、环境隔离和操作循环参考 |
| [openai/openai-testing-agent-demo](https://github.com/openai/openai-testing-agent-demo) | UI 测试 Agent 示例 | 自动化测试、截图判断和操作反馈循环参考 |
| [openai/operator](https://github.com/openai/operator) | 若仓库公开可用，关注计算机操作相关实现 | 需以仓库当前 README 和状态为准，不应仅凭名称采用 |

计算机操作 Agent 风险高于普通工具调用，实际产品必须增加域名白名单、操作确认、凭据隔离、审计日志和超时终止。

## 六、评测、质量与安全

| 仓库 | 用途 | 参考价值 |
|---|---|---|
| [openai/evals](https://github.com/openai/evals) | LLM 与 LLM 系统评测框架 | 建立任务集、评分器、回归测试和模型对比体系 |
| [openai/simple-evals](https://github.com/openai/simple-evals) | 简洁的评测实现 | 代码更小，适合先理解和接入自己的业务评测 |
| [openai/frontier-evals](https://github.com/openai/frontier-evals) | Frontier 模型能力与风险评测 | 高能力模型、安全和复杂任务评测参考 |
| [openai/human-eval](https://github.com/openai/human-eval) | 代码生成评测 | 代码 Agent 的 pass@k 和隔离执行参考 |
| [openai/mle-bench](https://github.com/openai/mle-bench) | 机器学习工程 Agent Benchmark | 长任务 Agent、产物判断和工程能力评测参考 |
| [openai/model_spec](https://github.com/openai/model_spec) | OpenAI Model Spec | 理解模型行为目标、边界和指令层级 |
| [openai/openai-moderation-api](https://github.com/openai/openai-moderation-api) | 若仓库仍公开可用，关注内容安全示例 | 新项目应以当前官方 Moderation API 和文档为准 |

业务 Agent 上线前，至少需要四类评测：意图/路由、工具参数、最终答案、端到端业务成功率。客服还应增加转人工准确率、知识命中率、幻觉率和敏感信息泄露率。

## 七、编码 Agent 与 Agent 工程化

| 仓库 | 用途 | 参考价值 |
|---|---|---|
| [openai/codex](https://github.com/openai/codex) | 开源编码 Agent | 工具执行、沙箱、审批、任务循环、上下文管理和终端 UX |
| [openai/skills](https://github.com/openai/skills) | Codex Skills 目录 | 可复用工作流、技能触发和渐进式上下文加载 |
| [openai/plugins](https://github.com/openai/plugins) | OpenAI/Codex 插件 | 工具、技能和扩展能力的打包方式 |
| [openai/role-specific-plugins](https://github.com/openai/role-specific-plugins) | 角色化插件模板 | 为测试、审查、运维等角色封装 Agent 能力 |
| [openai/symphony](https://github.com/openai/symphony) | 自治实现任务编排 | 隔离执行、并行任务、项目工作转实现运行的编排参考 |
| [openai/codex-action](https://github.com/openai/codex-action) | GitHub Action 中使用 Codex | CI、自动审查和仓库自动化参考 |
| [openai/codex-universal](https://github.com/openai/codex-universal) | Codex 环境基础镜像 | Agent 沙箱和通用开发环境参考 |

这些仓库虽然不是客服项目，但对任何生产 Agent 系统的权限、隔离、审批、工具协议和长任务执行都很有参考价值。

## 八、开源模型与模型运行

| 仓库 | 用途 | 参考价值 |
|---|---|---|
| [openai/gpt-oss](https://github.com/openai/gpt-oss) | OpenAI 开源权重语言模型 | 私有化部署、模型推理和开放模型研究 |
| [openai/harmony](https://github.com/openai/harmony) | gpt-oss Harmony 响应格式渲染 | 模型消息格式、工具调用和推理输出处理 |
| [openai/whisper](https://github.com/openai/whisper) | 开源语音识别 | 本地 ASR 和转写 |
| [openai/CLIP](https://github.com/openai/CLIP) | 图文对齐模型 | 图像检索、分类和跨模态 Embedding |
| [openai/shap-e](https://github.com/openai/shap-e) | 文本/图片生成 3D | 3D 内容生成研究 |
| [openai/point-e](https://github.com/openai/point-e) | 点云生成 | 3D 生成研究 |
| [openai/guided-diffusion](https://github.com/openai/guided-diffusion) | 扩散模型研究代码 | 图像生成研究，不是当前 API 应用主线 |

## 九、解释性与研究工具

| 仓库 | 用途 | 参考价值 |
|---|---|---|
| [openai/transformer-debugger](https://github.com/openai/transformer-debugger) | Transformer 内部行为调试 | 神经元、激活和模型解释性研究 |
| [openai/sparse_autoencoder](https://github.com/openai/sparse_autoencoder) | 稀疏自编码器研究 | Mechanistic Interpretability 参考 |
| [openai/circuit_sparsity](https://github.com/openai/circuit_sparsity) | 模型电路稀疏性研究 | 模型解释与安全研究 |
| [openai/spinningup](https://github.com/openai/spinningup) | 深度强化学习教程 | 强化学习入门，非现代 LLM 应用主线 |
| [openai/baselines](https://github.com/openai/baselines) | 强化学习算法基线 | 历史研究价值较高，新项目需检查维护状态 |

## 十、不建议作为新项目主底座的仓库

- `swarm`：教育和概念验证价值高，但新 Agent 项目优先使用 Agents SDK。
- `chatgpt-retrieval-plugin`：适合理解早期 Retrieval Plugin 设计；新 RAG 应结合 Responses API、File Search、Vector Store 或自己的检索服务。
- `openai-assistants-quickstart`：适合了解 Assistants API 历史用法；新项目优先检查 Responses API 和 Agents SDK 的当前迁移路线。
- 已归档的 Gym、Universe、旧机器人、旧 GAN/RL 仓库：适合论文复现，不适合作为现代应用工程底座。
- 长期未更新但 Star 高的仓库：Star 代表历史影响力，不等于当前产品路线。

## 当前项目的推荐阅读顺序

1. `openai-agents-python`：对照当前 `LangGraph + Policy + Command`，重点看 Tools、MCP、handoff、guardrails、sessions 和 tracing。
2. `openai-cs-agents-demo`：理解客服专业 Agent 分工，但保留当前 Flow 的确定性业务流程。
3. `openai-structured-outputs-samples`：把当前 LLM 输出 Command/DSL 升级为 Schema 约束的结构化协议。
4. `simple-evals`：先建立小型客服评测集，再考虑完整 `evals`。
5. `openai-realtime-agents`：为语音客服和电话渠道预留 Realtime Adapter。
6. ChatKit 示例：建设用户聊天端；坐席后台仍应按客服业务单独设计。
7. `codex` 和 `skills`：借鉴 Action/MCP 的权限、审批、技能加载和执行隔离。

## 建议吸收的具体能力

| 当前能力 | OpenAI 参考项目 | 建议演进 |
|---|---|---|
| LLM 生成 Command/DSL | Structured Outputs Samples、Agents SDK | 使用 JSON Schema/Pydantic 约束命令，减少正则解析和格式错误 |
| Flow Policy | Agents SDK、CS Agents Demo | 保留确定性 Flow，在复杂开放任务中增加专业 Agent handoff |
| 自定义 Action | Agents SDK Tools、MCP | 增加 MCP Adapter、超时、权限、审批和审计 |
| HumanHandoffCommand | CS Agents Demo、Realtime Agents | 补齐队列、分配、接管、归还和上下文摘要生命周期 |
| Inspect/日志 | Agents SDK Tracing、Realtime Console | 增加 trace、tool span、token、延迟和错误可视化 |
| 测试 | simple-evals、evals | 建立离线评测集和 CI 回归门禁 |
| WebSocket | Realtime API 示例 | 增加音频事件、打断、VAD 和流式工具调用支持 |

## 数据说明

- Star、更新时间和仓库状态是 2026-07-23 的 GitHub 快照，会持续变化。
- 调研优先采用官方仓库、GitHub API 和 README；部分 README 请求触发 GitHub 限流，未逐一读取全部仓库源码。
- 正式选型时还需检查每个仓库的许可证、最新 Release、Issue、Security Policy 和迁移说明。
