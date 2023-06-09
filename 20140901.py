"""
问题描述
　　给定n个不同的整数，问这些数中有多少对整数，它们的值正好相差1。
输入格式
　　输入的第一行包含一个整数n，表示给定整数的个数。
　　第二行包含所给定的n个整数。
输出格式
　　输出一个整数，表示值正好相差1的数对的个数。
样例输入
6
10 2 6 3 7 8
样例输出
3
样例说明
　　值正好相差1的数对包括(2, 3), (6, 7), (7, 8)。
评测用例规模与约定
　　1<=n<=1000，给定的整数为不超过10000的非负整数。
"""
n = int(input())
num_list = list(map(int, input().split()))
num_list = sorted(num_list)
count = 0
for i in range(1, n):
    if num_list[i] - num_list[i-1] == 1:
        count += 1
print(count)
