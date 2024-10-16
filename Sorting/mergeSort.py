import matplotlib.pyplot as plt
import numpy as np
def merge(arr, left, mid, right, bars):
    n1 = mid - left + 1
    n2 = right - mid
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        update_bars(arr, bars)
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        update_bars(arr, bars)
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        update_bars(arr, bars)
def merge_sort(arr, left, right, bars):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid, bars)
        merge_sort(arr, mid + 1, right, bars)
        merge(arr, left, mid, right, bars)
def update_bars(arr, bars):
    for bar, val in zip(bars, arr):
        bar.set_height(val)
    plt.pause(0.1)

def merge_sort_visual(arr):
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
    merge_sort(arr, 0, len(arr) - 1, bars)
    plt.show()

arr = [29, 84, 17, 65, 98, 14, 56, 3, 44, 92, 
       39, 71, 11, 27, 64, 50, 81, 6, 19, 99, 
       47, 33, 75, 61, 23, 2, 89, 43, 31, 93, 
       8, 13, 41, 55, 74, 37, 18, 97, 52, 21, 
       9, 5, 67, 78, 12, 88, 20, 32, 59, 70]

merge_sort_visual(arr)
