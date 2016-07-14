# Uses python3
import sys
import numpy as np 
# def optimal_weight(W, w):
#     # write your code here
#     result = 0
#     for x in w:
#         if result + x <= W:
#             result = result + x
#     return result


def optimal_weight(W,w):
	value = np.ndarray((W+1, n+1))
	# for i in range(n+1):
		# value[(0, i)] = 0
	# for j in range(W+1):
	# 	value[(j,0)] = 0

	for i in range(1, n+1):
		for j in range(1, W+1):
			if i-1 == 0:
				value[j,i] = 0
			else:
				value[j, i] = value[j, i-1]
			if w[i-1] <= j:
				if j - w[i-1] == 0 or i-1 ==0:
					val_i = w[i-1]
				else:
					val_i = value[j - w[i-1], i-1] + w[i-1]
				if value[j, i] < val_i:
					value[j, i] = val_i


	return int(value[W, n])


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
