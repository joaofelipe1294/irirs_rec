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
	circles = cv2.HoughCircles(pre_processed_image , cv2.HOUGH_GRADIENT , 1 , 20 , param1=50 ,param2=30 , minRadius=25 , maxRadius=50)
	print(type(circles))
	"""circles = np.uint16(np.around(circles))
	for i in circles[0,:]:
		cv2.circle(image,(i[0],i[1]) , i[2] ,(0 ,255 , 0) ,2)
		cv2.circle(image , (i[0] , i[1]) , 2 , (0 , 0 , 255) , 3)"""
	#cv2.imshow('image' , image)
	#cv2.imshow('threshold image' , threshold_image)
	#cv2.imshow('pre_processed image' , pre_processed_image)
	#cv2.imshow('edges' , edges)
	cv2.waitKey(0)





















base = BaseLoader('CASIA-Iris-Lamp-100')
for subject in base.subjects:
	print(subject.subject_id)
	left_image_path = subject.left_image_paths[0]
	#image_left = PreProcessor.process(left_image_path)
	
	right_image_path = subject.right_image_paths[0]
	image_right = PreProcessor.process(right_image_path)
	#cv2.imshow('image_left' , image_left)
	cv2.imshow('image_right' , image_right)
	cv2.waitKey(0)

#subject = base.subjects[37]
#image_path = subject.left_image_paths[0]
#pre_processed_image = PreProcessor.process(image_path)

"""subjects = base.subjects[0:25]
for subject in subjects:
	image_path = subject.left_image_paths[0]
	print(subject.subject_id)
	pre_processed_image = PreProcessor.process(image_path)"""
#pupil_detection(image_path)


"""ret ,threshold_image = cv2.threshold(image , 28 , 255 , cv2.THRESH_BINARY)
#cv2.imshow('threshold' , threshold_image)
#cv2.waitKey(0)

kernel = np.ones((3,3),np.uint8)
dilation = cv2.dilate(threshold_image,kernel,iterations = 4)
#cv2.imshow('dilatation' , dilation)
#cv2.waitKey(0)

erosion = cv2.erode(dilation,kernel,iterations = 4)
cv2.imshow('erosion' , erosion)

or_image = erosion & image
cv2.imshow('or' , or_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#edges = cv2.Canny(image , 100 , 200)
#cv2.imshow('original' , image)
#cv2.imshow('edges' , edges)
cv2.waitKey(0)"""

