"""
问题描述
　　有一类节日的日期并不是固定的，而是以“a月的第b个星期c”的形式定下来的，比如说母亲节就定为每年的五月的第二个星期日。
　　现在，给你a，b，c和y1, y2(1850 ≤ y1, y2 ≤ 2050)，希望你输出从公元y1年到公元y2年间的每年的a月的第b个星期c的日期。
　　提示：关于闰年的规则：年份是400的整数倍时是闰年，否则年份是4的倍数并且不是100的倍数时是闰年，其他年份都不是闰年。例如1900年就不是闰年，而2000年是闰年。
　　为了方便你推算，已知1850年1月1日是星期二。
输入格式
　　输入包含恰好一行，有五个整数a, b, c, y1, y2。其中c=1, 2, ……, 6, 7分别表示星期一、二、……、六、日。
输出格式
　　对于y1和y2之间的每一个年份，包括y1和y2，按照年份从小到大的顺序输出一行。
　　如果该年的a月第b个星期c确实存在，则以"yyyy/mm/dd"的格式输出，即输出四位数的年份，两位数的月份，两位数的日期，中间用斜杠“/”分隔，位数不足时前补零。
　　如果该年的a月第b个星期c并不存在，则输出"none"（不包含双引号)。
样例输入
5 2 7 2014 2015
样例输出
2014/05/11
2015/05/10
评测用例规模与约定
　　所有评测用例都满足：1 ≤ a ≤ 12，1 ≤ b ≤ 5，1 ≤ c ≤ 7，1850 ≤ y1, y2 ≤ 2050。
"""


def is_leap(_year):
    return (_year % 4 == 0 and _year % 100 != 0) or (_year % 400 == 0)


a, b, c, y1, y2 = list(map(int, input().split()))
year_prefixsum = {}
month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
month_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
month_prefixsum = {1: 0, 2: 31, 3: 28, 4: 31, 5: 30, 6: 31, 7: 30, 8: 31, 9: 31, 10: 30, 11: 31, 12: 30}
for i in range(2, 13):
    month_prefixsum[i] += month_prefixsum[i-1]
for year in range(y1+1, y2+1):
    if is_leap(year-1):
        year_prefixsum[year] = 366
    else:
        year_prefixsum[year] = 365
day_1850toy1 = 0
for year in range(1850, y1):
    if is_leap(year):
        day_1850toy1 += 366
    else:
        day_1850toy1 += 365
year_prefixsum[y1] = day_1850toy1
for year in range(y1+1, y2+1):
    year_prefixsum[year] += year_prefixsum[year-1]
for year in range(y1, y2+1):
    daysum = year_prefixsum[year] + month_prefixsum[a]
    if a > 3 and is_leap(year):
        daysum += 1
    week = (daysum + 2) % 7
    if week == 0:
        week = 7

    day = 7 * (b - 1) + (c - week) % 7 + 1
    if is_leap(year):
        if day > month_leap[a]:
            print('none')
        else:
            print(f'{year}/{a:02d}/{day:02d}')
    else:
        if day > month[a]:
            print('none')
        else:
            print(f'{year}/{a:02d}/{day:02d}')

