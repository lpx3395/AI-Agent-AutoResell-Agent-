from core.llm import ask_llm
from utils.prompt_templates import product_analysis_prompt

class ProductAgent:
    def run(self, product_info):
        prompt = product_analysis_prompt(product_info)
        return ask_llm(prompt)
