"""
问题描述
　　某股票交易所请你编写一个程序，根据开盘前客户提交的订单来确定某特定股票的开盘价和开盘成交量。
　　该程序的输入由很多行构成，每一行为一条记录，记录可能有以下几种：
　　1. buy p s 表示一个购买股票的买单，每手出价为p，购买股数为s。
　　2. sell p s 表示一个出售股票的卖单，每手出价为p，出售股数为s。
　　3. cancel i表示撤销第i行的记录。
　　如果开盘价为p0，则系统可以将所有出价至少为p0的买单和所有出价至多为p0的卖单进行匹配。因此，此时的开盘成交量为出价至少为p0的买单的总股数和所有
出价至多为p0的卖单的总股数之间的较小值。
　　你的程序需要确定一个开盘价，使得开盘成交量尽可能地大。如果有多个符合条件的开盘价，你的程序应当输出最高的那一个。
输入格式
　　输入数据有任意多行，每一行是一条记录。保证输入合法。股数为不超过108的正整数，出价为精确到恰好小数点后两位的正实数，且不超过10000.00。
输出格式
　　你需要输出一行，包含两个数，以一个空格分隔。第一个数是开盘价，第二个是此开盘价下的成交量。开盘价需要精确到小数点后恰好两位。
样例输入
buy 9.25 100
buy 8.88 175
sell 9.00 1000
buy 9.00 400
sell 8.92 400
cancel 1
buy 100.00 50

样例输出
9.00 450
评测用例规模与约定
　　对于100%的数据，输入的行数不超过5000。
"""
import sys


input_list, record = [], []
buy, sell = {}, {}
for s in sys.stdin:
    input_str = list(s.split())
    if input_str:
        input_list.append(input_str)
        if input_str[0] == 'cancel':
            input_list[int(input_str[1]) - 1].append('1')
for log in input_list:
    if len(log) == 3:
        record.append([log[0], float(log[1]), int(log[2])])
record.sort(key=lambda xx: xx[1], reverse=True)
num = 0
for x, y, z in record[::-1]:
    if x == 'sell':
        num += z
    sell[y] = num
num = 0
for x, y, z in record:
    if x == 'buy':
        num += z
    buy[y] = num
num = 0
price = 0
for i in record:
    if min(sell[i[1]], buy[i[1]]) > num:
        price = i[1]
        num = min(sell[i[1]], buy[i[1]])
print(f'{price:.2f} {num}')
