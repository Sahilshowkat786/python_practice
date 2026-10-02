# ============================================================
# GENERATORS IN PYTHON
# ============================================================

# A generator produces values one at a time.
# Generators use the "yield" keyword.
#
# Main concepts:
# 1. yield
# 2. generator function
# 3. next()
# 4. for loop with generator
# 5. generator state
# 6. StopIteration
# 7. generator expression
# 8. memory efficiency
# 9. infinite generator
# 10. yield from
# 11. send()
# 12. close()
# 13. throw()
# ============================================================


# ============================================================
# 1. BASIC GENERATOR FUNCTION
# ============================================================

def numbers():
    yield 1
    yield 2
    yield 3


gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))


# ============================================================
# 2. next()
# ============================================================

def test():
    yield "A"
    yield "B"
    yield "C"


gen = test()

print(next(gen))
print(next(gen))
print(next(gen))

# If you call next() again:
#
# print(next(gen))
#
# It will raise:
# StopIteration


# ============================================================
# 3. GENERATOR WITH FOR LOOP
# ============================================================

def count(n):
    for i in range(1, n + 1):
        yield i


for number in count(5):
    print(number)


# ============================================================
# 4. GENERATOR REMEMBERS ITS STATE
# ============================================================

def demo():
    print("Start")

    yield 10

    print("Middle")

    yield 20

    print("End")

    yield 30


gen = demo()

print(next(gen))
print(next(gen))
print(next(gen))


# ============================================================
# 5. GENERATOR WITH CALCULATION
# ============================================================

def squares(n):
    for i in range(1, n + 1):
        yield i * i


for value in squares(5):
    print(value)


# ============================================================
# 6. GENERATOR VS NORMAL LIST
# ============================================================

# List
numbers_list = [x for x in range(10)]

print(numbers_list)


# Generator
numbers_generator = (x for x in range(10))

print(numbers_generator)


for number in numbers_generator:
    print(number)


# ============================================================
# 7. GENERATOR EXPRESSION
# ============================================================

squares = (x * x for x in range(5))

for square in squares:
    print(square)


# ============================================================
# 8. GENERATOR FOR LARGE DATA
# ============================================================

def large_numbers(n):
    for i in range(n):
        yield i


# It does NOT create all numbers at once.

gen = large_numbers(1000000)

print(next(gen))
print(next(gen))
print(next(gen))


# ============================================================
# 9. INFINITE GENERATOR
# ============================================================

def infinite_numbers():
    number = 1

    while True:
        yield number
        number += 1


gen = infinite_numbers()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# ============================================================
# 10. INFINITE EVEN NUMBERS
# ============================================================

def even_numbers():
    number = 0

    while True:
        yield number
        number += 2


gen = even_numbers()

for i in range(5):
    print(next(gen))


# ============================================================
# 11. YIELD FROM
# ============================================================

def numbers1():
    yield 1
    yield 2
    yield 3


def numbers2():
    yield 4
    yield 5
    yield 6


def combined():
    yield from numbers1()
    yield from numbers2()


for number in combined():
    print(number)


# ============================================================
# 12. YIELD FROM WITH LIST
# ============================================================

def fruits():
    yield from ["Apple", "Banana", "Mango"]


for fruit in fruits():
    print(fruit)


# ============================================================
# 13. GENERATOR SEND()
# ============================================================

def receiver():
    value = yield
    print("Received:", value)


gen = receiver()

# Start the generator
next(gen)

# Send value into generator
gen.send(100)


# ============================================================
# 14. SEND() MULTIPLE VALUES
# ============================================================

def calculator():
    total = 0

    while True:
        value = yield total
        total += value


gen = calculator()

print(next(gen))       # Start generator

print(gen.send(10))    # 10
print(gen.send(20))    # 30
print(gen.send(30))    # 60


# ============================================================
# 15. GENERATOR close()
# ============================================================

def test_close():
    try:
        while True:
            yield 1

    finally:
        print("Generator closed")


gen = test_close()

print(next(gen))

gen.close()


# ============================================================
# 16. GENERATOR throw()
# ============================================================

def test_throw():
    try:
        yield 1
        yield 2

    except ValueError:
        print("ValueError received")


gen = test_throw()

print(next(gen))

gen.throw(ValueError)


# ============================================================
# 17. GENERATOR WITH FILES
# ============================================================

def read_file(filename):

    with open(filename, "r") as file:

        for line in file:
            yield line.strip()


# Example:
#
# for line in read_file("data.txt"):
#     print(line)
#
# This is useful for large files because
# the entire file is not loaded into memory.


# ============================================================
# 18. GENERATOR FOR FILTERING
# ============================================================

def even_numbers_from_list(numbers):

    for number in numbers:

        if number % 2 == 0:
            yield number


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for number in even_numbers_from_list(numbers):
    print(number)


# ============================================================
# 19. GENERATOR FOR SQUARES
# ============================================================

def square_generator(numbers):

    for number in numbers:
        yield number ** 2


numbers = [1, 2, 3, 4, 5]

for square in square_generator(numbers):
    print(square)


# ============================================================
# 20. CHECK GENERATOR TYPE
# ============================================================

import types


def example():
    yield 1


gen = example()

print(type(gen))

print(
    isinstance(
        gen,
        types.GeneratorType
    )
)


# ============================================================
# 21. GENERATOR IS ITERATOR
# ============================================================

def my_generator():
    yield 10
    yield 20
    yield 30


gen = my_generator()

print(iter(gen) is gen)


# ============================================================
# 22. STOPITERATION
# ============================================================

def small_generator():
    yield 1
    yield 2


gen = small_generator()

try:

    print(next(gen))
    print(next(gen))
    print(next(gen))

except StopIteration:

    print("Generator finished!")


# ============================================================
# 23. LIST VS GENERATOR
# ============================================================

import sys


list_data = [x for x in range(100000)]

generator_data = (x for x in range(100000))


print("List memory:",
      sys.getsizeof(list_data))

print("Generator memory:",
      sys.getsizeof(generator_data))


# ============================================================
# 24. IMPORTANT RULE
# ============================================================

# return:
#
# Stops the function completely.
#
# yield:
#
# Pauses the function and remembers its state.


def return_example():

    return 10


def yield_example():

    yield 10
    yield 20


print(return_example())

gen = yield_example()

print(next(gen))
print(next(gen))


# ============================================================
# 25. PRACTICAL EXAMPLE
# ============================================================

def numbers_between(start, end):

    while start <= end:

        yield start

        start += 1


for number in numbers_between(1, 10):

    print(number)


# ============================================================
# IMPORTANT POINTS TO REMEMBER
# ============================================================

"""
GENERATOR:

A generator is a special iterator that produces values
one at a time using yield.

yield:
    Pauses the function and saves its state.

next():
    Requests the next value.

StopIteration:
    Raised when the generator has no more values.

Generator expression:
    (x for x in range(10))

yield from:
    Used to yield values from another iterable/generator.

send():
    Sends a value into a generator.

close():
    Stops the generator.

throw():
    Sends an exception into the generator.

Main advantage:
    Memory efficient / lazy evaluation.

Common uses:
    - Large files
    - Large datasets
    - Data processing
    - APIs
    - Infinite sequences
    - AI/ML data pipelines
"""