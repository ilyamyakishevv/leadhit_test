import re 
from datetime import datetime



def email_validation(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))


def phone_validation(phone: str) -> bool:
    pattern = r"^\+7\d{3}\d{3}\d{2}\d{2}$"
    return bool(re.match(pattern, phone))


def date_validation(date: str) -> bool:
    try:
        datetime.strptime(date, "%d.%m.%Y")
        return True
    except ValueError:
            try:
                datetime.strptime(date, "%Y-%m-%d")
                return True
            except ValueError:
                return False


def validate_field_value(field_type: str, value: str) -> bool:
    if field_type == "email":
        return email_validation(value)
    elif field_type == "phone":
        return phone_validation(value)
    elif field_type == "date":
        return date_validation(value)
    else:
        return True