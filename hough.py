from base_loader import BaseLoader
from utils.segmentation import Segmentation
import cv2
import numpy as np
import math	

"""base = BaseLoader('CASIA-Iris-Lamp-100')
subject = base.subjects[0]
image_path = subject.left_image_paths[0]

image = cv2.imread(image_path , 0)
pre_processed_image = PreProcessor.process(image_path)
threshold_image = cv2.threshold(pre_processed_image , 28 , 255 , cv2.THRESH_BINARY)[1]
edges = cv2.Canny(threshold_image , 100 , 200)
rows , cols = edges.shape[:2]
ray = 47
hough_image = np.zeros((rows , cols) , np.uint8)
for x in range(0 , rows):
	for y in range(0 , cols):
		if edges[x][y] == 255:
			pass
			#print('ponto : ' + str(x) + ',' + str(y))
			for teta in range(0,359):

				xt = j - (ray - math.cos(teta))
				yt = i - (ray - math.sin(teta))
				#print('xt : ' + str(int(xt)) + ' | yt : ' + str(int(yt)) + ' | i:' + str(i) + ' j:' + str(j))
				hough_image[int(yt)][int(xt)] += 1"""
				#print('XT : ' + str(xt) + ' | YT : ' + str(yt))
#while i < rows - 1:
#	print(image[i][0])
#	i += 1

#print(edges[0][292])
#for teta in range(0,359):
	#xt = 0 - ray * math.cos(teta)


#cv2.imshow('original_image' , edges)
#cv2.imshow('hough_image' , hough_image)
#cv2.waitKey(0)


#cv2.imshow('image' , image)
#cv2.imshow('threshold image' , threshold_image)
#cv2.imshow('pre_processed image' , pre_processed_image)
#cv2.imshow('edges' , edges)
#cv2.waitKey(0)


base = BaseLoader('CASIA-Iris-Lamp-100')

subject = base.subjects[0]
image_path = subject.left_image_paths[0]
rgb_image = cv2.imread(image_path)
original_image = cv2.imread(image_path , 0)
height , width = original_image.shape[:2]


segmentation = Segmentation(image_path)
segmentation.pre_process()
segmentation.houghs_transform()
"""pre_processed_image = segmentation.pre_process()
edges = cv2.Canny(pre_processed_image , 100 , 200)
#cv2.imshow('rgb_image' , rgb_image)
#cv2.imshow('edges' , edges)
#cv2.waitKey(0)



#image = np.zeros((150,150) , np.uint8)
#image[10][74] = 255
#image[74][10] = 255
#image[74][139] = 255
#image[139][74] = 255
#print(image)

hough_plan = np.zeros((height , width) , np.uint8)
ray = 47
for line in range(0,height):
	for column in range(0,width):
		if edges[line][column] == 255:
			for teta in range(0 , 360):
				xt = line - ray * math.cos(teta)
				yt = column - ray * math.sin(teta)
				#print(str(line) + '|' + str(column) + ' | teta : ' + str(teta) + ' | xt : ' + str(int(xt)) + ' | ' + str(int(yt)))
				if int(xt) < height and int(yt) < width and int(xt) > 0 and int(yt) > 0:
					hough_plan[int(xt)][int(yt)] += 1

bigger = 0
bigger_line = 0
bigger_collumn = 0
for line in range(0,height):
	#print(line)
	for column in range(0,width):
		#print(column)
		if hough_plan[line][column] >= bigger:
			bigger = hough_plan[line][column]
			bigger_line = line
			bigger_collumn = column
			#print(str(line) + ' | ' + str(column) + ' | value : ' + str(bigger))
			#cv2.circle(rgb_image , tuple([bigger_line , bigger_collumn]) , ray , (0,0,255))


cv2.circle(rgb_image , tuple([bigger_collumn , bigger_line]) , ray , (0,255,0))
cv2.circle(rgb_image , tuple([bigger_collumn , bigger_line]) , 5 , (0,0,255) , -1)
#cv2.imshow('hough_plan' , hough_plan)
cv2.imshow('image' , rgb_image)
cv2.waitKey(0)"""
