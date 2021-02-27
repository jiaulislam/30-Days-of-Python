import math
import os
import random
import re
import sys

def find_elements_sum(row, col, arr):
    first_row = arr[row][col] + arr[row][col+1] + arr[row][col+2] 
    mid_row = arr[row+1][col+1]
    third_row = arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]

    return first_row + mid_row + third_row


def solve_the_problem():
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    maximum_sum = -999999999

    for i in range(0, 4):
        for j in range(0, 4):
            sum = find_elements_sum(i, j, arr)
            maximum_sum = max(sum, maximum_sum)

    return maximum_sum

if __name__ == '__main__':
    print(solve_the_problem())
