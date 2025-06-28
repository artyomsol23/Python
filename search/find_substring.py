def find_substring(main_string: str, sub_string: str) -> list[int]:
    """
    Находит все вхождения подстроки в строку, используя циклы for.
    
    Параметры:
        main_string (str): Строка, в которой выполняется поиск.
        sub_string (str): Подстрока, которую нужно найти.
    
    Возвращает:
        list[int]: Список индексов, где начинается подстрока.
                  Если подстрока не найдена, возвращает пустой список.

    Примеры:
        >>> find_substring("abacaba", "aba")
        [0, 4]
        >>> find_substring("hello", "ll")
        [2]
        >>> find_substring("abc", "")
        [0, 1, 2, 3]
    """
    # Длина основной строки и длина подстроки
    len_main, len_sub = len(main_string), len(sub_string)
    
    # Список для хранения найденных позиций
    positions = []
    
    # Специальный случай: если подстрока пустая
    if not sub_string:
        # Пустая подстрока считается входящей перед каждым символом и в конце
        return list(range(len_main + 1))
    
    # Проходим только по возможным стартовым позициям подстроки
    for i in range(len_main - len_sub + 1):
        # Флаг, указывающий на полное совпадение
        match = True
        
        # Проверяем посимвольное совпадение подстроки
        for j in range(len_sub):
            if main_string[i + j] != sub_string[j]:
                # Если хотя бы один символ не совпал
                match = False
                break  # Прерываем внутренний цикл
        
        # Если все символы совпали (match остался True)
        if match:
            positions.append(i)  # Добавляем индекс начала подстроки
    
    # Возвращаем список найденных позиций
    return positions
