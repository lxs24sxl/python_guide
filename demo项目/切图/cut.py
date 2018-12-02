import cv2  # [1]导入OpenCv开源库
import numpy as np
 
image_path = "F:\\11111111111111111111111111111\\100000.jpg"
srcImg = cv2.imread(image_path)  # [2]将图片加载到内存
 
cv2.namedWindow("[srcImg]", cv2.WINDOW_AUTOSIZE)  # [3]创建显示窗口
cv2.imshow("[srcImg]", srcImg)  # [4]在刚才创建的显示窗口中显示刚在加载的图片
cv2.waitKey(0)
 
# ========================================================================================================
# 模块说明:
#       由于OpenCv中,imread()函数读进来的图片,其本质上就是一个三维的数组,这个NumPy中的三维数组是一致的,所以设置图片的  
#   ROI区域的问题,就转换成数组的切片问题,在Python中,数组就是一个列表序列,所以使用列表的切片就可以完成ROI区域的设置  
# ========================================================================================================
image_save_path_head = "F:\\11111111111111111111111111111\\111\\cat_ROI_"
image_save_path_tail = ".jpg"
seq = 1
for i in range(2):  # [1]480*360==15*11---height
    for j in range(2):  # [2]column-----------width
        img_roi = srcImg[(i * 112):((i + 1) * 112), (j * 112):((j + 1) * 112)]
        image_save_path = "%s%d%s" % (image_save_path_head, seq, image_save_path_tail)##将整数和字符串连接在一起
        cv2.imwrite(image_save_path, img_roi)
        seq = seq + 1