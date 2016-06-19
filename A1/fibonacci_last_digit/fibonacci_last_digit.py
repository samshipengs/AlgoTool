# Uses python3
import sys

def get_fibonacci_last_digit(n):
    # write your code here
    F_mod = [0]*(n+1)
    F_mod[0] = 0
    F_mod[1] = 1
    for i in range(2,n+1):
    	F_mod[i] = (F_mod[i-1] + F_mod[i-2]) % 10
    return F_mod[-1]

if __name__ == '__main__':
	n = int(input())
	if n<0 or n>1e7:
		print("Please enter integer number between 0 and 1e7")
		n = int(input())
	print(get_fibonacci_last_digit(n))
