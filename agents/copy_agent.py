from core.llm import ask_llm
from utils.prompt_templates import copy_prompt

class CopyAgent:
    def run(self, product_info):
        prompt = copy_prompt(product_info)
        return ask_llm(prompt)
