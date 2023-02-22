import string

import django.core.exceptions


def luxury_words_validator(value: str):
    for symbol in string.punctuation:
        value = value.replace(symbol, ' ')
    value = value.split()
    luxury_word_founded = False
    for word in value:
        if 'превосходно' == word.lower() or 'роскошно' == word.lower():
            luxury_word_founded = True
            break
    if not luxury_word_founded:
        raise django.core.exceptions.ValidationError(
            'В тексте должны быть слова "превосходно" или "роскошно"'
        )
