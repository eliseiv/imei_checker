
# (Telegram ID)
WHITELIST = {
    1604863121,  # Мой ID
}


def is_user_allowed(user_id: int) -> bool:
    """
    Проверяет, находится ли пользователь в белом списке.

    :param user_id: ID пользователя Telegram.
    :return: True, если пользователь разрешен, иначе False.
    """
    return user_id in WHITELIST
