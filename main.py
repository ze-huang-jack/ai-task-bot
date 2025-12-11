from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters
from config import BOT_TOKEN
from bot.handlers import add_task, history
from bot.storage import init_db

init_db()

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("history", history))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, add_task))

app.run_polling()
