# Problem 70

n = 7

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    prev1 = 2
    prev2 = 1
    for i in range(3, n+1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    print(prev1)