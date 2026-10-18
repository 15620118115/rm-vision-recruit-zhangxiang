import cv2
import numpy as np

# 读取刚才得到的标定结果
data = np.load("calib_result.npz")
mtx = data["mtx"]
dist = data["dist"]

# 选一张标定图片
img = cv2.imread("calib_img/0.jpg")
h, w = img.shape[:2]

# 计算去畸变后的最优相机矩阵
new_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

# 执行去畸变
dst = cv2.undistort(img, mtx, dist, None, new_mtx)

# 保存两张对比图
cv2.imwrite("origin.jpg", img)
cv2.imwrite("undistort.jpg", dst)

print("已生成原图 origin.jpg 和去畸变图 undistort.jpg")
