"""
问题描述
　　用 ASCII 字符来画图是一件有趣的事情，并形成了一门被称为 ASCII Art 的艺术。例如，下图是用 ASCII 字符画出来的 CSPRO 字样。
　　..____.____..____..____...___..
　　./.___/.___||.._.\|.._.\./._.\.
　　|.|...\___.\|.|_).|.|_).|.|.|.|
　　|.|___.___).|..__/|.._.<|.|_|.|
　　.\____|____/|_|...|_|.\_\\___/.
　　本题要求编程实现一个用 ASCII 字符来画图的程序，支持以下两种操作：
　　 画线：给出两个端点的坐标，画一条连接这两个端点的线段。简便起见题目保证要画的每条线段都是水平或者竖直的。水平线段用字符 - 来画，竖直线段用字
符 | 来画。如果一条水平线段和一条竖直线段在某个位置相交，则相交位置用字符 + 代替。
　　 填充：给出填充的起始位置坐标和需要填充的字符，从起始位置开始，用该字符填充相邻位置，直到遇到画布边缘或已经画好的线段。注意这里的相邻位置只需
要考虑上下左右 4 个方向，如下图所示，字符 @ 只和 4 个字符 * 相邻。
　　.*.
　　*@*
　　.*.
输入格式
　　第1行有三个整数m, n和q。m和n分别表示画布的宽度和高度，以字符为单位。q表示画图操作的个数。
　　第2行至第q + 1行，每行是以下两种形式之一：
　　 0 x1 y1 x2 y2：表示画线段的操作，(x1, y1)和(x2, y2)分别是线段的两端，满足要么x1 = x2 且y1 ≠ y2，要么 y1 = y2 且 x1 ≠ x2。
　　 1 x y c：表示填充操作，(x, y)是起始位置，保证不会落在任何已有的线段上；c 为填充字符，是大小写字母。
　　画布的左下角是坐标为 (0, 0) 的位置，向右为x坐标增大的方向，向上为y坐标增大的方向。这q个操作按照数据给出的顺序依次执行。画布最初时所有位置都
是字符 .（小数点）。
输出格式
　　输出有n行，每行m个字符，表示依次执行这q个操作后得到的画图结果。
样例输入
4 2 3
1 0 0 B
0 1 0 2 0
1 0 0 A
样例输出
AAAA
A--A
样例输入
100 100 10
0 3 1 12 1
0 12 1 12 3
0 12 3 6 3
0 6 3 6 9
0 6 9 12 9
0 12 9 12 11
0 12 11 3 11
0 3 11 3 1
1 4 2 C
1 0 0 B
样例输出
................
...+--------+...
...|CCCCCCCC|...
...|CC+-----+...
...|CC|.........
...|CC|.........
...|CC|.........
...|CC|.........
...|CC|.........
...|CC+-----+...
...|CCCCCCCC|...
...+--------+...
................
评测用例规模与约定
　　所有的评测用例满足：2 ≤ m, n ≤ 100，0 ≤ q ≤ 100，0 ≤ x < m（x表示输入数据中所有位置的x坐标），0 ≤ y < n（y表示输入数据中所有位置的y坐标）。
"""
m, n, q = list(map(int, input().split()))
drawmap = [['.'] * m for _ in range(n)]
instructs = []
stop = ['-', '|', '+']
for _ in range(q):
    instructs.append(input().split())


for instruct in instructs:
    if instruct[0] == '0':  # 画线段
        x1, y1, x2, y2 = list(map(int, instruct[1:]))
        y1, y2 = n - 1 - y1, n - 1 - y2
        if x1 == x2:  # 画竖线
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                if drawmap[y][x1] == '-':
                    drawmap[y][x1] = '+'
                else:
                    drawmap[y][x1] = '|'
        else:  # 划横线
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                if drawmap[y1][x] == '|':
                    drawmap[y1][x] = '+'
                else:
                    drawmap[y1][x] = '-'
    else:  # 填充字符（大小写字母）
        x, y = list(map(int, instruct[1:-1]))
        y = n-1 - y
        c = instruct[-1]
        loop_list = [[x, y, c]]
        while loop_list:
            x_, y_, c_ = loop_list.pop()
            for right in range(x_ + 1, m):
                if drawmap[y_][right] in stop or drawmap[y_][right] == c_:
                    break
                drawmap[y_][right] = c_
                loop_list.append([right, y_, c_])
            for left in range(x_ - 1, -1, -1):
                if drawmap[y_][left] in stop or drawmap[y_][left] == c_:
                    break
                drawmap[y_][left] = c_
                loop_list.append([left, y_, c_])
            for down in range(y_ + 1, n):
                if drawmap[down][x_] in stop or drawmap[down][x_] == c_:
                    break
                drawmap[down][x_] = c_
                loop_list.append([x_, down, c_])
            for up in range(y_ - 1, -1, -1):
                if drawmap[up][x_] in stop or drawmap[up][x_] == c_:
                    break
                drawmap[up][x_] = c_
                loop_list.append([x_, up, c_])
for x in range(n):
    for y in range(m):
        print(drawmap[x][y], end='')
    print()


# def loop(x_, y_, c_):
#     # 对接受的坐标进行四个方向的循环，循环内容：
#     # 如果没有满足停止条件，则将该位置变为填充字符，并令该坐标也进行一次四方向循环
#     # 停止条件：1、碰到线段 2、越界 3、碰到填充字符
#     for right in range(x_ + 1, m):
#         if drawmap[y_][right] in stop or drawmap[y_][right] == c_:
#             break
#         drawmap[y_][right] = c_
#         loop(right, y_, c_)
#     for left in range(x_ - 1, -1, -1):
#         if drawmap[y_][left] in stop or drawmap[y_][left] == c_:
#             break
#         drawmap[y_][left] = c_
#         loop(left, y_, c_)
#     for down in range(y_ + 1, n):
#         if drawmap[down][x_] in stop or drawmap[down][x_] == c_:
#             break
#         drawmap[down][x_] = c_
#         loop(x_, down, c_)
#     for up in range(y_ - 1, -1, -1):
#         if drawmap[up][x_] in stop or drawmap[up][x_] == c_:
#             break
#         drawmap[up][x_] = c_
#         loop(x_, up, c_)



