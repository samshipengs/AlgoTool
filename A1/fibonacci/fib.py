# Uses python3
import numpy as np
def calc_fib_naive(n):
    if (n <= 1):
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:	
		F = [0]*(n+1)
		F[0] = 0
		F[1] = 1
		for i in range(2,n+1):
			F[i] = F[i-1] + F[i-2]
		return F[-1]
	return 0
n = int(input())
print(calc_fib(n))
