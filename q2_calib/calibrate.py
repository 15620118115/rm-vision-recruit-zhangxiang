import cv2
import numpy as np
import os

# ====================== 必须修改这里！ ======================
# 棋盘格内角点数量，9x6不用改
pattern_size = (9, 6)
# 你量的单个方格边长，单位是米！比如20毫米就填0.020
square_size = 0.018
# ========================================================

# 生成棋盘格的三维世界坐标
objp = np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2) * square_size

obj_points = []
img_points = []

img_folder = "./calib_img"
img_files = [f for f in os.listdir(img_folder) if f.endswith(".jpg")]
print(f"找到 {len(img_files)} 张标定图片")

for fname in img_files:
    img = cv2.imread(os.path.join(img_folder, fname))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)
    
    if ret:
        obj_points.append(objp)
        # 亚像素精确化
        corners_sub = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1),
                                       (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))
        img_points.append(corners_sub)
        print(f"{fname}：识别成功")
    else:
        print(f"{fname}：未识别到角点，跳过")

# 执行相机标定
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)

# 打印结果
print("\n" + "="*50)
print(f"重投影误差：{ret:.4f} 像素")
print("="*50)
print("内参矩阵：")
print(mtx)
print("="*50)
print("畸变系数：")
print(dist)
print("="*50)

# 保存标定结果文件，后面测距要用
np.savez("calib_result.npz", mtx=mtx, dist=dist)
print("标定结果已保存为 calib_result.npz")
