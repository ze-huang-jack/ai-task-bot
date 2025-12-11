from telegram import Update
from telegram.ext import ContextTypes
from bot.storage import save_task, list_tasks
from bot.ai import classify, next_action


async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    category = classify(text)
    action = next_action(text)

    save_task(text, category, action)

    await update.message.reply_text(
        f"📌 分类：{category}\n➡️ 下一步：{action}\n\n已记录！"
    )


async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tasks = list_tasks()

    if not tasks:
        await update.message.reply_text("暂无任务")
        return

    msg = ""
    for t in tasks:
        msg += f"{t.id}. {t.text} - {t.category} - Next: {t.next_action}\n"

    await update.message.reply_text(msg)
