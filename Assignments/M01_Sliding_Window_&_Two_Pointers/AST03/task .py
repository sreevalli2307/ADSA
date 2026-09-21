def countGoodSubstrings(s: str) -> int:
    count = 0
    
    # Iterate through all possible starting indices for a 3-character substring
    for i in range(len(s) - 2):
        substring = s[i:i + 3]
        # Check if all 3 characters are distinct
        if len(set(substring)) == 3:
            count += 1

    return count


if __name__ == "__main__":
    s = input().strip()
    print(countGoodSubstrings(s))