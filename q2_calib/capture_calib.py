import cv2
import os

if not os.path.exists("calib_img"):
    os.makedirs("calib_img")

cap = cv2.VideoCapture(0)
img_index = 0
print("按 S 保存图片，按 Q 退出")

while True:
    ret, frame = cap.read()
    if not ret:
        print("摄像头打不开，检查一下")
        break
    cv2.imshow("拍标定图 S保存 Q退出", frame)
    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite(f"calib_img/{img_index}.jpg", frame)
        print(f"保存了第 {img_index} 张")
        img_index += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
