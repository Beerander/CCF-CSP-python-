"""
问题描述
　　给定一个年份y和一个整数d，问这一年的第d天是几月几日？
　　注意闰年的2月有29天。满足下面条件之一的是闰年：
　　1） 年份是4的整数倍，而且不是100的整数倍；
　　2） 年份是400的整数倍。
输入格式
　　输入的第一行包含一个整数y，表示年份，年份在1900到2015之间（包含1900和2015）。
　　输入的第二行包含一个整数d，d在1至365之间。
输出格式
　　输出两行，每行一个整数，分别表示答案的月份和日期。
样例输入
2015
80
样例输出
3
21
样例输入
2000
40
样例输出
2
9
"""


def is_leap(_year):
    return (_year % 4 == 0 and _year % 100 != 0) or (_year % 400 == 0)


y = int(input())
d = int(input())
if is_leap(y):
    month_prefixsum = {1: 0, 2: 31, 3: 29, 4: 31, 5: 30, 6: 31, 7: 30, 8: 31, 9: 31, 10: 30, 11: 31, 12: 30, 13: 31}
else:
    month_prefixsum = {1: 0, 2: 31, 3: 28, 4: 31, 5: 30, 6: 31, 7: 30, 8: 31, 9: 31, 10: 30, 11: 31, 12: 30, 13: 31}
for i in range(2, 14):
    month_prefixsum[i] += month_prefixsum[i-1]
for k in month_prefixsum:
    if d <= month_prefixsum[k]:
        day = d - month_prefixsum[k-1]
        print(k-1)
        print(day)
        break
