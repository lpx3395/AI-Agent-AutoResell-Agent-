def copy_prompt(product_info):
    return f"""
你是一个闲鱼爆款文案专家，请根据以下商品信息生成高转化文案：

商品信息：
{product_info}

要求：
1. 强烈吸引点击
2. 强调“清仓/低价/捡漏”
3. 适合无货源卖家
4. 100-200字
"""

def pricing_prompt(product_info):
    return f"""
你是电商定价专家，请根据市场情况为以下商品定价：

{product_info}

输出：
1. 建议售价
2. 利润空间分析
3. 是否值得卖（是/否）
"""

def product_analysis_prompt(product_info):
    return f"""
分析这个商品是否适合在闲鱼卖爆：

{product_info}

输出：
1. 市场需求（高/中/低）
2. 竞争强度
3. 推荐指数（1-10）
"""
