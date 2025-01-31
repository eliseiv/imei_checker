[RU]

# IMEI Check Telegram Bot

## О проекте
IMEI Check Telegram Bot — это Telegram-бот, позволяющий проверять IMEI или серийные номера устройств через API IMEIcheck. Он возвращает информацию о модели, статусе блокировки, сети и других параметрах.

## Как начать работу

### Ссылка на бота
[@ttest_imei_bot](https://t.me/ttest_imei_bot)

### Добавление вашего ID в белый список
Чтобы бот работал для вас, добавьте ваш Telegram ID в файл `whitelist.py`:

```python
WHITELIST = {
    1604863121,  # Замените этот ID на ваш собственный
}
```

### Настройка API-ключа
В файле `.env` укажите ваш API-ключ от IMEIcheck:

```plaintext
TELEGRAM_BOT_TOKEN=your_telegram_token
IMEICHECK_API_KEY=your_api_key
```

### Запуск бота
1. Убедитесь, что у вас установлен Python 3.8+.
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Запустите бота:
   ```bash
   python bot.py
   ```

## Функционал
- Отправьте IMEI (15 цифр) или серийный номер (8–14 символов) в чат с ботом.
- В тестовой версии работает только 356735111052198
- Бот вернет информацию о устройстве, например:
  ```
  Результат проверки:
  - Название устройства: iPhone 11 Pro
  - IMEI: 123456789012345
  - Статус блокировки: Clean
  - Сеть: Global
  ```

[EN}

# IMEI Check Telegram Bot

## About the Project
IMEI Check Telegram Bot is a Telegram bot that allows you to check IMEI or serial numbers of devices via the IMEIcheck API. It returns information about the device model, lock status, network, and other parameters.

## Getting Started

### Bot Link
[@ttest_imei_bot](https://t.me/ttest_imei_bot)

### Adding Your ID to the Whitelist
To allow the bot to work for you, add your Telegram ID to the `whitelist.py` file:

```python
WHITELIST = {
    1604863121,  # Replace this ID with your own
}
```

### Setting Up the API Key
In the `.env` file, specify your IMEIcheck API key:

```plaintext
TELEGRAM_BOT_TOKEN=your_telegram_token
IMEICHECK_API_KEY=your_api_key
```

### Running the Bot
1. Ensure you have Python 3.8+ installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the bot:
   ```bash
   python bot.py
   ```

## Features
- Send an IMEI (15 digits) or serial number (8–14 characters) to the bot.
- In test version only 356735111052198 aviable
- The bot will return device information, for example:
  ```
  Check Results:
  - Device Name: iPhone 11 Pro
  - IMEI: 123456789012345
  - Block Status: Clean
  - Network: Global
  ```
