# Uses python3
import sys

def get_majority_element(a,left,right):
    a.sort()
    mid = (left+right-1)//2
    if right == 1:
        return 1
    for i in range(mid+1):
        if right % 2 == 1:
            if a[i] == a[mid+i]:
                return 2
        else:
            if a[i] == a[mid+i+1]:
                return 3 
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
