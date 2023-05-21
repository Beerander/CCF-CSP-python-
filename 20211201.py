"""
http://118.190.20.162/view.page?gpid=T138
"""
n, N = list(map(int, input().split()))
num = list(map(int, input().split()))
num = [0] + num + [N]
num_d = [0] * (n + 1)
for i in range(n + 1):
    num_d[i] = num[i+1] - num[i]
res = 0
for i in range(n + 1):
    res += num_d[i] * i
print(res)

