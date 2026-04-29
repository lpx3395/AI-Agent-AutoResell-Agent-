from core.llm import ask_llm
from utils.prompt_templates import pricing_prompt

class PricingAgent:
    def run(self, product_info):
        prompt = pricing_prompt(product_info)
        return ask_llm(prompt)
