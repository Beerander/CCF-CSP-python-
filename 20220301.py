"""
http://118.190.20.162/view.page?gpid=T143
"""
n, k = list(map(int, input().split()))
sents = []
count = 0
for _ in range(k):
    sents.append(list(map(int, input().split())))
args = [0] * n
for sent in sents:
    x, y = sent
    if y != 0 and args[y-1] == 0:
        count += 1
    args[x-1] = 1
print(count)


