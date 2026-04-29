auto-resell-agent/
│
├── README.md
├── requirements.txt
├── main.py
│
├── agents/
│   ├── copy_agent.py
│   ├── pricing_agent.py
│   ├── product_agent.py
│
├── core/
│   ├── workflow.py
│   ├── llm.py
│
├── data/
│   ├── sample_products.json
│
└── utils/
    ├── prompt_templates.py

# AI-Agent-AutoResell-Agent-
自动分析商品（图片/文案） 自动生成闲鱼高转化文案 自动定价策略 自动发布/模拟发布 数据反馈优化（简单版）
# Auto Resell Agent

一个基于多Agent协作的闲鱼自动选品+文案生成系统。

## 功能
- 商品分析
- 自动定价
- 爆款文案生成
- 多Agent协同

## 技术点
- LLM Agent
- Prompt Engineering
- Workflow orchestration

## 使用
```bash
pip install -r requirements.txt
python main.py
