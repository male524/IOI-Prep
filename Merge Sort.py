import random

rand_items = [random.randint(-100, 100) for i in range(20)]


def merge_sort(A):
    pass


print('before: ', rand_items)
merge_sort(rand_items)
print('After: ', rand_items)