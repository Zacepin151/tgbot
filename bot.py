from aiogram import Bot, Dispatcher, types, Router, filters, F
import asyncio

# Токен вашего бота
API_TOKEN = "7820806714:AAEOT3fv8ABLOd1LFgXWo---nspfGZr7mIE"

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
start_router = Router()

# Обработчик команды /start
@start_router.message(filters.CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я echo bot. Напиши мне что-нибудь, и я повторю.")

# Обработчик команды /help
@start_router.message(filters.Command("help"))
async def send_help(message: types.Message):
    help_text = (
        "Доступные команды:\n"
        "/start - Начать общение с ботом\n"
        "/help - Показать список доступных команд"
    )
    await message.reply(help_text)

# Обработчик текстовых сообщений
@start_router.message(F.text)
async def echo(message: types.Message):
    await message.answer(f"Вы сказали: {message.text}")

async def main():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
