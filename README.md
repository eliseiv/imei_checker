IMEI Check Telegram Bot
Этот Telegram-бот позволяет проверять IMEI или серийные номера устройств через API IMEIcheck. Он возвращает информацию о модели, статусе блокировки, сети и других параметрах.

Как начать работу
Ссылка на бота :
@ttest_imei_bot
Добавление вашего ID в белый список :
Чтобы бот работал для вас, добавьте ваш Telegram ID в файл whitelist.py:
python
Copy
1
2
3
⌄
WHITELIST = {
    1604863121,  # Замените этот ID на ваш собственный
}
Настройка API-ключа :
В файле .env укажите ваш API-ключ от IMEIcheck:
plaintext
Copy
1
2
TELEGRAM_BOT_TOKEN=ваш_telegram_token
IMEICHECK_API_KEY=ваш_api_key
Запуск бота :
Убедитесь, что у вас установлен Python 3.8+.
Установите зависимости:
bash
Copy
1
pip install -r requirements.txt
Запустите бота:
bash
Copy
1
python bot.py
Функционал
Отправьте IMEI (15 цифр) или серийный номер (8–14 символов) в чат с ботом.
Бот вернет информацию о устройстве, например:
Copy
1
2
3
4
5
Результат проверки:
- Название устройства: iPhone 11 Pro
- IMEI: 123456789012345
- Статус блокировки: Clean
- Сеть: Global
