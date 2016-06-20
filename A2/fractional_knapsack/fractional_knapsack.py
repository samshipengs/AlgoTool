# Uses python3
import sys
import numpy as np
def get_optimal_value(capacity, weights, values):
	value = 0.
	cap_remian = capacity
    # write your code here
	ratio = np.array(values)/np.array(weights)
	ratio_sorted_ind = np.argsort(ratio)[::-1]
	for i in ratio_sorted_ind:
		if cap_remian/weights[i] <= 1.:
			value += cap_remian*ratio[i]
			break
			# cap_remian -= weights[i]
		else:
			value += weights[i]*ratio[i]
			cap_remian -= weights[i]
	return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    # print(weights)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
