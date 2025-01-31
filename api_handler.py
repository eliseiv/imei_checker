import requests
import logging
from dotenv import load_dotenv
import os

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Загрузка переменных окружения
load_dotenv()
IMEICHECK_API_KEY = os.getenv("IMEICHECK_API_KEY")


def get_services():
    """
    Получает список доступных сервисов через API IMEIcheck.
    :return: Список сервисов в виде строки.
    """
    url = "https://api.imeicheck.net/v1/services"
    headers = {
        "Authorization": f"Bearer {IMEICHECK_API_KEY}",
        "Content-Type": "application/json",
        "Accept-Language": "en"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        services = response.json()
        return "\n".join([f"{s['id']}: {s['title']} (Price: ${s['price']})" for s in services])
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP ошибка: {http_err}"
    except requests.exceptions.RequestException as e:
        return f"Ошибка при получении сервисов: {str(e)}"


def check_imei(imei: str, service_id: int = 12) -> str:
    """
    Проверяет IMEI через API IMEIcheck.

    :param imei: IMEI устройства (строка из 8–15 цифр).
    :param service_id: ID сервиса для проверки (по умолчанию 12 - моковый сервис).
    :return: Результат проверки в виде строки.
    """
    # Проверка формата IMEI
    if len(imei) < 8 or len(imei) > 15 or not imei.isdigit():
        return "Неверный формат IMEI. Пожалуйста, отправьте от 8 до 15 цифр."

    url = "https://api.imeicheck.net/v1/checks"
    headers = {
        "Authorization": f"Bearer {IMEICHECK_API_KEY}",
        "Content-Type": "application/json",
        "Accept-Language": "en"
    }
    body = {
        "deviceId": imei,
        "serviceId": service_id,
        "type": "sandbox"
    }

    logging.info(
        f"Отправка запроса: URL={
            url}, Headers={headers}, Body={body}"
    )

    try:
        response = requests.post(url, headers=headers, json=body, timeout=10)
        logging.info(
            f"Получен ответ: Status Code={
                response.status_code}, Body={response.text}"
        )

        if response.status_code == 201:
            result = response.json()
            properties = result.get("properties", {})
            formatted_result = (
                f"Результат проверки:\n"
                f"- Название устройства: {
                    properties.get('deviceName', 'N/A')}\n"
                f"- IMEI: {properties.get('imei', 'N/A')}\n"
                f"- Модель: {properties.get('modelDesc', 'N/A')}\n"
                f"- Статус блокировки: {
                    properties.get('usaBlockStatus', 'N/A')}\n"
                f"- Сеть: {properties.get('network', 'N/A')}\n"
            )
            return formatted_result
        elif response.status_code == 422:
            error_details = response.json()
            logging.error(f"Ошибка валидации данных: {error_details}")
            errors = error_details.get("errors", {})
            if "deviceId" in errors:
                return f"Недопустимый IMEI: {errors['deviceId'][0]}"
            else:
                return f"Ошибка валидации данных: {error_details.get('message', 'Неизвестная ошибка')}"
        else:
            response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP ошибка: {http_err}"
    except requests.exceptions.RequestException as e:
        return f"Ошибка при проверке IMEI: {str(e)}"
