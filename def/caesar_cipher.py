def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':  # 'encrypt' - шифрование, 'decrypt' - дешифрование
        shift = -shift
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char
    
    return result
