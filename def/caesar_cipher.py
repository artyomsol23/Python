def caesar_cipher(text, shift, mode='encrypt'):
    """
    Функция для шифрования и дешифрования текста с использованием шифра Цезаря.
    
    :param text: Исходный текст для преобразования (str)
    :param shift: Величина сдвига алфавита (int)
    :param mode: Режим работы: 'encrypt' - шифрование, 'decrypt' - дешифрование (str)
    :return: Преобразованный текст (str)
    """
    result = ""
    
    # Если режим дешифрования, инвертируем сдвиг
    if mode == 'decrypt':
        shift = -shift
    
    # Проходим по каждому символу в тексте
    for char in text:
        # Обрабатываем только буквенные символы
        if char.isalpha():
            # Определяем базовый код ASCII для регистра (верхний/нижний)
            base = ord('A') if char.isupper() else ord('a')
            # Вычисляем новый символ со сдвигом (с учетом закольцованности алфавита)
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            # Не-буквенные символы добавляем без изменений
            result += char
    
    return result
