import timeit


def heapify(arr, end, i):
    largest = i
    l_child = 2 * i + 1
    r_child = 2 * i + 2
    if l_child < end and arr[l_child] >= arr[i]:
        largest = l_child
    if r_child < end and arr[r_child] >= arr[largest]:
        largest = r_child
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, end, largest)


def build_heap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)


def heap_sort(arr):
    build_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def partition(arr, p, r):
    pivot = arr[r]
    smaller = p
    for i in range(p, r, 1):
        if arr[i] <= pivot:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            smaller += 1
    arr[smaller], arr[r] = arr[r], arr[smaller]
    return smaller


def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


setup = '''
from __main__ import bubble_sort
from __main__ import heap_sort
from __main__ import quick_sort
'''


def test_sorted(method):
    code = '''
array = [1,4,6,8,9,15,56,77,98]
''' + method
    times = timeit.repeat(setup=setup,
                          stmt=code,
                          number=100,
                          repeat=5)

    print(method + ' sorted time: {}'.format(min(times)))


def test_unsorted(method):
    code = '''
array = [77,98,8,1,9,15,6,56,4]
''' + method
    times = timeit.repeat(setup=setup,
                          stmt=code,
                          number=100,
                          repeat=5)

    print(method + ' unsorted time: {}'.format(min(times)))


def test_reverse_sorted(method):
    code = '''
array = [98,77,56,15,9,8,6,4,1]
''' + method
    times = timeit.repeat(setup=setup,
                          stmt=code,
                          number=100,
                          repeat=5)

    print(method + ' reverse sorted time: {}'.format(min(times)))


if __name__ == '__main__':
    test_sorted("heap_sort(array)")
    test_sorted("quick_sort(array,0,len(array)-1)")
    test_sorted("bubble_sort(array)")
    print("")
    test_unsorted("heap_sort(array)")
    test_unsorted("quick_sort(array,0,len(array)-1)")
    test_unsorted("bubble_sort(array)")
    print("")
    test_reverse_sorted("heap_sort(array)")
    test_reverse_sorted("quick_sort(array,0,len(array)-1)")
    test_reverse_sorted("bubble_sort(array)")
