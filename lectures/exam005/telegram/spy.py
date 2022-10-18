from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    files = open("loger.csv", "a")
    files.write(f"{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n")
    files.close()