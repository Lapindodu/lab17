# Task 1: Create a generator to iterate over a list of numbers.
def number_generator(numbers):
    for number in numbers:
        yield number


# Task 2: Develop a generator that yields even numbers from a given range.
def even_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num


# Task 3: Implement a generator to yield odd numbers within a specified range.
def odd_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num


# Task 4: Write a generator that produces Fibonacci numbers.
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Task 5: Create a generator that yields prime numbers up to a given limit.
def prime_number_generator(limit):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, limit + 1):
        if is_prime(num):
            yield num


# Task 6: Develop a generator to traverse a binary tree in pre-order.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order_traversal(root):
    if root:
        yield root.val
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)


# Task 7: Implement a generator for in-order traversal of a binary tree.
def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.val
        yield from in_order_traversal(root.right)


# Task 8: Write a generator for post-order traversal of a binary tree.
def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.val


# Task 9: Create a generator to traverse a graph using depth-first search (DFS).
def dfs_traversal(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            yield node
            visited.add(node)
            stack.extend(reversed(graph.get(node, [])))


# Task 10: Develop a generator for breadth-first search (BFS) traversal of a graph.
def bfs_traversal(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            yield node
            visited.add(node)
            queue.extend(graph.get(node, []))


# Task 11: Implement a generator that yields the keys of a dictionary.
def dict_keys_generator(d):
    for key in d.keys():
        yield key


# Task 12: Write a generator that yields the values of a dictionary.
def dict_values_generator(d):
    for value in d.values():
        yield value


# Task 13: Create a generator to iterate over key-value pairs of a dictionary.
def dict_items_generator(d):
    for item in d.items():
        yield item


# Task 14: Develop a generator that yields lines from a file one by one.
def file_lines_generator(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            yield line.strip()


# Task 15: Implement a generator to iterate over words in a text file.
def file_words_generator(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            for word in line.split():
                yield word


# Task 16: Write a generator that yields characters from a string one by one.
def string_chars_generator(string):
    for char in string:
        yield char


# Task 17: Create a generator to yield unique elements from a list.
def unique_elements_generator(lst):
    seen = set()
    for elem in lst:
        if elem not in seen:
            seen.add(elem)
            yield elem


# Task 18: Develop a generator that yields elements of a list in reverse order.
def reverse_list_generator(lst):
    for elem in reversed(lst):
        yield elem


# Task 19: Implement a generator to yield the Cartesian product of two lists.
def cartesian_product_generator(lst1, lst2):
    for elem1 in lst1:
        for elem2 in lst2:
            yield (elem1, elem2)


# Task 20: Write a generator that yields permutations of a list.
from itertools import permutations


def permutations_generator(lst):
    for perm in permutations(lst):
        yield perm


# Task 21: Create a generator to yield combinations of a list of elements.
from itertools import combinations


def combinations_generator(lst):
    for r in range(1, len(lst) + 1):
        for combo in combinations(lst, r):
            yield combo


# Task 22: Develop a generator to iterate over a list of tuples.
def tuple_list_generator(tuples):
    for tup in tuples:
        yield tup


# Task 23: Implement a generator that yields elements from multiple lists in parallel.
def parallel_lists_generator(*lists):
    for elements in zip(*lists):
        yield elements


# Task 24: Write a generator that yields elements from a nested list (flattening the list).
def flatten_list_generator(nested_list):
    for elem in nested_list:
        if isinstance(elem, list):
            yield from flatten_list_generator(elem)
        else:
            yield elem


# Task 25: Create a generator to yield elements from a nested dictionary.
def nested_dict_generator(d):
    for key, value in d.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)


# Task 26: Develop a generator to yield powers of 2 up to a given number.
def powers_of_two_generator(n):
    for i in range(n + 1):
        yield 2 ** i


# Task 27: Implement a generator that yields powers of a given base up to a specified limit.
def powers_of_base_generator(base, limit):
    result = 1
    while result <= limit:
        yield result
        result *= base


# Task 28: Write a generator to yield the squares of numbers in a given range.
def squares_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 2


# Task 29: Create a generator to yield cubes of numbers in a specified range.
def cubes_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 3


# Task 30: Develop a generator that yields factorials of numbers up to a given limit.
def factorials_generator(n):
    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * factorial(num - 1)

    for i in range(n + 1):
        yield factorial(i)


# Task 31: Implement a generator to yield numbers in the Collatz sequence.
def collatz_sequence_generator(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    yield n


# Task 32: Write a generator that yields numbers in a geometric progression.
def geometric_progression_generator(initial, ratio, limit):
    value = initial
    while value <= limit:
        yield value
        value *= ratio


# Task 33: Create a generator to yield numbers in an arithmetic progression.
def arithmetic_progression_generator(initial, difference, limit):
    value = initial
    while value <= limit:
        yield value
        value += difference


# Task 34: Develop a generator that yields the running sum of a list of numbers.
def running_sum_generator(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total


# Task 35: Implement a generator to yield the running product of a list of numbers.
def running_product_generator(numbers):
    product = 1
    for number in numbers:
        product *= number
        yield product


