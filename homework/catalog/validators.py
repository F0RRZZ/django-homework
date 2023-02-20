import django.core.exceptions


def luxury_words_validator(value: str):
    if 'превосходн' not in value.lower() and 'роскошн' not in value.lower():
        raise django.core.exceptions.ValidationError(
            'В тексте должны быть слова "превосходно" или "роскошно"'
        )
