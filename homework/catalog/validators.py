import django.core.exceptions


def luxury_words_validator(value: str):
    if 'превосходн' not in value.lower() and 'роскошн' not in value.lower():
        raise django.core.exceptions.ValidationError(
            'В тексте должны быть слова "превосходно" или "роскошно"'
        )


def words_count_validator(value: str):
    if len(value.split()) <= 2:
        raise django.core.exceptions.ValidationError(
            'В тексте должно быть больше 2-х слов'
        )
