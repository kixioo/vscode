def smallest_factor(n):
    k = 2
    while k <= n:
        if n % k == 0:
            return k
        k += 1
a = smallest_factor(30)
print(a+10)
这是我的一次修改 修改时间为2022.5.27
