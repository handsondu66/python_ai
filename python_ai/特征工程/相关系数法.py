import numpy as np
# 选择最优K个特征， 分类， 回归
from sklearn.feature_selection import SelectKBest, f_classif, f_regression
# 判断特征与目标的相关性
data = np.array([      # 特征
    [23, 45, 9, 89, 12],
    [34, 12, 20, 90, 10],
    [2, 23, 16, 78, 8],
    [34, 50, 15, 95, 20]
])

label = np.array([0, 1, 1, 0])       # 目标/标签

# 相关系数法
selector = SelectKBest(f_classif, k=3)   # 保留最优的3个特征
data1 = selector.fit_transform(data, label)
print(data1)
print("相关系数: ", selector.pvalues_)  # 相关性越强，p值越小