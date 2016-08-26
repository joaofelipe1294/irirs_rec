import cv2
import numpy as np


class PreProcessor:
		
	@classmethod
	def process(PreProcessor , image_path):
		image = cv2.imread(image_path , 0)
		threshold_image = cv2.threshold(image , 28 , 255 , cv2.THRESH_BINARY)[1] #making threshold
		invert_threshold = cv2.bitwise_not(threshold_image)                      #inverting threshold result
		floodfill_image = threshold_image.copy()                                 #creating the image that will be flooded
		h, w = threshold_image.shape[:2]                                         #getting dimension values to create the mask
		mask = np.zeros((h + 2 , w + 2) , np.uint8)                              #creating the mask that will be used on cv2.floodFill()
		cv2.floodFill(floodfill_image , mask , (0 , 0) , 0)                      #appling floodFill algorithm
		white_pupil = invert_threshold + floodfill_image                         #filling pupil 
		black_pupil = cv2.bitwise_not(white_pupil)                               #invert white_pupil image
		pre_processed_image = image & black_pupil                                #using logig operation AND between the initial image and the black_pupil to complete the pre processing
		
		cv2.imshow('threshold' , threshold_image)
		cv2.imshow('invert threshold' , invert_threshold)
		cv2.imshow('floodfill' , floodfill_image)
		cv2.imshow('white pupil' , white_pupil)
		cv2.imshow('black pupil' , black_pupil)
		cv2.imshow('pre_processed' , pre_processed_image)
		cv2.waitKey(0)
		
		return pre_processed_image
