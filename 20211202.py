"""
http://118.190.20.162/view.page?gpid=T137
分段 观察数字特点 妙
"""
n, N = map(int, input().split())  # n, N两个正整数
A = [0] + list(map(int, input().split()))  # [0] + A[1]..A[n]

r = N // (n + 1)
f_num = [0] * (n + 1)  # 当前f分段的剩余数的个数
for i in range(n):
    f_num[i] = A[i + 1] - A[i]
f_num[n] = N - A[n]
f = g = 0  # f(i),g(i)的初始值
res = 0  # error(A)
g_num = r  # 当前g分段的剩余数的个数
while f <= n:
    # 当前f分段的剩余数的个数 >= 当前g分段的剩余数的个数
    if f_num[f] >= g_num:
        res += abs(g - f) * g_num
        f_num[f] -= g_num
        g += 1
        g_num = r
    # 当前f分段的剩余数的个数 < 当前g分段的剩余数的个数
    else:
        res += abs(g - f) * f_num[f]
        g_num -= f_num[f]
        f += 1
print(res)
