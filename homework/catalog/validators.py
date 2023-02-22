import string

import django.core.exceptions


class ValidateMustContain:
    def __init__(self, *words):
        self.words = words

    def __call__(self, value):
        for symbol in string.punctuation:
            value = value.replace(symbol, ' ')

        value = value.split()
        luxury_word_founded = False
        for word in value:
            for must_contain_word in self.words:
                if must_contain_word == word.lower():
                    luxury_word_founded = True
                    break
            if luxury_word_founded:
                break
        if not luxury_word_founded:
            raise django.core.exceptions.ValidationError(
                'В тексте должны быть слова "превосходно" или "роскошно"'
            )