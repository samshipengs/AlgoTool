# Uses python3
import sys

def optimal_summands(n):
	summands = []
	#write your code here
	Sum = 0
	N = 1
	while Sum < n:
		if (n-Sum) < N:
			summands[-1] += (n-Sum)
			Sum = n
		else:
			summands.append(N)
			Sum += N
			N += 1
	return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
