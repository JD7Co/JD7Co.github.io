import os
import psutil
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
# И обязательно:
from aiogram.utils.keyboard import InlineKeyboardBuilder 

        logger.info(f"✅ Бот подключен: @{me.username}")
        logger.info(f"✅ ID бота: {me.id}")
        logger.info(f"✅ Имя: {me.first_name}")
        logger.info("=" * 50)
        logger.info("🟢 Бот ожидает сообщений...")
        logger.info("=" * 50)

        await bot.delete_webhook(drop_pending_updates=True)
        
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
