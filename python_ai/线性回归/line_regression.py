import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression   # 线性回归

def load_datasets():
    x = np.random.uniform(0., 80., (200, 1))   # 200行1列的[0~80]随机浮点数
    w = 0.9
    b = 15
    y = w*x + b
    x = np.random.normal(x, 2)   # 正态分布
    y = np.random.normal(y, 2)   # 正态分布
    return x, y


def show_data(x, y):
    plt.scatter(x, y)
    plt.show()


if __name__ == "__main__":
    # 加载数据集
    x, y = load_datasets()
    # 创建线性回归模型
    model = LinearRegression()
    # 带入训练集训练
    model.fit(x, y)
    print("w is: ", model.coef_)     # 权重
    print("b is: ", model.intercept_)  # 偏置
    w = model.coef_
    b = model.intercept_
    plt.plot(x, w*x+b, c='r', linewidth=5)
    # 带入测试集验证
    x_test = np.array([[20]])
    y_pre = model.predict(x_test)
    print("y_pre: ", y_pre)
    # 显示数据
    show_data(x, y)

