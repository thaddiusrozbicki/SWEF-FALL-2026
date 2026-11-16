# Two Sum — scratch file for class
# Problem details: see TWO_SUM.md (same folder)


def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i


print(two_sum([2, 7, 11, 15], 9))  # expect [0, 1]
print(two_sum([3, 2, 4], 6))       # expect [1, 2]
print(two_sum([3, 3], 6))          # expect [0, 1]
