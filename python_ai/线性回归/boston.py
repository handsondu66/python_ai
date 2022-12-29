import numpy as np
from sklearn.datasets import load_boston   # 波士顿房价数据集
from sklearn.linear_model import LinearRegression  # 线性回归


def load_datasets():
    boston = load_boston()
    data = boston.data      # 数据
    label = boston.target   # 标签
    print(data.shape)
    print(label.shape)

if __name__ == "__main__":
    # 加载数据集
    load_datasets()
    # 创建线性回归模型
    # 带入训练集训练
    # 预测模型



