from django.core.exceptions import ValidationError
import re

def validate_iran_phone_number(value):
    """
    تابع اعتبارسنجی شماره همراه ایران
    """
    iran_phone_regex = r'^09\d{9}$'
    if not re.match(iran_phone_regex, value):
        raise ValidationError(
            'Enter a valid Iranian cellphone number.'
        )