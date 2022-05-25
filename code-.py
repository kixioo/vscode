def smallest_factor(n):
    k = 2
    while k <= n:
        if n % k == 0:
            return k
        k += 1
a = smallest_factor(30)
print(a+10)

