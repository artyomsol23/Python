def is_palindrome(s: str):
    s = s.lower().replace(" ", "")
    
    return s == s[::-1]
