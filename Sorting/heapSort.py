import matplotlib.pyplot as plt
import numpy as np

def heapify(arr, n, i, bars, speed):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        update_bars(arr, bars, speed)
        heapify(arr, n, largest, bars, speed)

def heap_sort(arr, bars, speed):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, bars, speed)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        update_bars(arr, bars, speed)
        heapify(arr, i, 0, bars, speed)

def update_bars(arr, bars, speed):
    for bar, val in zip(bars, arr):
        bar.set_height(val)
    plt.pause(speed)

def heap_sort_visual(arr, speed=0.1):
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
    heap_sort(arr, bars, speed)
    plt.show()

arr = [29, 84, 17, 65, 98, 14, 56, 3, 44, 92, 
       39, 71, 11, 27, 64, 50, 81, 6, 19, 99, 
       47, 33, 75, 61, 23, 2, 89, 43, 31, 93, 
       8, 13, 41, 55, 74, 37, 18, 97, 52, 21, 
       9, 5, 67, 78, 12, 88, 20, 32, 59, 70]

heap_sort_visual(arr)
