def caesar_cipher(text, shift, mode='encrypt'):
    """
    Функция для шифрования и дешифрования текста с помощью шифра Цезаря.
    
    :param text: исходный текст
    :param shift: величина сдвига
    :param mode: 'encrypt' для шифрования, 'decrypt' для дешифрования
    :return: преобразованный текст
    """
    result = ""
    
    if mode == 'decrypt':  # Если режим дешифрования, меняем направление сдвига
        shift = -shift
    
    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            base = ord('A') if char.isupper() else ord('a')  # Определяем базовый код для верхнего или нижнего регистра
            new_char = chr((ord(char) - base + shift) % 26 + base)  # Вычисляем новый символ с учетом сдвига
            result += new_char
        else:  # Не-алфавитные символы добавляем без изменений
            result += char
    
    return result
