import os
import logging
import asyncio
import psutil  # Мониторинг нагрузки
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# 1. Загрузка окружения
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 5666795893  # Твой ID

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- МЕНЮ ---
def main_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="💰 Passive Income", url="https://pawns.app/?r=1139563"))
    builder.row(types.InlineKeyboardButton(text="🎵 Suno AI Hub", callback_data="suno"))
    builder.row(types.InlineKeyboardButton(text="🛡 Статус Системы", callback_data="status"))
    return builder.as_markup()

# --- ОБРАБОТЧИКИ ---
@dp.message(Command("start"))
async def start(message: types.Message):
    # Админ-уведомление
    if message.from_user.id != ADMIN_ID:
        await bot.send_message(ADMIN_ID, f"🔔 Вход: {message.from_user.full_name}")
    
    await message.answer("🦾 **JED СИСТЕМА JD7 АКТИВИРОВАНА**", reply_markup=main_kb())

@dp.callback_query(F.data == "status")
async def check_status(callback: types.CallbackQuery):
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    text = f"🖥 **Статус системы:**\n\n⚙️ CPU: `{cpu}%` \n🧠 RAM: `{ram}%` \n🛰 Состояние: `Оптимально`"
    
    # Кнопка обновления и возврата
    kb = InlineKeyboardBuilder()
    kb.row(types.InlineKeyboardButton(text="🔄 Обновить", callback_data="status"))
    kb.row(types.InlineKeyboardButton(text="⬅️ Назад", callback_data="back"))
    
    await callback.message.edit_text(text, reply_markup=kb.as_markup(), parse_mode="Markdown")

@dp.callback_query(F.data == "back")
async def go_back(callback: types.CallbackQuery):
    await callback.message.edit_text("🦾 **Выберите сектор:**", reply_markup=main_kb())

# --- ЗАПУСК ---
async def main():
    print("🚀 Двигатель JED запущен...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
