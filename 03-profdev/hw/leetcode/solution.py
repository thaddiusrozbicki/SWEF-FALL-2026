# Longest Substring Without Repeating Characters
# Full problem: see ../README.md Part 3
# Run: python3 solution.py


def length_of_longest_substring(s):
    seen, left, best = {}, 0, 0
    for right, c in enumerate(s):
        if seen.get(c, -1) >= left:
            left = seen[c] + 1
        seen[c] = right
        best = max(best, right - left + 1)
    return best


print(length_of_longest_substring("abcabcbb"))  # 3
print(length_of_longest_substring("bbbbb"))     # 1
print(length_of_longest_substring("pwwkew"))    # 3