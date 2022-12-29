import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler   # 归一化

data = np.array([
    [24, 3000],
    [25, 3100],
    [26, 3000],
    [27, 2800],
    [30, 3500]
])

# 归一化
scaler = MinMaxScaler()
data1 = scaler.fit_transform(data)

plt.subplot(121)
plt.scatter(data[:, 0], data[:, 1])
plt.subplot(122)
plt.scatter(data1[:, 0], data1[:, 1])
plt.show()

