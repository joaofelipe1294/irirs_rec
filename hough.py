from base_loader import BaseLoader
from utils.segmentation import Segmentation
import cv2
import numpy as np
import math	
import PIL


def threshold(image , val=255):
	height , width = image.shape
	for line in range(0 , height):
		for column in range(0 , width):
			if image.item(line , column) != val:
				image.itemset((line , column), 0)
			else:
				image.itemset((line , column) , 255)
	#cv2.imshow('mask' , image)
	#cv2.waitKey(0)




base = BaseLoader('CASIA-Iris-Lamp-100')
subject = base.subjects[0]
image_path = subject.left_image_paths[0]
segmentation = Segmentation(image_path=image_path , ray=47)
segmentation.pre_process()
segmentation.houghs_transform()

pre_processed_image = segmentation.pre_processed_image
equalized_image = cv2.equalizeHist(pre_processed_image)
centroid = segmentation.pupil_centroid
ray = segmentation.ray
#print(centroid)
#print(ray)
line_init = centroid[0] - ray
line_end = centroid[0] + ray
column_init = centroid[1] - ray
column_end = centroid[1] + ray
cut_image = equalized_image[line_init:line_end , column_init:column_end ]
#print(cut_image)
cut_image = np.array(cut_image , np.uint8)
#cv2.imshow('sub_image' , cut_image)
#cv2.waitKey(0)
sum_values = []
for increment_size in range(0,80):
	new_line_init = line_init - increment_size
	new_line_end = line_end + increment_size
	new_column_init = column_init - increment_size
	new_column_end = column_end + increment_size
	cut_image = equalized_image[new_line_init:new_line_end , new_column_init:new_column_end]
	cut_image = np.array(cut_image , np.uint8)
	copy_image = cut_image.copy()
	height , width = copy_image.shape
	#print(centroid)
	cv2.circle(copy_image , tuple([height / 2 , width / 2]) , ray + increment_size , 255 , -1)
	#print('line : ' + str(new_line_init) + ' - ' + str(new_line_end) + ' | column : ' + str(new_column_init) + ' - ' + str(new_column_end) + ' | count : ' + str(increment_size))
	threshold(copy_image)
	#cv2.imshow('mask_init' , copy_image)
	#cv2.imshow('sub_image' , cut_image)
	masked_image = cut_image & copy_image
	sum_values.append(np.sum(masked_image))
	#cv2.imshow('comparing' , masked_image)
	#cv2.waitKey(0)

print(sum_values)