from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from api_handler import check_imei, get_services
from whitelist import is_user_allowed

# Словарь для хранения выбранного сервиса
SERVICE_IDS = {
    "mock_success": 12,  # Всегда успешный результат
    "mock_unsuccess": 13,  # 10% ошибок
    "mock_fail": 14,  # Всегда ошибка
    "mock_mixed": 15  # Смешанные результаты
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Команда /start.
    """
    if not is_user_allowed(update.effective_user.id):
        await update.message.reply_text("Извините, у вас нет доступа к этому боту.")
        return
    await update.message.reply_text(
        "Привет! Я бот для проверки IMEI устройств.\n"
        "Чтобы начать, отправьте IMEI устройства.\n"
        "Для просмотра доступных сервисов используйте команду /services.\n"
        "Для выбора сервиса используйте команду /set_service."
    )


async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Команда /services.
    """
    if not is_user_allowed(update.effective_user.id):
        await update.message.reply_text("Извините, у вас нет доступа к этому боту.")
        return
    response = get_services()
    await update.message.reply_text(f"Доступные сервисы:\n{response}")


async def set_service(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Команда /set_service.
    """
    if not is_user_allowed(update.effective_user.id):
        await update.message.reply_text("Извините, у вас нет доступа к этому боту.")
        return
    try:
        service_name = update.message.text.split()[1].lower()
        if service_name in SERVICE_IDS:
            context.user_data["service_id"] = SERVICE_IDS[service_name]
            await update.message.reply_text(f"Выбран сервис: {service_name.capitalize()}")
        else:
            await update.message.reply_text(
                "Неверное название сервиса. Доступные: mock_success, mock_unsuccess, mock_fail, mock_mixed."
            )
    except IndexError:
        await update.message.reply_text(
            "Укажите название сервиса. Пример: /set_service mock_success"
        )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обработка текстовых сообщений.
    """
    if not is_user_allowed(update.effective_user.id):
        await update.message.reply_text("Извините, у вас нет доступа к этому боту.")
        return

    user_input = update.message.text.strip()

    # Проверка формата IMEI
    if len(user_input) < 8 or len(user_input) > 15 or not user_input.isdigit():
        await update.message.reply_text("Неверный формат IMEI. Пожалуйста, отправьте от 8 до 15 цифр.")
        return

    # Выбор сервиса (по умолчанию 12)
    service_id = context.user_data.get("service_id", 12)

    # Вызов функции проверки IMEI
    response = check_imei(user_input, service_id)
    await update.message.reply_text(response)

if __name__ == "__main__":
    from dotenv import load_dotenv
    import os

    load_dotenv()
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("services", services))
    app.add_handler(CommandHandler("set_service", set_service))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()
