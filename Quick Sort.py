import random

rand_items = [random.randint(1, 100) for i in range(10000)]


def quick_sort(A):
    if len(A) > 1:
        pivot_index = len(A) // 2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(A):
            if i != pivot_index:
                if val < A[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        quick_sort(smaller_items)
        quick_sort(larger_items)
        A[:] = smaller_items + [A[pivot_index]] + larger_items




print('before: ', rand_items)
quick_sort(rand_items)
print('After: ', rand_items)