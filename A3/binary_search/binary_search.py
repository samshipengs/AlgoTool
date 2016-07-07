# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    while left < (right-1):
        mid = (left + right)//2
        if x < a[mid]:
            right = mid
        else:
            left = mid
    if x == a[left]:
        return left
    else:
        return -1

 # def binary_search(a, x):


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
