from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_comits as bc


app = ApplicationBuilder().token("6069521139:AAH5lLaVp7qt5YYWACUdfGUP6TGr39m55mI").build()

app.add_handler(CommandHandler("hello", bc.hello))
app.add_handler(CommandHandler("time", bc.time))
app.add_handler(CommandHandler("help", bc.help))
app.add_handler(CommandHandler("sum", bc.sum))
print('server start')
app.run_polling()