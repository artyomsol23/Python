def find_substring(main_string: str, sub_string: str) -> list[int]:
    len_main, len_sub = len(main_string), len(sub_string)
    
    positions = []
    
    if not sub_string:
        return list(range(len_main + 1))
    
    for i in range(len_main - len_sub + 1):
        match = True
        
        for j in range(len_sub):
            if main_string[i + j] != sub_string[j]:
                match = False
                break
        
        if match:
            positions.append(i)
    
    return positions
