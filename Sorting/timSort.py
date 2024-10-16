import matplotlib.pyplot as plt
import numpy as np

RUN = 32

def insertion_sort(arr, left, right, bars, speed):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            update_bars(arr, bars, speed)
        arr[j + 1] = key
        update_bars(arr, bars, speed)

def merge(arr, left, mid, right, bars, speed):
    len1, len2 = mid - left + 1, right - mid
    left_half = arr[left:mid + 1]
    right_half = arr[mid + 1:right + 1]

    i, j, k = 0, 0, left

    while i < len1 and j < len2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        update_bars(arr, bars, speed)
        k += 1

    while i < len1:
        arr[k] = left_half[i]
        i += 1
        k += 1
        update_bars(arr, bars, speed)

    while j < len2:
        arr[k] = right_half[j]
        j += 1
        k += 1
        update_bars(arr, bars, speed)

def tim_sort(arr, bars, speed):
    n = len(arr)
    for start in range(0, n, RUN):
        end = min(start + RUN - 1, n - 1)
        insertion_sort(arr, start, end, bars, speed)

    size = RUN
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right, bars, speed)
        size *= 2

def update_bars(arr, bars, speed):
    for bar, val in zip(bars, arr):
        bar.set_height(val)
    plt.pause(speed)

def tim_sort_visual(arr, speed=0.1):
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    bars = ax.bar(np.arange(len(arr)), arr, color='blue')
    update_bars(arr, bars, speed)
    tim_sort(arr, bars, speed)
    plt.show()

arr = [29, 84, 17, 65, 98, 14, 56, 3, 44, 92, 
       39, 71, 11, 27, 64, 50, 81, 6, 19, 99, 
       47, 33, 75, 61, 23, 2, 89, 43, 31, 93, 
       8, 13, 41, 55, 74, 37, 18, 97, 52, 21, 
       9, 5, 67, 78, 12, 88, 20, 32, 59, 70]

tim_sort_visual(arr, speed=0.05)
