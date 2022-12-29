"""
1、注释
    单行注释: #, 快捷键 ctrl+/
    多行注释: 三组单引号或者双引号
2、缩进
    严格缩进要求，同一个语句块要求对齐
3、变量
    变量的类型由赋的值决定， type --- 类型
    a = 10
    a, b = 1, 2.34
4、输入输出
    输入: input
        val = input(提示符)
        input输入的数据都是str类型， 需要强转成需要的类型，例: int(值)
    输出: print
        print(值列表, sep=分隔符, end=结束符)
        print("a = %d, b = %f" % (a, b))
        print("a = {}, b = {}".format(a, b))
5、控制语句
    分支语句
        if....else
        if....elif...else
    循环语句
        while 条件语句:
            循环体
        for 变量 in 字符串/列表:
            循环体
    循环控制
        break: 跳出本层循环
        continue: 结束本次循环，进入下一次循环
6、python基本数据类型---numbers
    整型int:
        十进制: 100
        八进制: 0o144
        十六进制: 0x64
        二进制: 0b1100100
    浮点型 float:
        小数型: 1.345
        指数型: 1.34e-3
7、随即包
    import random
    random.random()  --- [0, 1)随机浮点数
    random.uniform(x, y)  --- [x, y]之间随机浮点数
    random.randint(x, y)  --- [x, y]之间随机整数
"""


# python注释
# 单行注释 #, 快捷键：ctrl + /
"""
多行注释三组单引号或双引号
"""

'''
C语言:
int a = 10;
if (a < 10)
    a = 100;
else
{
    a = -10;
    printf("a = %d", a);
}
'''
# # python中严格缩进，同一个代码块需要对齐
# a = 10
# if a < 10:
#     a = 100
# else:
#     a = -10
#     print(a)

# # python变量
# a = 10    # 变量的类型由赋的值决定
# b = 1.234
# c = "hello world"
# print(a, b, c)
# print(type(a), type(b), type(c))   # type---类型
# a = b = c = 1
# print(a, b, c)
# a, b = "hello", 2.34   # python中可以同时给多个变量赋值
# print(a, b)
# a, b = b, a
# print(a, b)

# python输入和输出
# 输入 input
# a = input()   # input输入的数据都是str类型
# print(a, type(a))
# a = int(a)      # 转换成int类型
# print(a, type(a))
# a = input("请输入整数: ")
# a = int(a)
# print(a)

# 输出 print
# a, b, c = 123, 2.34, "hello world"
# print(a, b, c)
# print("a = %d, b = %f, c = %s" % (a, b, c))   # 按照指定格式打印
# print("a = {}, b = {}, c = {}".format(a, b, c))
# print(a, b, c, end='***')  # end --- 结束符
# print(a, b, c, sep='#')  # sep --- 分隔符

# python控制语句
# 分支语句
# a = 10
# if a < 10:
#     print("a < 10!")
# elif 10 == a:
#     print("a == 10!")
# else:
#     print("a > 10!")

# 循环语句while
# 1- 100累加和
# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print("1-100累加和: ", sum)

# # 循环语句 for
# # for 变量  in  字符串/列表  --- 把列表字符串中每个元素依次赋给变量
# for i in [1, 2, 3]:
#     print(i)   # i - 1, 2, 3
# sum = 0
# for i in range(101):   # [0, 101)  左闭右开
#     sum += i
# print("1-100累加和: ", sum)
# sum = 0
# for i in range(0, 101, 2):   # [start, stop, step)
#     sum += i
# print("1-100所有偶数之和: ", sum)

# # 实现打印九九乘法表（while/for）
# """
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9
# ...
# 1*9=9 2*9=18 ...... 9*9=81
# """
# i = j = 1  # i-行   j-列
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("{}*{}={}".format(j, i, i*j), end='\t')
#         j += 1
#     i += 1
#     print()
#
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("{}*{}={}".format(j, i, i * j), end='\t')
#     print()

# python基本类型 ---- numbers 数字类型
# 整型 int
a = 100         # 十进制
b = 0o144       # 八进制
c = 0x64        # 十六进制
d = 0b1100100   # 二进制
print(a, b, c, d)
print(a, oct(a), hex(a), bin(a))   # 十进制、八进制、十六进制、二进制

# 浮点型 float
a = 1.2345
b = 3.456e3  # 3456
print(a, b)

# 导包  --- 随即包
import random
a = random.random()   # [0, 1) 0~1之间随机浮点数
print(a)
a = random.uniform(10, 20)   # [10, 20]之间的随机浮点数
print(a)
a = random.randint(10, 20)   # [10, 20]之间的随机整数
print(a)
