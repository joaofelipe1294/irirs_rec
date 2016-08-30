from base_loader import BaseLoader
from utils.pre_processor import PreProcessor
import cv2
import numpy as np
import math

base = BaseLoader('CASIA-Iris-Lamp-100')
subject = base.subjects[0]
image_path = subject.left_image_paths[0]

image = cv2.imread(image_path , 0)
pre_processed_image = PreProcessor.process(image_path)
threshold_image = cv2.threshold(pre_processed_image , 28 , 255 , cv2.THRESH_BINARY)[1]
edges = cv2.Canny(threshold_image , 100 , 200)
rows , cols = edges.shape[:2]
ray = 47
hough_image = np.zeros((rows , cols) , np.uint8)
print('linhas : ' + str(cols))
for i in range(0 , rows):
	for j in range(0 , cols):
		if edges[i][j] == 255:
			for teta in range(0,359):

				xt = j - (ray - math.cos(teta))
				yt = i - (ray - math.sin(teta))
				print('xt : ' + str(int(xt)) + ' | yt : ' + str(int(yt)) + ' | i:' + str(i) + ' j:' + str(j))
				hough_image[int(yt)][int(xt)] += 1
				#print('XT : ' + str(xt) + ' | YT : ' + str(yt))
#while i < rows - 1:
#	print(image[i][0])
#	i += 1

cv2.imshow('hough_image' , hough_image)
cv2.waitKey(0)


#cv2.imshow('image' , image)
#cv2.imshow('threshold image' , threshold_image)
#cv2.imshow('pre_processed image' , pre_processed_image)
#cv2.imshow('edges' , edges)
#cv2.waitKey(0)
