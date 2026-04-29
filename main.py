from core.workflow import AutoResellWorkflow

if __name__ == "__main__":
    product_info = """
    骆驼空气循环扇，变频静音，大风量，适合宿舍和办公室
    """

    workflow = AutoResellWorkflow()
    result = workflow.run(product_info)

    print("\n=== 最终结果 ===")
    for k, v in result.items():
        print(f"\n{k.upper()}:\n{v}")
