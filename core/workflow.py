from agents.copy_agent import CopyAgent
from agents.pricing_agent import PricingAgent
from agents.product_agent import ProductAgent

class AutoResellWorkflow:
    def __init__(self):
        self.copy_agent = CopyAgent()
        self.pricing_agent = PricingAgent()
        self.product_agent = ProductAgent()

    def run(self, product_info):
        print("🔍 分析商品...")
        analysis = self.product_agent.run(product_info)

        print("💰 定价中...")
        pricing = self.pricing_agent.run(product_info)

        print("✍️ 生成文案...")
        copy = self.copy_agent.run(product_info)

        return {
            "analysis": analysis,
            "pricing": pricing,
            "copy": copy
        }
