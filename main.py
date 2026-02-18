import logging
import os
from typing import Optional
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramAPIError

# ============ КОНФИГУРАЦИЯ ============
TOKEN = os.getenv("BOT_TOKEN", "ТВОЙ_ТОКЕН_ЗДЕСЬ")

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# ============ КЛАВИАТУРЫ ============

def main_menu() -> types.InlineKeyboardMarkup:
    """Главное меню JD7"""
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="🎵 Suno AI Music", callback_data="suno_hub"))
    builder.row(types.InlineKeyboardButton(text="📈 VIP Trading", callback_data="trade_hub"))
    builder.row(types.InlineKeyboardButton(text="💰 Passive (Pawns.app)", callback_data="pawns_hub"))
    builder.row(types.InlineKeyboardButton(text="💎 My $JD7 Wallet", callback_data="wallet_jd7"))
    builder.row(types.InlineKeyboardButton(text="📜 NDA & Privacy", callback_data="legal_info"))
    return builder.as_markup()

def back_menu() -> types.InlineKeyboardMarkup:
    """Меню с кнопкой 'Назад'"""
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back_to_menu"))
    return builder.as_markup()

def suno_menu() -> types.InlineKeyboardMarkup:
    """Меню Suno AI Music"""
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="🎧 Создать трек", callback_data="suno_create"))
    builder.row(types.InlineKeyboardButton(text="📊 Мои треки", callback_data="suno_tracks"))
    builder.row(types.InlineKeyboardButton(text="💡 Советы и примеры", callback_data="suno_tips"))
    builder.row(types.InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_menu"))
    return builder.as_markup()

def trading_menu() -> types.InlineKeyboardMarkup:
    """Меню VIP Trading"""
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="📉 Анализ рынка", callback_data="trade_analysis"))
    builder.row(types.InlineKeyboardButton(text="🎯 Сигналы", callback_data="trade_signals"))
    builder.row(types.InlineKeyboardButton(text="👥 Присоединиться к VIP", callback_data="trade_vip"))
    builder.row(types.InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_menu"))
    return builder.as_markup()

def wallet_menu() -> types.InlineKeyboardMarkup:
    """Меню кошелька"""
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="💸 Баланс", callback_data="wallet_balance"))
    builder.row(types.InlineKeyboardButton(text="📤 Вывести средства", callback_data="wallet_withdraw"))
    builder.row(types.InlineKeyboardButton(text="📥 Пополнить", callback_data="wallet_deposit"))
    builder.row(types.InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_menu"))
    return builder.as_markup()

# ============ ОБРАБОТЧИКИ КОМАНД ============

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    try:
        user_id = message.from_user.id
        username = message.from_user.username or "Аноним"
        
        logger.info(f"Пользователь {user_id} (@{username}) запустил бота")
        
        await message.answer(
            f"🤖 **JED AI System v1.0 Activated.**\n\n"
            f"Добро пожаловать в экосистему **JDmitrijs7®**.\n"
            f"Ваш ID: `{user_id}`\n"
            f"Ваш статус: Начинающий Архитектор\n"
            f"Powered Index: 0%\n"
            f"Время входа: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            f"Выберите модуль для управления:",
            reply_markup=main_menu(),
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"Ошибка в обработчике /start: {e}")
        await message.answer("❌ Произошла ошибка. Попробуйте позже.")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    """Обработчик команды /help"""
    try:
        await message.answer(
            "📖 **Справка по JD7 System**\n\n"
            "**Доступные команды:**\n"
            "/start - Запустить бота\n"
            "/help - Показать эту справку\n"
            "/status - Проверить статус\n\n"
            "**Модули:**\n"
            "🎵 Suno AI Music - Создание музыки на ИИ\n"
            "📈 VIP Trading - Торговля криптовалютой\n"
            "💰 Passive Income - Пассивный заработок\n"
            "💎 JD7 Wallet - Управление кошельком\n"
            "📜 NDA & Privacy - Юридическая информация",
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"Ошибка в обработчике /help: {e}")
        await message.answer("❌ Произошла ошибка.")

@dp.message(Command("status"))
async def cmd_status(message: types.Message):
    """Проверка статуса системы"""
    try:
        await message.answer(
            f"✅ **JD7 System Status**\n\n"
            f"Статус: Online\n"
            f"Версия: 1.0\n"
            f"Время ответа: {datetime.now().strftime('%H:%M:%S')}\n"
            f"Пользователи: Активны",
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"Ошибка в обработчике /status: {e}")
        await message.answer("❌ Произошла ошибка.")

# ============ ОБРАБОТЧИКИ CALLBACK (ГЛАВНОЕ МЕНЮ) ============

@dp.callback_query(F.data == "back_to_menu")
async def back_to_main_menu(callback: types.CallbackQuery):
    """Возврат в главное меню"""
    try:
        await callback.message.edit_text(
            f"🤖 **JED AI System v1.0**\n\n"
            f"Добро пожаловать в экосистему **JDmitrijs7®**.\n"
            f"Ваш статус: Начинающий Архитектор\n"
            f"Powered Index: 0%\n\n"
            f"Выберите модуль для управления:",
            reply_markup=main_menu(),
            parse_mode="Markdown"
        )
        await callback.answer("↩️ Вернулись в главное меню", show_alert=False)
    except Exception as e:
        logger.error(f"Ошибка при возврате в меню: {e}")
        await callback.answer("❌ Ошибка", show_alert=True)

# ============ SUNO AI MUSIC ============

@dp.callback_query(F.data == "suno_hub")
async def process_suno(callback: types.CallbackQuery):
    """Обработчик кнопки Suno AI Music"""
    try:
        await callback.message.edit_text(
            "🎵 **Suno AI Music Generator**\n\n"
            "Создавайте уникальную музыку с помощью ИИ!\n\n"
            "Особенности:\n"
            "• 🎼 Автоматическая генерация музыки\n"
            "• 🎯 Выбор жанра и стиля\n"
            "• 📊 Анализ популярности\n"
            "• 💾 Сохранение в библиотеку\n\n"
            "Выберите действие:",
            reply_markup=suno_menu(),
            parse_mode="Markdown"
        )
        await callback.answer("🎵 Открыт модуль Suno AI Music", show_alert=False)
    except Exception as e:
        logger.error(f"Ошибка в Suno Hub: {e}")
        await callback.answer("❌ Ошибка", show_alert=True)

@dp.callback_query(F.data == "suno_create")
async def suno_create(callback: types.CallbackQuery):
    """Создание нового трека"""
    try:
        await callback.message.edit_text(
            "🎧 **Создание нового трека**\n\n"
            "Отправьте описание трека (жанр, стиль, настроение):\n\n"
            "Пример: 'Электронная музыка, энергичная, для спортзала'\n\n"
            "Или используйте готовые шаблоны ниже:",
            reply_markup=suno_menu(),
            parse_mode="Markdown"
        )
        logger.info("Пользователь начал создание трека в Suno")
    except Exception as e:
        logger.error(f"Ошибка при создании трека: {e}")
        await callback.answer("❌ Ошибка", show_alert=True)

@dp.callback_query(F.data == "suno_tracks")
async def suno_tracks(callback: types.CallbackQuery):
    """Просмотр созданных треков"""
    try:
        await callback.message.edit_text(
            "📊 **Ваши треки**\n\n"
            "У вас еще нет созданных треков.\n\n"
            "Нажмите '🎧 Создать трек' для начала!",
            reply_markup=suno_menu(),
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"Ошибка при загрузке треков: {e}")
        await callback.answer("❌ Ошибка", show_alert=True)

@dp.callback_query(F.data == "suno_tips")
async def suno_tips(callback: types.CallbackQuery):
    """Советы по использованию"""
    try:
        await callback.message.edit_text(
            "💡 **Советы и примеры**\n\n"
            "**Лучшие практики:**\n"
            "1️⃣ Будьте специфичны в описании\n"
            "2️⃣ Укажите темп (BPM)\n"
            "3️⃣ Упомяните инструменты\n"
            "4️⃣ Опишите эмоции трека\n\n"
            "**Примеры успешных описаний:**\n"
            "• 'Lo-fi Hip Hop, 90 BPM, расслабляющая атмосфера'\n"
            "• 'Синтвейв, 120 BPM, ретро-фьючеристический стиль'\n"
            "• 'Электро-поп, веселая и энергичная'",
            reply_markup=suno_menu(),
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"Ошибка при показе советов: {e}")
        await callback.answer("❌ Ошибка", show_alert=True)

# ============ VIP TRADING ============

@dp.callback_query(F.data == "trade_hub")
async def process_trading(callback: types.CallbackQuery):
    """Обработчик кнопки VIP Trading"""
    try:
        await callback.message.edit_text(
            "📈 **VIP Trading Platform**\n\n"
            "Профессиональная торговля криптовалютой\n\n"
            "Преимущества VIP:\n"
            "📊 Аналитика в реальном времени\n"
            "🎯 Точные торговые сигналы\n"
            "💰 До 300% прибыли (честная работа)\n"
            "👥 Закрытое сообщество трейдеров\n"
            "📚 Обучающие материалы\n\n"
            "Выберите действие:",
            reply_markup=trading_menu(),
            parse_mode="Markdown"
        )
        await callback.answer("📈 Открыт модуль VIP Trading", show_alert=False)
    except Exception as e:
        logger.error(f"Ошибка в Trade Hub: {e}")
        await callback.answer("❌ Ошибка", show_alert=True)

@dp.callback_query(F.data == "trade_analysis")
async def trade_analysis(callback: types.CallbackQuery):
    """Анализ рынка"""
    try:
        await callback.message.edit_text(
            "📉 **Анализ рынка**\n\n"
            "Текущие данные:\n"
            "BTC: $45,230 📈 +2.5%\n"
            "ETH: $2,850 📈 +1.8%\n"
            "BNB: $620 📉 -0.5%\n\n"
            "Рекомендация: HOLD\n"
            "Риск: СРЕДНИЙ",
            reply_markup=trading_menu(),
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"Ошибка при анализе: {e}")
        await callback.answer("❌ Ошибка", show_alert=True)

@dp.callback_query(F.data == "trade_signals")
async def trade_signals(callback: types.CallbackQuery):
    """Торговые сигналы"""
    try:
        await callback.message.edit_text(
            "🎯 **Торговые сигналы**\n\n"
            "Последние сигналы:\n\n"
            "🟢 BTC/USDT: BUY @ 45,000\n"
            "TP: 46,500 | SL: 44,000\n\n"
            "🟡 ETH/USDT: HOLD\n"
            "Ожидание подтверждения\n\n"
            "Точность: 78%",
            reply_markup=trading_menu(),
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"Ошибка при загрузке сигналов: {e}")
        await callback.answer("❌ Ошибка", show_alert=True)

@dp.callback_query(F.data == "trade_vip")
async def trade_vip(callback: types.CallbackQuery):
    """Присоединиться к VIP"""
    try:
        await callback.message.edit_text(
            "👥 **Присоединиться к VIP**\n\n"
            "Стоимость подписки:\n"
            "• 1 месяц: $99\n"
            "• 3 месяца: $249 (скидка 16%)\n"
            "• 6 месяцев: $449 (скидка 25%)\n\n"
            "В пакет входит:\n"
            "✅ Ежедневные сигналы\n"
            "✅ Приватный канал\n"
            "✅ Консультации\n"
            "✅ Поддержка 24/7\n\n"
            "Для подписки свяжитесь с менеджером.",
            reply_markup=trading_menu(),
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"Ошибка при подписке на VIP: {e}")
        await callback.answer("❌ Ошибка", show_alert=True)

# ============ PASSIVE INCOME (PAWNS) ============

@dp.callback_query(F.data == "pawns_hub")
async def process_pawns(callback: types.CallbackQuery):
    """Пассивный доход через Pawns.app"""
    try:
        await callback.message.edit_text(
            "🛰 **JD7® Traffic Monetization (Pawns.app)**\n\n"
            "Превращайте трафик в деньги!\n\n"
            "Как это работает:\n"
            "1️⃣ Установите приложение\n"
            "2️⃣ Поделитесь своим интернетом\n"
            "3️⃣ Получайте $0.10 - $0.50 за ГБ\n"
            "4️⃣ Выводите прибыль\n\n"
            "Ваша реферальная ссылка:\n"
            "`https://pawns.app/?r=1139563`\n\n"
            "Статус: ✅ Активно",
            reply_markup=back_menu(),
            parse_mode="Markdown"
        )
        await callback.answer("💰 Открыт модуль Passive Income", show_alert=False)
    except Exception as e:
        logger.error(f"Ошибка в Pawns Hub: {e}")
        await callback.answer("❌ Ошибка", show_alert=True)

# ============ WALLET ============

@dp.callback_query(F.data == "wallet_jd7")
async def process_wallet(callback: types.CallbackQuery):
    """Открытие кошелька"""
    try:
        await callback.message.edit_text(
            "💎 **My $JD7 Wallet**\n\n"
            "Управляйте своими средствами\n\n"
            "📊 Статистика:\n"
            "Общий баланс: $0.00\n"
            "Доступно к выводу: $0.00\n"
            "В ожидании: $0.00\n\n"
            "Последние операции:\n"
            "Нет операций\n\n"
            "Выберите действие:",
            reply_markup=wallet_menu(),
            parse_mode="Markdown"
        )
        await callback.answer("💎 Открыт кошелек", show_alert=False)
    except Exception as e:
        logger.error(f"Ошибка при открытии кошелька: {e}")
        await callback.answer("❌ Ошибка", show_alert=True)

@dp.callback_query(F.data == "wallet_balance")
async def wallet_balance(callback: types.CallbackQuery):
    """Проверка баланса"""
    try:
        await callback.message.edit_text(
            "💸 **Баланс кошелька**\n\n"
            "Основной счет: $0.00\n"
            "Бонусы: $0.00\n"
            "Рефбонусы: $0.00\n\n"
            "Сумма в обработке: $0.00\n"
            "Статус: ✅ Верифицирован",
            reply_markup=wallet_menu(),
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"Ошибка при проверке баланса: {e}")
        await callback.answer("❌ Ошибка", show_alert=True)

@dp.callback_query(F.data == "wallet_withdraw")
async def wallet_withdraw(callback: types.CallbackQuery):
    """Вывод средств"""
    try:
        await callback.message.edit_text(
            "📤 **Вывод средств**\n\n"
            "Доступные методы:\n"
            "💳 Банковская карта\n"
            "💰 Криптовалюта (BTC, ETH)\n"
            "📲 PayPal\n"
            "🏦 Перевод на счет\n\n"
            "Минимальный вывод: $10\n"
            "Комиссия: 2%\n\n"
            "Для вывода свяжитесь с поддержкой.",
            reply_markup=wallet_menu(),
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"Ошибка при выводе: {e}")
        await callback.answer("❌ Ошибка", show_alert=True)

@dp.callback_query(F.data == "wallet_deposit")
async def wallet_deposit(callback: types.CallbackQuery):
    """Пополнение счета"""
    try:
        await callback.message.edit_text(
            "📥 **Пополнение счета**\n\n"
            "Способы пополнения:\n"
            "💳 Банковская карта Visa/Mastercard\n"
            "💰 Криптовалюта (BTC, ETH, USDT)\n"
            "📲 PayPal\n"
            "💸 Сбербанк/Яндекс.Касса\n\n"
            "Минимальное пополнение: $5\n"
            "Комиссия: 0-1%\n\n"
            "Деньги поступают мгновенно!",
            reply_markup=wallet_menu(),
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"Ошибка при пополнении: {e}")
        await callback.answer("❌ Ошибка", show_alert=True)

# ============ LEGAL INFO ============

@dp.callback_query(F.data == "legal_info")
async def process_legal(callback: types.CallbackQuery):
    """NDA и информация о приватности"""
    try:
        await callback.message.edit_text(
            "📜 **NDA & Privacy Policy**\n\n"
            "**Конфиденциальность:**\n"
            "Все ваши данные защищены шифрованием\n"
            "Мы не передаем информацию третьим лицам\n"
            "Используются SSL сертификаты\n\n"
            "**Соглашение об использовании:**\n"
            "✅ Возраст 18+\n"
            "✅ Запрещена автоматизация\n"
            "✅ Запрещена перепродажа\n"
            "✅ Запрещена реклама\n\n"
            "**Контакты поддержки:**\n"
            "📧 support@jd7.com\n"
            "🤖 Чат поддержки в боте\n\n"
            "Полный текст: [Прочитать документ]",
            reply_markup=back_menu(),
            parse_mode="Markdown"
        )
        await callback.answer("📜 Открыта информация о приватности", show_alert=False)
    except Exception as e:
        logger.error(f"Ошибка при открытии юридической информации: {e}")
        await callback.answer("❌ Ошибка", show_alert=True)

# ============ ОБРАБОТКА ОШИБОК ============

@dp.callback_query()
async def unknown_callback(callback: types.CallbackQuery):
    """Обработчик неизвестных callback"""
    try:
        logger.warning(f"Неизвестный callback: {callback.data}")
        await callback.answer("❌ Неизвестная команда", show_alert=True)
    except Exception as e:
        logger.error(f"Ошибка при обработке callback: {e}")

@dp.message()
async def unknown_message(message: types.Message):
    """Обработчик неизвестных сообщений"""
    try:
        logger.info(f"Неизвестное сообщение: {message.text}")
        await message.answer(
            "❓ Неизвестная команда.\n\n"
            "Используйте меню ниже или введите:\n"
            "/start - Главное меню\n"
            "/help - Справка\n"
            "/status - Статус",
            reply_markup=main_menu()
        )
    except Exception as e:
        logger.error(f"Ошибка при обработке сообщения: {e}")

# ============ ЗАПУСК БОТА ============

async def main():
    """Главная функция запуска"""
    try:
        logger.info("🤖 JD7 Bot запущен...")
        logger.info(f"Токен загружен: {TOKEN[:10]}...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
