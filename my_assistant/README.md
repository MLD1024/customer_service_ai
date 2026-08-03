# Atguigu AI 项目

LLM驱动的对话系统项目。

## 项目结构

```
.
├── config.yml          # 系统配置（pipeline、policies）
├── domain.yml          # Domain定义（slots、responses、actions）
├── endpoints.yml       # 端点配置（models、nlg、tracker_store）
├── data/
│   └── flows.yml       # Flow定义
├── actions/
│   └── actions.py      # 自定义动作
└── models/             # 训练后的模型
```

## 快速开始

1. 安装依赖:
   ```bash
   pip install atguigu-ai
   ```

2. 配置环境变量:
   ```bash
   # 阿里云DashScope
   export DASHSCOPE_API_KEY=your-api-key
   
   # 或 OpenAI
   export OPENAI_API_KEY=your-api-key
   ```

3. 训练模型:
   ```bash
   atguigu train
   ```

4. 运行服务:
   ```bash
   atguigu run
   ```

5. 交互测试:
   ```bash
   atguigu shell
   ```

## 配置说明

### 模型配置 (endpoints.yml)

在 `endpoints.yml` 中配置LLM模型:

```yaml
models:
  default:
    type: "qwen"  # openai, qwen, azure, anthropic
    model: "qwen-plus"
    # api_key: ${DASHSCOPE_API_KEY}
    # api_base: "http://localhost:8000/v1"  # vLLM等自部署服务
    # enable_thinking: false  # 深度思考模式
```

### 槽位配置 (domain.yml)

```yaml
slots:
  user_name:
    type: text
    mappings:
      - type: from_llm  # 由LLM提取
    description: "用户姓名"
  
  order_id:
    type: text
    mappings:
      - type: controlled  # 由Action控制
    description: "订单编号"
```

### Pipeline配置 (config.yml)

```yaml
pipeline:
  - name: "LLMCommandGenerator"
    llm: "default"  # 引用endpoints.yml中的模型

policies:
  - name: "FlowPolicy"
  - name: "EnterpriseSearchPolicy"
    vector_store: "faiss"
    llm: "default"
```

## 更多信息

请参考 Atguigu AI 文档获取更多信息。
