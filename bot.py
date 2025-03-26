from aiogram import Bot, Dispatcher, types, Router, filters, F
import asyncio

API_TOKEN = "7659698716:AAGeUzYvrxJ_6bWl8Wqzh8Jt-kYbuywMWU8"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
start_router = Router()


@start_router.message(filters.CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я echo bot. Напиши мне что-нибудь, и я повторю. Доступные команды: /help")


@start_router.message(filters.Command("help"))
async def send_help(message: types.Message):
    help_text = """
Доступные команды:
/start - Начать работу с ботом
/help - Показать это сообщение

Просто отправьте текст, и бот его повторит с приставкой "Вы сказали: "
    """
    await message.answer(help_text)


@start_router.message(F.text)
async def echo(message: types.Message):
    await message.answer(f"Вы сказали: {message.text}")

async def main():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

   