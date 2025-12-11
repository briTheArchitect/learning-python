"""
Practice file demonstrating Python list comprehension patterns:
mapping, filtering, conditional comprehensions, and nested comprehensions.

Core patterns:

1. Basic mapping:
[NEW_VALUE for ITEM in LIST]

2. Filtering:
[ITEM for ITEM in LIST if CONDITION]

3. Conditional expression inside a comprehension:
[VALUE_IF_TRUE if CONDITION else VALUE_IF_FALSE for ITEM in LIST]

4. Nested list comprehension (flattening):
[ITEM for SUBLIST in NESTED_LIST for ITEM in SUBLIST]
"""

# DOUBLE EVERY NUMBER
def double_num(arr):
    return [n * 2 for n in arr]

arr = [1, 2, 3, 4]
print(double_num(arr))

# CONVERT ALL WORDS TO UPPERCASE
def upper_case(words):
    return [word.upper() for word in words]

words = ['cat', 'dog', 'bird']
print(upper_case(words))

# CONVERT NUMBERS TO STRINGS
def num_to_str(nums):
    return [str(num) for num in nums]

nums = [10, 20, 30]
print(num_to_str(nums))

# KEEP ONLY POSITIVE NUMBERS
def only_positive(nums):
    return [n for n in nums if n > 0]

nums = [-2, 5, 0, 8, -1]
print(only_positive(nums))

# SQUARE ONLY THE EVEN NUMBERS
def square_evens(nums):
    return [n ** 2 for n in nums if n % 2 == 0]

nums = [1, 2, 3, 4, 5]
print(square_evens(nums))

# GET LENGTHS OF ONLY THE LONG WORDS (LEN > 3)
def len_long_words(words):
    return [len(word) for word in words if len(word) > 3]

words = ['hi', 'apple', 'no', 'piano']
print(len_long_words(words))

# FLATTEN A 2D LIST
# NESTED COMPREHENSION:
# [num for sublist in nested for num in sublist]
def flatten_2D(nested):
    return [num for sublist in nested for num in sublist]

nested = [[1,2],[3,4],[5]]
print(flatten_2D(nested))

# EXTRACT FIRST LETTERS ONLY FROM WORDS THAT START WITH A VOWEL
def first_letters(words):
    # startswith() ONLY takes strings or tuple of strings
    return [word[0] for word in words if word.startswith(('a', 'e', 'i', 'o', 'u'))]

words = ['apple', 'dog', 'orange', 'car', 'umbrella']
print(first_letters(words))

# ADD 1 TO EACH NUMBER IF ITS NEGATIVE
# [VALUE_IF_TRUE if CONDITION else VALUE_IF_FALSE for ITEM in LIST]
def add_to_negative(nums):
    
    return [num + 1 if num < 0 else num for num in nums]

nums = [3, -1, -5, 10]
print(add_to_negative(nums))

# REPLACE EACH NUMBER WITH 'EVEN' OR 'ODD'
def even_odd_labels(nums):
    return ['EVEN' if n % 2 == 0 else 'ODD' for n in nums]

nums = [1, 2, 3, 4, 5]
print(even_odd_labels(nums))

# BUILD A LIST OF TUPLES (NUMBER, NUMBER^2)
def list_tuples(nums):
    return [(num, num ** 2) for num in nums]

nums = [1, 2, 3]
print(list_tuples(nums))

# KEEP ONLY ITEMS THAT DON'T CONTAIN THE LETTER 'a'
def items_without_a(words):
    return [word for word in words if 'a' not in word]

words = ['cat', 'dog', 'fish', 'ham']
print(items_without_a(words))
