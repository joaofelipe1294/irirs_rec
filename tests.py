from base_loader import BaseLoader
from utils.pre_processor import PreProcessor
import cv2
import numpy as np


def pupil_detection(image_path):
	image = cv2.imread(image_path , 0)
	pre_processed_image = PreProcessor.process(image_path)
	threshold_image = cv2.threshold(pre_processed_image , 28 , 255 , cv2.THRESH_BINARY)[1]
	#threshold_image = cv2.bitwise_not(threshold_image)
	edges = cv2.Canny(threshold_image , 100 , 200)
	circles = cv2.HoughCircles(pre_processed_image , cv2.HOUGH_GRADIENT , 1 , 20 , param1=50 ,param2=30 , minRadius=43 , maxRadius=49)
	print(circles[0])
	circles = np.uint16(np.around(circles))
	for i in circles[0,:]:
		cv2.circle(image,(i[0],i[1]) , i[2] ,(0 ,255 , 0) ,2)
		cv2.circle(image , (i[0] , i[1]) , 2 , (0 , 0 , 255) , 3)
	cv2.imshow('image' , image)
	#cv2.imshow('threshold image' , threshold_image)
	#cv2.imshow('pre_processed image' , pre_processed_image)
	#cv2.imshow('edges' , edges)
	cv2.waitKey(0)





base = BaseLoader('CASIA-Iris-Lamp-100')
subject = base.subjects[0]
image_path = subject.left_image_paths[0]
pupil_detection(image_path)


""" mostra todas as imagens pre processadas ""
base = BaseLoader('CASIA-Iris-Lamp-100')
for subject in base.subjects:
	print(subject.subject_id)
	images = subject.left_image_paths + subject.right_image_paths
	for image_path in images:
		original_image = cv2.imread(image_path , 0)
		pre_processed_image = PreProcessor.process(image_path)
		show = np.concatenate((original_image , pre_processed_image) , axis=1)
		cv2.imshow('resault' , show)
		cv2.waitKey(1000)
"""""""""""""""""""""""""""""""""""""""""""""""