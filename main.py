import asyncio

from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os


BOT_TOKEN = os.getenv('BOT_TOKEN')
PORT = int(os.environ.get('PORT', 10000))


async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        welcome_message = (
            "<b>Я смотрю на вас, смотрю — и вижу всё новые лица.</b>\n"
            "<b>Тихо.◻️▪️◻️</b>\n"
            "А это значит:<tg-spoiler> кто-то нарушил первое и второе правило клуба.</tg-spoiler>🔊\n\n"
            "<b>Я вижу в Бойцовском Клубе самых сильных мужчин на свете.</b>\n"
            "Потенциал, который не должен тратиться на офисы, пустые разговоры "
            "и бесконечную прокрутку экрана.🔇💭\n\n"
            f"<i>Добро пожаловать в Бойцовский Клуб, {user.first_name}.</i>📢🃏"
        )

        await update.message.reply_text(
            text=welcome_message,
            parse_mode="HTML"  # Для поддержки эмодзи и форматирования
        )


async def run_bot():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    if 'RENDER' in os.environ:
        await application.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=BOT_TOKEN,
            webhook_url=f"https://fighterbot-4ts2.onrender.com/{BOT_TOKEN}",
            drop_pending_updates=True,
            close_loop=False
        )
    else:
        await application.run_polling(drop_pending_updates=True)


def main():
    try:
        loop = asyncio.get_running_loop()
    except Exception as e:
        print(e)

    if 'RENDER' in os.environ:
        loop.create_task(run_bot())
        loop.run_forever()
    else:
        loop.run_until_complete(run_bot())


if __name__ == '__main__':
    main()
