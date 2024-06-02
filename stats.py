from collections import Counter

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def mode(numbers):
    counter = Counter(numbers)
    max_count = max(counter.values())
    modes = [k for k, v in counter.items() if v == max_count]
    return modes

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
print(f"Mean: {mean(numbers)}")
print(f"Median: {median(numbers)}")
print(f"Mode: {mode(numbers)}")
