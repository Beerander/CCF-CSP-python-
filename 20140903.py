"""
问题描述
　　给出一个字符串和多行文字，在这些文字中找到字符串出现的那些行。你的程序还需支持大小写敏感选项：当选项打开时，表示同一个字母的大写和小写看作
不同的字符；当选项关闭时，表示同一个字母的大写和小写看作相同的字符。
输入格式
　　输入的第一行包含一个字符串S，由大小写英文字母组成。
　　第二行包含一个数字，表示大小写敏感的选项，当数字为0时表示大小写不敏感，当数字为1时表示大小写敏感。
　　第三行包含一个整数n，表示给出的文字的行数。
　　接下来n行，每行包含一个字符串，字符串由大小写英文字母组成，不含空格和其他字符。
输出格式
　　输出多行，每行包含一个字符串，按出现的顺序依次给出那些包含了字符串S的行。
样例输入
Hello
0
5
HelloWorld
HiHiHelloHiHi
GrepIsAGreatTool
HELLO
HELLOisNOTHello

样例输出
HelloWorld
HiHiHelloHiHi
HELLOisNOTHello
样例说明
　　在上面的样例中，第四个字符串虽然也是Hello，但是大小写不正确。如果将输入的第二行改为0，则第四个字符串应该输出。
评测用例规模与约定
　　1<=n<=100，每个字符串的长度不超过100。
"""
pattern = input()
is_sensitive = int(input())
n = int(input())
if not is_sensitive:
    pattern = pattern.upper()
for _ in range(n):
    input_str = input()
    if is_sensitive:
        if pattern in input_str:
            print(input_str)
    else:
        input_str_upper = input_str.upper()
        if pattern in input_str_upper:
            print(input_str)
