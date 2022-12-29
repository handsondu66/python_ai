import numpy as np
from sklearn.neighbors import KNeighborsClassifier   # K近邻法
from sklearn.datasets import load_iris   # 鸢尾花数据集
from sklearn.model_selection import train_test_split   # 分割训练集和测试集

def load_datasets():
    iris = load_iris()
    data = iris.data    # 数据
    label = iris.target   # 标签
    # 返回值: 训练数据、测试数据、训练标签，测试标签
    x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.2)
    return x_train, x_test, y_train, y_test

if __name__ == "__main__":
    # 加载数据集
    x_train, x_test, y_train, y_test = load_datasets()
    # 创建KNN模型
    model = KNeighborsClassifier(n_neighbors=11)
    # 带入训练集到模型中
    model.fit(x_train, y_train)
    # 对测试集预测
    y_pre = model.predict(x_test)
    print("True: ", y_test)
    print("Pred: ", y_pre)



