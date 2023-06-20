def solution(s):
    return ''.join(chr(219 - ord(c)) if 'a' <= c <= 'z' else c for c in s)