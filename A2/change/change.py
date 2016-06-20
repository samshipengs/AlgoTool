# Uses python3
import sys

def get_change(n):
    #write your code here
    # 1, 5, 10
    n1 = n//10
    n2 = (n%10)//5
    n3 = ((n%10)%5)//1
    return n1+n2+n3

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
