# coding=utf-8

import numpy as np
import cv2 as cv

#图片旋转
def rotate(image, angle, center=None, scale=1.0):
	(h, w) = image.shape[:2]
	if center is None:
		center = (w//2, h//2)
	M = cv.getRotationMatrix2D(center, angle,scale)
	rotated = cv.warpAffine(image, M, (w, h))
	return rotated

#图片仿射 4点映射
def affine(image):
	(cols,rows) = image.shape[:2]
	pts1 = np.float32([[0,0], [cols-1,0], [0, rows-1], [cols-1,rows-1]])
	pts2 = np.float32([[99,102], [cols-1,91], [50, rows-1], [cols-50,rows-50]])
	M = cv.getPerspectiveTransform(pts1, pts2)
	affined = cv.warpPerspective(image, M, (rows, cols))
	return affined



if __name__ == '__main__':
	image = "./pic/ex.png"
	img = cv.imread(image, 0)
	cv.imshow("ii", img)


	# rotated = rotate(img, 70)
	# cv.imshow("70", rotated)

	affined = affine(img)
	cv.imshow("2",affined)

	


	cv.waitKey(0)
	cv.destroyAllWindows()