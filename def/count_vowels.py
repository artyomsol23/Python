def count_vowels(text: str):
    vowels = "aeiouаеёиоуыэюя"
    
    return sum(1 for char in text.lower() if char in vowels)
