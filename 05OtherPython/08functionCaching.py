# ============================================================
# FUNCTION CACHING IN PYTHON
# ============================================================

# Function caching means:
# Store the result of a function so that if the same input
# is used again, Python can return the stored result instead
# of calculating it again.


# ============================================================
# 1. BASIC @cache
# ============================================================

from functools import cache


@cache
def square(n):
    print("Calculating square...")
    return n * n


print(square(5))
print(square(5))
print(square(5))

# "Calculating square..." is printed only once.
#
# First call:
#     square(5) -> calculate -> store 25
#
# Next calls:
#     square(5) -> get 25 from cache


# ============================================================
# 2. CACHE WITH MULTIPLE ARGUMENTS
# ============================================================

@cache
def add(a, b):
    print("Calculating addition...")
    return a + b


print(add(10, 20))
print(add(10, 20))
print(add(5, 10))

# (10, 20) is cached separately from (5, 10).


# ============================================================
# 3. CACHE WITH STRING
# ============================================================

@cache
def greet(name):
    print("Creating greeting...")
    return f"Hello {name}"


print(greet("Sahil"))
print(greet("Sahil"))

print(greet("Rahul"))


# ============================================================
# 4. FIBONACCI WITHOUT CACHE
# ============================================================

def fibonacci_without_cache(n):

    if n <= 1:
        return n

    return (
        fibonacci_without_cache(n - 1)
        + fibonacci_without_cache(n - 2)
    )


print(fibonacci_without_cache(10))


# ============================================================
# 5. FIBONACCI WITH CACHE
# ============================================================

@cache
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(50))


# ============================================================
# 6. WHY CACHE HELPS
# ============================================================

# Without cache:
#
# fibonacci(5)
#     ├── fibonacci(4)
#     │      ├── fibonacci(3)
#     │      └── fibonacci(2)
#     │
#     └── fibonacci(3)
#
# Same values are calculated many times.
#
#
# With cache:
#
# fibonacci(5)
#     ↓
# Calculate and store
#
# fibonacci(4)
#     ↓
# Calculate and store
#
# fibonacci(3)
#     ↓
# Already stored → reuse result


# ============================================================
# 7. @lru_cache
# ============================================================

from functools import lru_cache


@lru_cache(maxsize=3)
def multiply(a, b):

    print("Calculating multiplication...")

    return a * b


print(multiply(2, 3))
print(multiply(2, 3))

print(multiply(4, 5))
print(multiply(6, 7))


# maxsize=3 means the cache can store up to 3 entries.


# ============================================================
# 8. LRU MEANING
# ============================================================

# LRU = Least Recently Used
#
# When cache becomes full, older/less recently used
# entries can be removed.


# ============================================================
# 9. cache_info()
# ============================================================

@lru_cache(maxsize=5)
def cube(n):

    return n ** 3


cube(2)
cube(3)
cube(2)
cube(4)

print(cube.cache_info())

# Example:
#
# CacheInfo(
#     hits=1,
#     misses=3,
#     maxsize=5,
#     currsize=3
# )


# ============================================================
# 10. UNDERSTANDING cache_info()
# ============================================================

"""
hits:
    Number of times result was found in cache.

misses:
    Number of times result was NOT found
    and had to be calculated.

maxsize:
    Maximum number of cached results.

currsize:
    Number of results currently stored.
"""


# ============================================================
# 11. CLEAR CACHE
# ============================================================

cube.cache_clear()

print(cube.cache_info())


# ============================================================
# 12. @cache vs @lru_cache
# ============================================================

"""
@cache

    Unlimited cache.

Example:

from functools import cache

@cache
def function(x):
    return x * 2


@lru_cache

    Cache has a maximum size.

Example:

from functools import lru_cache

@lru_cache(maxsize=100)
def function(x):
    return x * 2
"""


# ============================================================
# 13. CACHE WITH RECURSION
# ============================================================

@cache
def factorial(n):

    if n <= 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))


# ============================================================
# 14. CACHE IS BASED ON ARGUMENTS
# ============================================================

@cache
def test(value):

    print("Calculating...")
    return value * 10


print(test(10))   # Calculate
print(test(10))   # Cache
print(test(20))   # Calculate
print(test(20))   # Cache


# ============================================================
# 15. IMPORTANT: ARGUMENTS MUST BE HASHABLE
# ============================================================

# These work:

@cache
def example(number):
    return number * 2


print(example(10))
print(example("Python"))


# Lists cannot normally be used as cache arguments:
#
# @cache
# def test_list(my_list):
#     return len(my_list)
#
# test_list([1, 2, 3])
#
# This raises:
# TypeError: unhashable type: 'list'
#
# Use a tuple instead:

@cache
def test_tuple(my_tuple):

    return sum(my_tuple)


print(test_tuple((1, 2, 3)))


# ============================================================
# 16. PRACTICAL EXAMPLE
# ============================================================

@cache
def expensive_calculation(number):

    print("Performing expensive calculation...")

    result = number ** 2 + number * 10

    return result


print(expensive_calculation(100))
print(expensive_calculation(100))
print(expensive_calculation(100))


# ============================================================
# 17. HOW CACHING WORKS
# ============================================================

"""
Function call
      |
      v
Is this input already cached?
      |
   YES -----------------> Return stored result
      |
      NO
      |
      v
Calculate result
      |
      v
Store result in cache
      |
      v
Return result
"""


# ============================================================
# 18. IMPORTANT THINGS TO REMEMBER
# ============================================================

"""
1. Caching stores function results.

2. @cache is provided by functools.

3. @lru_cache is also provided by functools.

4. Same arguments -> cached result can be reused.

5. Different arguments -> new calculation.

6. @cache has unlimited cache size.

7. @lru_cache can have a maximum size.

8. LRU means Least Recently Used.

9. cache_info() shows cache statistics.

10. cache_clear() removes cached results.

11. Arguments need to be hashable.

12. Caching is especially useful for:
    - Recursion
    - Fibonacci
    - Expensive calculations
    - Repeated function calls
    - Dynamic programming
"""


# ============================================================
# MOST IMPORTANT SYNTAX
# ============================================================

"""
from functools import cache

@cache
def function(x):
    return x * 2
"""


# ============================================================
# ADVANCED SYNTAX
# ============================================================

"""
from functools import lru_cache

@lru_cache(maxsize=100)
def function(x):
    return x * 2
"""