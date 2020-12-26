import random

rand_items = [random.randint(-50, 100) for i in range(20)]


def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                A[j + 1], A[j] = A[j], A[j + 1]


print("Before: ", rand_items)
bubble_sort(rand_items)
print("After: ", rand_items)
