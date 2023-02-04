from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_comits as bc
import tok as t

app = ApplicationBuilder().token(t.token).build()

app.add_handler(CommandHandler("hello", bc.hello))
app.add_handler(CommandHandler("time", bc.time))
app.add_handler(CommandHandler("help", bc.help))
app.add_handler(CommandHandler("sum", bc.sum))
print('server start')
app.run_polling()