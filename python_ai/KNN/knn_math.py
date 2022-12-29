import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier  # K近邻法

def load_datasets():
    data = np.array([
        [0.2, 0.6],
        [1.2, 8.1],
        [2.8, 9.5],
        [3.5, 5.8],
        [4.2, 9.],
        [4.9, 2.],
        [5.2, 9.2],
        [6.8, 3.],
        [8., 8.5],
        [8.2, 0.]
    ])
    label = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1])
    data_test = np.array([[4.5, 0]])
    return data, label, data_test


def show_data(data, label, data_test):
    plt.scatter(data[:6, 0], data[:6, 1], s=30, c='b')
    plt.scatter(data[6:, 0], data[6:, 1], s=30, c='r')
    plt.scatter(data_test[0, 0], data_test[0, 1], s=30, c='g')
    plt.show()


# 当文件直接执行时才会执行内部的代码
if __name__ == "__main__":
    # 加载数据集
    data, label, data_test = load_datasets()
    # 创建KNN模型
    model = KNeighborsClassifier(n_neighbors=1)
    # 带入训练集到模型
    model.fit(data, label)
    # 预测
    y_pre = model.predict(data_test)
    print("Pred: ", y_pre)

    show_data(data, label, data_test)




