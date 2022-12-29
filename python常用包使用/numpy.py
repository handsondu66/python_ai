# python常用包 --- numpy
# 导包
import numpy as np

# 创建numpy数组
# a = np.array([1., 2., 3., 4., 5., 6., 7., 8., 9., 10.])
# b = np.array([[1, 2, 3, 4],
#               [5, 6, 7, 8],
#               [9, 10, 11, 12]])
# print(a, type(a))
# print(b, type(b))
# print("轴(维)： ", a.ndim, b.ndim)   # 1, 2
# print("维度: ", a.shape, b.shape)    # (10,) (3, 4)
# print("总元素个数: ", a.size, b.size)  # 10, 12
# print("元素类型: ", a. dtype, b.dtype)  # float64, int32

# m = np.arange(10, dtype=float)   # 生成连续的数组
# print(m)
# n = np.arange(10, 100, 10)  # [10 20 30 40 50 60 70 80 90] [start, stop, step)
# print(n)
# x = np.reshape(m, (2, 5))   # 更改维度
# print(x)
# y = x.reshape((10, ))   # 改成一维数组
# print(y)
# z = n.reshape((3, -1))   # 改成(3, 3)数组
# print(z, z.shape)
#
# a = np.zeros((3, 4), dtype=float)   # 生成全为0的数组
# print(a, a.shape)

# numpy的运算
import numpy as np

# a = np.array([[1, 2], [1, 2]])
# b = np.array([[1, 2], [1, 2]])
# c = a + b
# print(c)
# c = a - b
# print(c)
# c = a * b
# print(c)
# c = a / b    # 结果为浮点数
# print(c)
# c = a // b   # 整除运算
# print(c)
# print(np.sum(a))   # 和
# print(np.max(a))   # 最大值
# print(np.min(a))   # 最小值
# print(a.mean())    # 平均值

# a = np.array([[1, 2], [1, 2]])
# b = np.array([[1, 2], [1, 2]])
# m = np.hstack((a, b))    # 按行合并
# print(m)
# n = np.vstack((a, b))    # 按列合并
# print(n)

# 切片
# # 一维数组
# a = np.array([10, 5, -9, 2, 5, 12, 0, 23, 9, -7])
# print(a, a.shape)
# print(a[0], a[-1], a[:3], a[3:])
# a[a<0] = 0    # 把所有<0的值都变成0
# print(a)

# # 二维数组
# a = np.array([[10, 9, 3, 0],
#               [4, 5, -9, 2],
#               [4, 0, 3, 6]])
# print(a, a.shape)
# print(a[0], a[1], a[2])   # 访问每一行
# print(a[:, 0], a[:, 1], a[:, 2], a[:, 3])   # 访问每一列
# print(a[0][0], a[0, 0])   # 访问第0行第0列元素
# print(a[1, 1:])   # [ 5 -9  2]
# print(a[1:, 1:])   # [[ 5 -9  2], [ 0  3  6]]