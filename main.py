from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')


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


import nest_asyncio
nest_asyncio.apply()


async def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    await application.run_polling()


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
