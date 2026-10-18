import numpy as np

# 模拟一个合理的笔记本摄像头内参
width = 640
height = 480
fx = 500.0
fy = 500.0
cx = width / 2
cy = height / 2

mtx = np.array([
    [fx, 0,  cx],
    [0,  fy, cy],
    [0,  0,  1]
], dtype=np.float64)

# 模拟畸变系数
dist = np.array([[0.1, -0.05, 0.001, 0.001, 0.01]], dtype=np.float64)

# 保存成和标定输出一样的格式
np.savez("calib_result.npz", mtx=mtx, dist=dist)
print("已生成模拟标定结果 calib_result.npz")
print("内参矩阵：")
print(mtx)
print("畸变系数：")
print(dist)
