import matplotlib.pyplot as plt
import numpy as np
import random

def counting_sort(arr, exp, bars, speed):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        update_bars(output, bars, speed)

    for i in range(n):
        arr[i] = output[i]
    update_bars(arr, bars, speed)

def radix_sort(arr, bars, speed):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp, bars, speed)
        exp *= 10

def update_bars(arr, bars, speed):
    for bar, val in zip(bars, arr):
        bar.set_height(val)
    plt.pause(speed)

def radix_sort_visual(arr, speed=0.1):
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
    radix_sort(arr, bars, speed)
    plt.show()

arr = [random.randint(1, 1000) for _ in range(200)]

radix_sort_visual(arr, speed=0.05)
