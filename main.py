import os
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

# Логирование
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Токен
TOKEN = "7820178918:AAETCuw9c59S-STc7sFHPsUWvSDCpmjJ7DE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ============ РЕГИСТРАЦИЯ ОБРАБОТЧИКОВ ============

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    logger.info(f"✅ /start получен от {message.from_user.id} ({message.from_user.username})")
    await message.answer(
        "🤖 **Бот работает!**\n\n"
        "Добро пожаловать в JD7! 🎉\n\n"
        "Доступные команды:\n"
        "/test - Тест\n"
        "/help - Справка"
    )

@dp.message(Command("test"))
async def cmd_test(message: types.Message):
    logger.info(f"✅ /test получен")
    await message.answer("✅ Тест пройден!")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    logger.info(f"✅ /help получен")
    await message.answer(
        "📖 **Справка**\n\n"
        "/start - Главное меню\n"
        "/test - Тест бота\n"
        "/status - Статус"
    )

@dp.message(Command("status"))
async def cmd_status(message: types.Message):
    logger.info(f"✅ /status получен")
    await message.answer("✅ Бот онлайн и работает нормально!")

# Обработчик всех остальных сообщений
@dp.message()
async def echo(message: types.Message):
    logger.info(f"📨 Сообщение: {message.text}")
    await message.answer(f"Вы написали: {message.text}\n\nВведите /help для справки")

# ============ ЗАПУСК БОТА ============

async def main():
    logger.info("=" * 50)
    logger.info("🤖 Бот запускается...")
    logger.info("=" * 50)
    
    try:
        # Проверка токена и подключения
        me = await bot.get_me()
        logger.info(f"✅ Бот подключен: @{me.username}")
        logger.info(f"✅ ID бота: {me.id}")
        logger.info(f"✅ Имя: {me.first_name}")
        logger.info("=" * 50)
        logger.info("🟢 Бот ожидает сообщений...")
        logger.info("=" * 50)
        
        # Запуск polling (слушает сообщения)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
        
    except Exception as e:
        logger.error(f"❌ Критическая ошибка: {e}", exc_info=True)
    finally:
        logger.info("❌ Бот остановлен")
        await bot.session.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
