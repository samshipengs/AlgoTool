# Uses python3
import sys

def get_fibonaccihuge(n, m):
	if m == 1:
		return 0
	else:
		N = m*10
		F = [0]*(N+1)
		F[0] = 0
		F[1] = 1
		F_mod = [0]*(N+1)
		F_mod[0] = 0
		F_mod[1] = 1
		for i in range(2,N+1):
			F[i] = F[i-1] + F[i-2]
			F_mod[i] = F[i] % m
			rep = int(i/2)+1
			if F_mod[:rep] == F_mod[rep:i+1]:
				break
		res_ind = n % (int(i/2)+1)
		result = F[res_ind] % m
		return result
	return 0

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
