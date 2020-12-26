import random

rand_items = [random.randint(-100, 100) for i in range(20)]


def insertion_sort(A):



print('before: ', rand_items)
insertion_sort(rand_items)
print('After: ', rand_items)