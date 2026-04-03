# Bincom Python Test Submission
# Name: Divine Chukwu
# Language: Python 3

"""
NOTE:
- Colors were extracted from provided HTML.
- Mean color interpreted as most frequent (mode).
- Median calculated from sorted list.
"""

import random
from collections import Counter

# Extracted colors from HTML (cleaned obvious typos: BLEW->BLUE, ARSH->ASH)
colors = [
# MONDAY
"GREEN","YELLOW","GREEN","BROWN","BLUE","PINK","BLUE","YELLOW","ORANGE","CREAM","ORANGE","RED","WHITE","BLUE","WHITE","BLUE","BLUE","BLUE","GREEN",

# TUESDAY
"ASH","BROWN","GREEN","BROWN","BLUE","BLUE","BLUE","PINK","PINK","ORANGE","ORANGE","RED","WHITE","BLUE","WHITE","WHITE","BLUE","BLUE","BLUE",

# WEDNESDAY
"GREEN","YELLOW","GREEN","BROWN","BLUE","PINK","RED","YELLOW","ORANGE","RED","ORANGE","RED","BLUE","BLUE","WHITE","BLUE","BLUE","WHITE","WHITE",

# THURSDAY
"BLUE","BLUE","GREEN","WHITE","BLUE","BROWN","PINK","YELLOW","ORANGE","CREAM","ORANGE","RED","WHITE","BLUE","WHITE","BLUE","BLUE","BLUE","GREEN",

# FRIDAY
"GREEN","WHITE","GREEN","BROWN","BLUE","BLUE","BLACK","WHITE","ORANGE","RED","RED","RED","WHITE","BLUE","WHITE","BLUE","BLUE","BLUE","WHITE"
]

# Count frequencies
color_count = Counter(colors)

# 1 & 2. Mean color (mode) and most worn color
most_common_color = color_count.most_common(1)[0][0]
print("Mean color:", most_common_color)
print("Most worn color:", most_common_color)

# 3. Median color
sorted_colors = sorted(colors)
median_color = sorted_colors[len(sorted_colors)//2]
print("Median color:", median_color)

# 4. Variance (based on frequency)
freq_values = list(color_count.values())
mean_freq = sum(freq_values) / len(freq_values)
variance = sum((x - mean_freq) ** 2 for x in freq_values) / len(freq_values)
print("Variance:", variance)

# 5. Probability of RED
total = len(colors)
red_count = color_count.get("RED", 0)
prob_red = red_count / total
print("Probability of RED:", prob_red)

# 6. PostgreSQL (structure only)
"""
CREATE TABLE colors (
    color VARCHAR(20),
    frequency INT
);
"""

# 7. Recursive search
def recursive_search(arr, target, index=0):
    if index >= len(arr):
        return False
    if arr[index] == target:
        return True
    return recursive_search(arr, target, index + 1)

print("Search 7 in list:", recursive_search([1,2,3,4,5,6,7], 7))

# 8. Random 4-digit binary → base 10
binary = ''.join(str(random.randint(0,1)) for _ in range(4))
decimal = int(binary, 2)
print("Binary:", binary, "Decimal:", decimal)

# 9. Sum first 50 Fibonacci numbers
a, b = 0, 1
fib_sum = 0

for _ in range(50):
    fib_sum += a
    a, b = b, a + b

print("Sum of first 50 Fibonacci numbers:", fib_sum)
