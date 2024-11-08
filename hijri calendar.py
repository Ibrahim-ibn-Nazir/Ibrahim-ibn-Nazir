from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
from hijri_converter import Gregorian

# Replace 'YOUR_BOT_TOKEN' with the token you got from BotFather
BOT_TOKEN = '7828785397:AAErgUzaTE9gV4xTrAhJVRjFedlgSmtzpiQ'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Type /date to get today's date in both solar and lunar (Islamic) calendars.")

async def get_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the current date
    today = datetime.now()
    
    # Convert to Hijri date
    hijri_date = Gregorian(today.year, today.month, today.day).to_hijri()
    hijri_date_str = f"{hijri_date.day}-{hijri_date.month}-{hijri_date.year} AH"
    
    # Format the solar date
    solar_date_str = today.strftime("%d-%m-%Y")
    
    # Send the result
    response = f"Solar Date: {solar_date_str}\nIslamic Date: {hijri_date_str}"
    await update.message.reply_text(response)

def main():
    # Initialize Application with your bot token
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("date", get_date))
    
    # Start polling for updates
    app.run_polling()

if __name__ == "__main__":
    main()
