def Check_Palindrome(n: int, s: str) -> bool:
    # Check if original string is already a palindrome
    if s == s[::-1]:
        return True

    # Try deleting each character one by one
    for i in range(n):
        t = s[:i] + s[i+1:]
        if t == t[::-1]:
            return True

    return False


if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    print(Check_Palindrome(n, s))