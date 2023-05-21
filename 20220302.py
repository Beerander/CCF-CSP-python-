"""
http://118.190.20.162/view.page?gpid=T142
差分+前缀和
"""
n, m, k = map(int, input().split())
spots = [[i for i in map(int, input().split())] for j in range(n)]
num = 0
for i in range(n):
    if num < spots[i][0]:
        num = spots[i][0]+1
    spots[i][0], spots[i][1] = max(1, spots[i][0]-spots[i][1]+1), spots[i][0]
times = []
for i in range(m):
    point = int(input())
    times.append(point+k)
temp = [0 for i in range(num*2)]
for spot in spots:
    temp[spot[0]] += 1
    temp[spot[1]+1] -= 1
for i in range(1, num+1):
    temp[i] += temp[i-1]
for time in times:
    print(temp[time])

