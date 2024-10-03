import re

SPECIAL_SYMBOL = "+"
COUNTRY_CODE = "38"
ADDITIONAL_CODE = "0"
REG_EXP = r"[^\d+]"


def normalize_phone(phone_number: str) -> str:
    """
    Normalize a phone number by removing non-numeric characters and ensuring it starts with a specific country code.
    Args:
        phone_number (str): The phone number to be normalized.
    Returns:
        str: The normalized phone number.
    """

    phone_number = re.sub(REG_EXP, "", phone_number).strip()

    if phone_number.startswith(COUNTRY_CODE + ADDITIONAL_CODE):
        phone_number = SPECIAL_SYMBOL + phone_number

    elif not phone_number.startswith(SPECIAL_SYMBOL):
        phone_number = SPECIAL_SYMBOL + COUNTRY_CODE + phone_number

    return phone_number
