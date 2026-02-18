import os
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен
TOKEN = "7820178918:AAETCuw9c59S-STc7sFHPsUWvSDCpmjJ7DE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Простой /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    logger.info(f"✅ /start получен от {message.from_user.id}")
    await message.answer("🤖 **Бот работает!**\n\nДобро пожаловать в JD7! 🎉")

@dp.message(Command("test"))
async def cmd_test(message: types.Message):
    logger.info(f"Test получен")
    await message.answer("✅ Тест пройден!")

async def main():
    logger.info("🤖 Бот запускается...")
    try:
        # Провер��а токена
        me = await bot.get_me()
        logger.info(f"✅ Бот подключен: @{me.username}")
        
        # Запуск polling
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"❌ Ошибка: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
