# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

ordered = sorted(a)
result = ordered[-1]*ordered[-2]
print(result)
