# python包 --- matplotlib
# import numpy as np
# import matplotlib.pyplot as plt    # 2D绘图
#
# x = np.array([1, 2])
# y = np.array([1, 2])
#
# # # plt.scatter(x, y)   # 描点
# # plt.scatter(x, y, s=100, c='r', marker='s')  # 描点：x轴、y轴、大小、颜色、形状
# # # plt.plot(x, y)      # 连线
# # plt.plot(x, y, c='g', linewidth=5)   # 连线： 颜色、线宽
# # plt.show()          # 显示
#
# plt.subplot(121)   # 绘制子图：共几行共几列第几张图
# plt.xlabel("x")    # x轴标签
# plt.ylabel("y")    # y轴标签
# plt.xlim(-1, 5)    # x轴范围
# plt.title("scatter")  # 标题
# plt.scatter(x, y, s=50, c='b', marker='*')
# plt.subplot(122)   # 一行两列第2张图
# plt.plot(x, y, c='r', linewidth=3)
# plt.show()