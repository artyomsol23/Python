def caesar_cipher(text, shift, mode='encrypt'):
    """
    Функция для шифрования и дешифрования текста с использованием шифра Цезаря.
    
    :param text: Исходный текст для преобразования (str)
    :param shift: Величина сдвига алфавита (int)
    :param mode: Режим работы: 'encrypt' - шифрование, 'decrypt' - дешифрование (str)
    :return: Преобразованный текст (str)
    """
    result = ""
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char
    
    return result
