'''
1、string/bytes    不可变类型
    str = "hello world"
    str[start:stop:step]    左闭右开
    find  --- 查找子串的位置，找不到返回-1
    index --- 查找子串的位置，找不到报错
    count --- 查找某字串出现的次数
    +  --- 字符串连接
    *n --- n个字符串

    str --》bytes： encode
    bytes --》str： decode

2、列表List  []  可变类型
    切片方式与字符串相同
    增：
        insert --- 在指定位置插入元素
        append --- 在末尾追加元素
    删:
        pop  --- 按位置删除
        remove --- 按元素删除第一个匹配项
    改:
        list[下标] = value
    查:
        index --- 查找某元素的位置，找不到报错
        count --- 查找某元素出现的次数

3、元组Tuple  ()   不可变类型
    切片方式与列表相同
    index --- 查找某元素的位置，找不到报错
    count --- 查找某元素出现的次数

4、字典dictionary  {}   可变类型
    dict = {键值对, 键值对, ......}
    访问: dict[键]
    增：
        dict[新键] = value
    删：
        pop(键)  -- 按键删除键值对
    改：
        dict[旧键] = value
    查：
        keys  --- 键
        values  --- 值
        items --- 键值对

5、函数
    函数的定义的一般形式：
        def 函数名(形参列表):
            函数体
            return 返回值列表

    调用：
        函数名(实参列表)
        变量 = 函数名(实参列表)  --- 接收返回值

    默认参数值
    关键字传参
        print(sep=分隔符， end=结束符)
    局部变量和全局变量
        global 全局变量

6、类与对象
    class 类名:
        def __init__(self):   构造器
            成员属性
        def __del__(self):    析构器
            回收资源
        成员方法
        def 函数名(self)：
            函数体

    定义对象: 对象 = 类名(向构造器传参)
    访问成员: 对象.成员

7、文件
    open  --- 打开文件
    close  --- 关闭文件
    read/readline/readlines --- 读取文件内容
    write --- 写入文件内容

    with open as fd:  --- 用完文件后文件自动关闭
'''

# python基本类型 ---- string/bytes 字符串类型    不可变类型
# str = "hello world"
# print(str)
# print(str[0], str[1], str[-1])   # h e d,下标负数表示从后往前数
# print(str[0:3])   # 字符串切片[start:stop:step], 左闭右开
# print(str[0:5], str[3:], str[::2])  # 前5个, 除前3个， 隔一个取一个
#
# print(str + " nihao!")   # 字符串连接
# print(str * 2)     # 两个str
#
# print("字符串的长度: ", len(str))
# print(str.find("world"))  # 查找子串，返回子串首地址, 找不到返回-1
# print(str.index("world"))   # 查找子串，返回子串首地址, 找不到报错
# print(str.count('l'))   # 查找某元素出现的次数
# print(str.split(" "))   # 分割字符串， 按空格分割
#
# # str与bytes转换
# sstr = "hello 世界"
# bstr = b"hello"     # bytes类型不能带中文, 通信时需要使用bytes类型
# print(sstr, bstr)
# print(type(sstr), type(bstr))
#
# bs = sstr.encode(encoding='utf-8')   # 把str转化成bytes类型
# print(bs, type(bs))
# ss = bs.decode(encoding='utf-8')   # 把bytes转化回str类型
# print(ss, type(ss))

# python类型   ---- 列表 List  可变类型
# list = [1, 2, 3, 3, 1.3, "hello", [10, 11, 12]]
# print(list)
# print(list[0], list[-1], list[:3])   # 列表的切片与字符串一样
# print("字符串的长度: ", len(list))
# # 增
# list.insert(1, 1000)   # 在index位置插入元素1000
# list.append(-9)    # 在末尾追加元素
# # 删
# list.pop(0)   # 按位置删除，默认删除最后一个元素
# list.remove(3)   # 按元素删除第一个匹配项
# print(list)
# # 改
# list[0] = 100
# print(list)
# # 查
# print(list.index(2))  # 查找某元素的位置，不存在报错
# print(list.count(2))  # 查找某元素出现的次数

# 练习: 使用列表求斐波拉契数列的前10个元素  [1 1 2 3 5 8 13 21 34 55]
# fib = [1, 1]
# for i in range(2, 10):
#     fib.append(fib[i-2] + fib[i-1])
# print(fib)

# # python类型  ---- 元组Tuple  ()  不可变类型
# tup = (1, 1.23, 1, "hello", (10, 11), [21, 22, 23])
# print(tup, tup[0], tup[-1])
# print(tup[-1][1])   # 22    元组切片方式与列表相同
#
# print("元素个数: ", len(tup))
# print("查找某元素的位置: ", tup.index("hello"))  # 找不到报错
# print("查找某元素出现的次数: ", tup.count(1))

# # python类型  ---- 字典dictionary  {} 键值对  可变类型
# dict = {"name": "Lucy", "age": 20, "height": 1.65}
# print(dict)
# print(dict["name"])   # 字典通过键访问值
# # 增
# dict['sex'] = "female"   # 自动在末尾添加新的键值对
# # 删
# dict.pop('height')   # 按键删除键值对
# # 改
# dict['age'] = 21   # 当键是新的就是新增，否则就是修改
# # 查
# print(dict)
# for key in dict.keys():  # 获取所有的键
#     print(key)
# for value in dict.values():   # 获取所有的值
#     print(value)
# for item in dict.items():    # 获取所有的键值对
#     print(item)
# for key, value in dict.items():
#     print(key, ": ", value)

# python函数
# def myadd(a, b):    # 函数定义
#     """
#     :param a: 被加数
#     :param b: 加数
#     :return: 两个数之和
#     """
#     return (a+b)    # 返回值
#
# # 有默认值的参数可以传参也可以不传参，不传参则使用默认值，传参使用传进去的值
# def myadd1(x, y, z=100):   # 默认参数值， 从后往前设置
#     return (x+y+z)
#
# def swap(x, y):
#     return y, x    # python可以返回多个值
#
#
# # 函数的调用
# sum = myadd(10, 20)
# print(sum)
#
# print(myadd1(10, 20))
# print(myadd1(10, 20, 30))
# print(myadd1(z=0, x=10, y=20))  # 关键字传参，可以打乱顺序传参
#
# m = 10
# n = 20
# m, n = swap(m, n)
# print(m, n)
#
# a = 10
#
# def func(m):
#     print(m)   # 10
#     m = 100
#     print(m)   # 100
#
# def func1():
#     global a   # 声明使用全局的a
#     a = 100
#     print(a)  # 100
#
# func(a)
# print(a)   # 10
#
# func1()
# print(a)   # 100

# 练习: 封装一个函数，求列表元素之和
# list = [0, -9, 2, 3, 8, 10, 2, 3, -10, 23, 45]
#
# def list_sum(list):
#     n = len(list)
#     sum = 0
#     for i in range(n):
#         sum += list[i]
#     return sum
#
# sum = list_sum(list)
# print("列表元素之和: ", sum)

# 面向对象
# class Animal:   # 定义类
#     # 构造器： 初始化对象， 当对象被创建时
#     def __init__(self, name="", age=0):
#         self.name = name
#         self.age = age
#         print("Animal.__init__")
#     # 析构器： 回收资源， 当对象被销毁时
#     def __del__(self):
#         print("Animal.__del__")
#     def info(self):
#         print("这是一个动物类, name: {}, age: {}".format(self.name, self.age))
#
# # 定义对象
# # cat = Animal()
# cat = Animal("猫咪", 2)
# cat.info()   # 对象访问成员

# # 练习： 封装一个矩形类，求矩形的周长与面积
# class Rect:
#     def __init__(self, w=1, h=1):
#         self.width = w
#         self.height = h
#
#     def getLength(self):
#         return (self.width+self.height)*2
#
#     def getArea(self):
#         return (self.width * self.height)
#
#
# rect = Rect(10, 20)
# print("矩形周长： ", rect.getLength())
# print("矩形面积： ", rect.getArea())

# python 文件操作
# 以只写方式打开文件1.txt
# fd = open("1.txt", "w", encoding='utf-8')
# # 向文件中写入内容
# str = "hello world\n nihao\n\n 世界, 你好!"
# fd.write(str)
# # 关闭文件
# fd.close()

# with打开文件会自动关闭文件
# with open("1.txt", "r", encoding='utf-8') as fd:
#     # 读取文件内容并打印在屏幕上
#     # data = fd.read()
#     # print(data)
#
#     # 按行循环读取
#     # while True:
#     #     line = fd.readline()
#     #     if not line:   # 判断是否读取到文件内容
#     #         break
#     #     print(line, end='')
#
#     # 读取文件所有的行
#     lines = fd.readlines()
#     for line in lines:
#         print(line, end="")

