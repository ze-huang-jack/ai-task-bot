# 简单规则分类
def classify(text: str) -> str:
    text = text.lower()

    if "买" in text or "购买" in text:
        return "Shopping"
    if "写" in text or "报告" in text or "工作" in text:
        return "Work"
    if "学习" in text or "背" in text or "看书" in text:
        return "Study"

    return "General"


# 简单规则的下一步行动建议
def next_action(text: str) -> str:
    text = text.lower()

    if "写" in text:
        return "先列一个大纲（outline）"
    if "买" in text:
        return "先对比两个价格（compare）"
    if "学习" in text:
        return "先整理要学的内容（summarize topics）"

    return "先明确任务目标（define goal）"
