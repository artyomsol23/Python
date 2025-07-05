def count_vowels(text: str) -> int:
    vowels = "aeiouаеёиоуыэюя"
    
    return sum(1 for char in text.lower() if char in vowels)
