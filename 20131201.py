"""
问题描述
　　给定n个正整数，找出它们中出现次数最多的数。如果这样的数有多个，请输出其中最小的一个。
输入格式
　　输入的第一行只有一个正整数n(1 ≤ n ≤ 1000)，表示数字的个数。
　　输入的第二行有n个整数s1, s2, …, sn (1 ≤ si ≤ 10000, 1 ≤ i ≤ n)。相邻的数用空格分隔。
输出格式
　　输出这n个次数中出现次数最多的数。如果这样的数有多个，输出其中最小的一个。
样例输入
6
10 1 10 20 30 20
样例输出
10
算法设计
使用字典储存出现次数，输出最大的即可
"""

from collections import Counter
n = int(input())
nlist = list(input().split(' '))
# n = 1000
# nlist = [(i+1) % 700 for i in range(1000)]
n_dict = Counter()
for num in nlist:
    n_dict[num] += 1
# print(sorted(n_dict, key=lambda x: n_dict[x], reverse=True)[0])
print(max(n_dict, key=lambda x: n_dict[x]))

