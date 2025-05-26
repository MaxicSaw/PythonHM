import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_dir = "..\\logs"
log_file_path = os.path.join(log_dir, "masks.log")
file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def mask_card(card_number: str) -> str | None:
    """
    Маскирует номер банковской карты, оставляя видимыми только первые 4 и последние 4 цифры.
    Логирует действия и предупреждения.

    Args:
        card_number: Номер банковской карты в виде строки.

    Returns:
        Маскированный номер карты в виде строки.
        Пример: "1234 **** **** 5678"
    """
    if card_number is None:
        logger.warning("В mask_card передан None, возвращается None")
        return None
    if len(card_number) < 8:
        logger.warning(
            f"В mask_card передан номер карты короче 8 символов: {card_number}.  Возвращается без маскирования."
        )
        return card_number  # Or raise ValueError, depending on desired behavior

    masked_card = f"{card_number[:4]} **** **** {card_number[-4:]}"
    logger.debug(f"Номер карты замаскирован: {card_number} -> {masked_card}")
    return masked_card


def mask_account(account_number: str) -> str | None:
    """
    Маскирует номер банковского счета, оставляя видимыми только последние 4 цифры.
    Логирует действия и предупреждения.

    Args:
            account_number: Номер банковского счета в виде строки.

    Returns:
            Маскированный номер счета в виде строки.
            Пример: "****5678"
        """
    if account_number is None:
        logger.warning("В mask_account передан None, возвращается None")
        return None
    if len(account_number) < 4:
        logger.warning(
            f"В mask_account передан номер счета короче 4 символов: {account_number}. Возвращается без маскирования."
        )
        return account_number  # Or raise ValueError, depending on desired behavior

    masked_account = f"****{account_number[-4:]}"
    logger.debug(f"Номер счета замаскирован: {account_number} -> {masked_account}")
    return masked_account
