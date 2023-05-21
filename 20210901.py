"""
http://118.190.20.162/view.page?gpid=T129
"""
n = int(input())
B = list(map(int, input().split()))
res_max, res_min = B[0], B[0]
for i in range(1, n):
    res_max += B[i]
    if B[i] > B[i-1]:
        res_min += B[i]
print(res_max)
print(res_min)

