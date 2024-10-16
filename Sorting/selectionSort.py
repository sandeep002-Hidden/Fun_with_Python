import matplotlib.pyplot as plt
import numpy as np

def selection_sort(arr, bars):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        update_bars(arr, bars)

def update_bars(arr, bars):
    for bar, val in zip(bars, arr):
        bar.set_height(val)
    plt.pause(0.1)

def selection_sort_visual(arr):
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
    update_bars(arr, bars)
    selection_sort(arr, bars)
    plt.show()

arr = [29, 84, 17, 65, 98, 14, 56, 3, 44, 92, 
       39, 71, 11, 27, 64, 50, 81, 6, 19, 99, 
       47, 33, 75, 61, 23, 2, 89, 43, 31, 93, 
       8, 13, 41, 55, 74, 37, 18, 97, 52, 21, 
       9, 5, 67, 78, 12, 88, 20, 32, 59, 70]

selection_sort_visual(arr)
