def compute_prefix_function(pattern: str) -> list[int]:
    m = len(pattern)
    prefix = [0] * m
    j = 0
    
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1
            
        prefix[i] = j
        
    return prefix


def kmp_search(text: str, pattern: str) -> int:
    n, m = len(text), len(pattern)
    
    if m == 0:
        return 0
    
    prefix = compute_prefix_function(pattern)
    j = 0
    
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
            
        if text[i] == pattern[j]:
            j += 1
        
        if j == m:
            return i - j + 1
    
    return -1
