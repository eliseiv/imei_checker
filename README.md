IMEI Check Telegram Bot

О проекте

IMEI Check Telegram Bot — это Telegram-бот, позволяющий проверять IMEI или серийные номера устройств через API IMEIcheck. Он возвращает информацию о модели, статусе блокировки, сети и других параметрах.

Как начать работу

Ссылка на бота

@ttest_imei_bot

Добавление вашего ID в белый список

Чтобы бот работал для вас, добавьте ваш Telegram ID в файл whitelist.py:

WHITELIST = {
    1604863121,  # Замените этот ID на ваш собственный
}

Настройка API-ключа

В файле .env укажите ваш API-ключ от IMEIcheck:

TELEGRAM_BOT_TOKEN=your_telegram_token
IMEICHECK_API_KEY=your_api_key

Запуск бота

Убедитесь, что у вас установлен Python 3.8+.

Установите зависимости:

pip install -r requirements.txt

Запустите бота:

python bot.py

Функционал

Отправьте IMEI (15 цифр) или серийный номер (8–14 символов) в чат с ботом.

Бот вернет информацию о устройстве, например:

Результат проверки:
- Название устройства: iPhone 11 Pro
- IMEI: 123456789012345
- Статус блокировки: Clean
- Сеть: Global

Контакты

Если у вас возникнут вопросы или проблемы, свяжитесь со мной:

Email: your_email@example.com

Telegram: @your_username

