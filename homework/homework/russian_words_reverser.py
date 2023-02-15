def reverse_russian_words(text):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result, word = '', ''
    for symbol in text:
        if symbol.lower() not in alphabet:
            if word:
                result += word[::-1]
                word = ''
            result += symbol
        else:
            word += symbol
    result += word[::-1]
    return result
