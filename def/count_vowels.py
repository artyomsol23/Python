def count_vowels(s):
    vowels = "aeiouаеёиоуыэюя"  # Русские и английские гласные
    return sum(1 for char in s.lower() if char in vowels)

text = "Hello, World! Привет, мир!"
print("Количество гласных:", count_vowels(text))  # 7
