import os
import logging
import asyncio
import psutil # Для статуса системы
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# --- НАСТРОЙКИ ---
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 5666795893 # <--- ПРОВЕРЬ СВОЙ ID ТУТ

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- ЛОГИКА КНОПОК ---

# Функция для создания главного меню
def get_main_menu():
    builder = InlineKeyboardBuilder()
    # 1. Сектор Деньги (Ссылка)
    builder.row(types.InlineKeyboardButton(text="💰 Passive Income", url="https://pawns.app/?r=1139563"))
    # 2. Сектор Музыка (Переход в меню)
    builder.row(types.InlineKeyboardButton(text="🎵 Suno AI Hub", callback_data="suno_menu"))
    # 3. Сектор Статус (Диагностика)
    builder.row(types.InlineKeyboardButton(text="🛡 Статус Системы", callback_data="status_check"))
    return builder.as_markup()

# --- ОБРАБОТЧИКИ ---

# Команда /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Уведомление тебе (Админка)
    if message.from_user.id != ADMIN_ID:
        try:
            await bot.send_message(ADMIN_ID, f"🔔 Новый пользователь: {message.from_user.full_name} (@{message.from_user.username})")
        except:
            pass # Если ты еще не писал боту, он не сможет отправить тебе сообщение

    await message.answer(
        "🦾 **JED СИСТЕМА АКТИВИРОВАНА!**\n\nВыберите сектор управления из списка ниже:",
        reply_markup=get_main_menu()
    )

# Обработка кнопки Suno AI
@dp.callback_query(F.data == "suno_menu")
async def process_suno(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="⬅️ Назад", callback_data="to_main"))
    
    await callback.message.edit_text(
        "🎵 **Suno AI Music Hub**\n\nЗдесь будет управление генерацией музыки для JD7-Records.\nМодуль в разработке...",
        reply_markup=builder.as_markup()
    )

# Обработка кнопки Статус
@dp.callback_query(F.data == "status_check")
async def process_status(callback: types.CallbackQuery):
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="🔄 Обновить", callback_data="status_check"))
    builder.row(types.InlineKeyboardButton(text="⬅️ Назад", callback_data="to_main"))

    await callback.message.edit_text(
        f"🖥 **Статус Системы JD7**\n\n⚙️ Нагрузка CPU: `{cpu}%` \n🧠 Память RAM: `{ram}%` \n🛰 Статус: `Online`",
        reply_markup=builder.as_markup()
    )

# Кнопка Назад
@dp.callback_query(F.data == "to_main")
async def process_back(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "🦾 **JED СИСТЕМА АКТИВИРОВАНА!**\n\nВыберите сектор:",
        reply_markup=get_main_menu()
    )

# --- ЗАПУСК ---
async def main():
    print("📡 JED BOT ЗАПУЩЕН И ГОТОВ К РАБОТЕ!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
())
        
    except Exception as e:
        logger.error(f"❌ Критическая ошибка: {e}", exc_info=True)
    finally:
        logger.info("❌ Бот остановлен")
        await bot.session.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
