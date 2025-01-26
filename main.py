from flask import Flask, render_template, request, jsonify
from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

app = Flask(__name__)

# Telegram Bot Token
TOKEN = "7385151783:AAHVeBOK9VVf5zlFW3oqlB_WZz3RpuOjcjY"
bot = Bot(token=TOKEN)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    address = request.form.get('address')
    comments = request.form.get('comments')

    # Send data to Telegram bot
    bot.send_message(
        chat_id="5943499677",
        text=(
            f"📋 নতুন Contact Form জমা পড়েছে:\n\n"
            f"👤 নাম: {name}\n"
            f"📧 ইমেইল: {email}\n"
            f"📱 ফোন: {phone}\n"
            f"🏠 ঠিকানা: {address}\n"
            f"💬 মন্তব্য: {comments}"
        )
    )
    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
