import cv2
import numpy as np
import math


class Segmentation:
		
	def __init__(self , image_path , ray):
		self.image_path = image_path
		self.original_image = cv2.imread(self.image_path , 0)
		self.pre_processed_image = None
		self.pupil_centroid = None
		self.space_off = 250
		self.ray = ray

	#@classmethod
	#def process(PreProcessor , image_path):
	def pre_process(self):
		#compute pre_processed_image
		threshold_image = cv2.threshold(self.original_image , 28 , 255 , cv2.THRESH_BINARY)[1] #making threshold
		invert_threshold = cv2.bitwise_not(threshold_image)                      #inverting threshold result
		floodfill_image = threshold_image.copy()                                 #creating the image that will be flooded
		h, w = threshold_image.shape[:2]                                         #getting dimension values to create the mask
		mask = np.zeros((h + 2 , w + 2) , np.uint8)                              #creating the mask that will be used on cv2.floodFill()
		seed = (0 , 0)
		seeds = [(0 , 0) , (319 , 0) , (639 , 0) , (0 , 139) , (639 , 139) , (0 , 479) , (319 , 479) , (639 , 479)]
		for index in range(1 ,8):
			cv2.floodFill(floodfill_image , mask , seeds[index] , 0)             #appling floodFill algorithm	
		white_pupil = invert_threshold + floodfill_image                         #filling pupil 
		black_pupil = cv2.bitwise_not(white_pupil)                               #invert white_pupil image
		#and_processed_image = image & black_pupil                               #using logig operation AND between the initial image and the black_pupil to complete the pre processing	
		kernel = np.ones((9 , 9) , np.uint8)
		open_image = cv2.morphologyEx(black_pupil , cv2.MORPH_OPEN , kernel)
		out = open_image & black_pupil
		self.pre_processed_image = self.original_image & out
		print('pre process complete')
		#cv2.imshow('opening' , open_image)
		#cv2.imshow('out' ,image & out)
		#cv2.imshow('original' , image)
		#cv2.imshow('threshold' , threshold_image)
		#cv2.imshow('invert threshold' , invert_threshold)
		#cv2.imshow('floodfill' , floodfill_image)
		#cv2.imshow('white pupil' , white_pupil)
		#cv2.imshow('black pupil' , black_pupil)
		#cv2.imshow('pre_processed' , self.pre_processed_image)
		#cv2.waitKey(0)
		



	def houghs_transform(self):
		#compute pupil_centroid
		rgb_image = cv2.imread(self.image_path)                    #reading image that can show the circle that identify the pupil
		height , width = self.original_image.shape[:2]             #getting number of lines and collumns ,will be used to build houghs_plan
		edges = cv2.Canny(self.pre_processed_image , 100 , 200)    #using Canny algorithm to generate the edges
		hough_plan = np.zeros((height , width) , np.uint8)         #creating houghs_plan filled with 0
		for line in range(0,height):                               #loop that compute houghs_plan
			for column in range(0,width):
				if edges.item(line , column) == 255:
					for teta in range(0 , 360):
						xt = int(line - self.ray * math.cos(teta))
						yt = int(column - self.ray * math.sin(teta))
						if xt < height and yt < width and xt > 0 and yt > 0:
							hough_plan.itemset((xt , yt) , hough_plan.item(xt , yt) + 1)
					
		bigger = 0             
		bigger_line = 0
		bigger_collumn = 0
		for line in range(0,height):                               #loop that sweeps intire houghs_plan to find the pupil_centroid
			for column in range(0,width):
				if hough_plan.item(line , column) >= bigger:
					bigger = hough_plan.item(line , column)
					bigger_line = line
					bigger_collumn = column
		self.pupil_centroid = tuple([bigger_line, bigger_collumn])
		print('pupil centroid computed')
		#cv2.imshow('rgb_image' , rgb_image)
		#cv2.imshow('edges' , edges)
		#cv2.circle(rgb_image , tuple([bigger_collumn , bigger_line]) , self.ray , (0,255,0))
		#cv2.circle(rgb_image , tuple([bigger_collumn , bigger_line]) , 5 , (0,0,255) , -1)
		#cv2.imshow('hough_plan' , hough_plan)
		#cv2.imshow('image' , rgb_image)
		#cv2.waitKey(0)
		
		
		

		