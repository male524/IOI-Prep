import random

rand_items = [random.randint(-100, 100) for i in range(100)]


def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1


print('before: ', rand_items)
insertion_sort(rand_items)
print('After: ', rand_items)
