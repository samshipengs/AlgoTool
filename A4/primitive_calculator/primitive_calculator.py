# Uses python3
import sys
import numpy as np

# def optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)
def optimal_sequence(n):
    # v is vector where v[i] stands for the min steps to reach i
    v = [0]*(n+1)
    v[1] = 1
    for i in range(1, n):
        if v[i+1] == 0 or (v[i+1] > v[i] + 1):
            v[i+1] = v[i] + 1
        if 2*i <= n:
            if v[i*2] == 0 or (v[i*2] > v[i] + 1):
                v[i*2] = v[i] + 1
        if 3*i <= n:
            if v[i*3] == 0 or (v[i*3] > v[i] + 1):
                v[i*3] = v[i] + 1
    # Filled the min steps v, now we need to find which path(number) it took
    solution = []
    while n > 1:
        solution.append(n)
        if v[n-1] == v[n] - 1:
            n = n - 1
        elif n%2 == 0 and (v[n//2]==v[n]-1):
            n = n//2
        elif n%3 == 0 and (v[n//3]==v[n]-1):
            n = n//3
    solution.append(1)
    return reversed(solution)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
