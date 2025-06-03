import matplotlib.pyplot as plt
import numpy as np

# 生成一个 102x128 的全零矩阵
data = np.zeros((128, 128))

# 设置两个关注区域的中心点
center_row1, center_col1 = 100, 35  # 第一个中心点
center_row2, center_col2 = 80, 65  # 第二个中心点

# 设置不同方向的标准差，控制渐变的形状
sigma_x1, sigma_y1 = 7, 15  # 第一个中心点的标准差
sigma_x2, sigma_y2 = 5, 3 # 第二个中心点的标准差

# 创建一个网格，计算每个点到两个中心点的距离
rows, cols = np.meshgrid(np.arange(data.shape[0]), np.arange(data.shape[1]), indexing='ij')

# 计算第一个中心点的距离衰减
distance1 = ((rows - center_row1)**2 / (2 * sigma_y1**2)) + ((cols - center_col1)**2 / (2 * sigma_x1**2))
data1 = np.exp(-distance1)

# 计算第二个中心点的距离衰减
distance2 = ((rows - center_row2)**2 / (2 * sigma_y2**2)) + ((cols - center_col2)**2 / (2 * sigma_x2**2))
data2 = np.exp(-distance2)

# 合并两个中心点的区域
data = data1 + data2

# 引入随机扰动，使得每个点的衰减方式有所不同
random_variation = np.random.normal(0, 0.2, data.shape)  # 加入随机波动
data += random_variation

# 归一化数据，确保数值在 [0, 1] 范围内
data = np.clip(data, 0, 1)

# 添加更复杂的噪声效果
noise = np.random.normal(0, 0.05, data.shape)  # 正态分布噪声
data += noise

# 归一化数据，确保数值在 [0, 1] 范围内
data = np.clip(data, 0, 1)

# 创建一个新的画布
plt.figure(figsize=(10, 8))

# 使用imshow绘制热力图
plt.imshow(data, cmap='coolwarm', interpolation='nearest')

# 关闭坐标轴和标签
plt.axis('off')

# 显示图形
plt.show()
