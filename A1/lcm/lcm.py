# Uses python3
import sys

def gcd(a, b):
	pair = sorted([a,b])
	if pair[0] == 0:
		return pair[1]
	else:
		b = pair[1]%pair[0]
	return gcd(pair[0],b)

def lcm(a, b):
    #write your code here
    GCD = gcd(a,b)
    return (a*b)/GCD

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

