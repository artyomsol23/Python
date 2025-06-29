def compute_prefix_function(pattern: str) -> list[int]:
    """Вычисляет префикс-функцию для заданного паттерна.
    
    Args:
        pattern (str): Подстрока, которую ищем.
        
    Returns:
        list[int]: Массив длин наибольших совпадающих префиксов и суффиксов.
    """
    m = len(pattern)
    prefix = [0] * m  # Префикс-функция (изначально заполнена нулями)
    j = 0  # Указатель для сравнения префикса
    
    for i in range(1, m):  # Начинаем с 1, т.к. prefix[0] = 0
        # Пока символы не совпадают, двигаем j назад
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        
        # Если символы совпадают, увеличиваем j
        if pattern[i] == pattern[j]:
            j += 1
            
        prefix[i] = j  # Записываем текущее значение
        
    return prefix


def kmp_search(text: str, pattern: str) -> int:
    """Поиск подстроки в тексте с использованием алгоритма КМП.
    
    Args:
        text (str): Исходный текст.
        pattern (str): Подстрока, которую нужно найти.
        
    Returns:
        int: Начальный индекс найденной подстроки или `-1`, если не найдена.
    """
    n, m = len(text), len(pattern)
    
    if m == 0:
        return 0  # Пустая подстрока считается найденной в начале
    
    prefix = compute_prefix_function(pattern)
    j = 0  # Указатель для паттерна
    
    for i in range(n):
        # Пока не совпадает, возвращаемся по таблице префиксов
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
            
        # Если символы совпадают, двигаемся дальше
        if text[i] == pattern[j]:
            j += 1
            
        # Если дошли до конца паттерна — подстрока найдена
        if j == m:
            return i - j + 1  # Индекс начала подстроки
    
    return -1  # Подстрока не найдена
