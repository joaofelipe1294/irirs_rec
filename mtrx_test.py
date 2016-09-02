from base_loader import BaseLoader
from utils.segmentation import Segmentation
import numpy as np
import cv2
import math

"""def houghs_transform(image_path = None , min_ray = None ,max_ray = None):
		#compute pupil_centroid
		if min_ray == None or max_ray == None:
			raise Exception('Os parametros referentes ao raio maxio e/ou minimo nao foram informados')
		rgb_image = cv2.imread(image_path)                    #reading image that can show the circle that identify the pupil
		original_image = cv2.imread(image_path , 0)
		height , width = original_image.shape[:2]              #getting number of lines and collumns ,will be used to build houghs_plan
		print('width : ' + str(width) + ' | height : ' + str(height))
		houghs_plan = []
		for x in range(0 , max_ray - min_ray + 1):
			houghs_plan.append(np.zeros((height , width) , np.uint8))         #creating houghs_plan filled with 0
		segmentation = Segmentation(image_path=image_path )
		segmentation.pre_process()
		pre_processed_image = segmentation.pre_processed_image
		edges = cv2.Canny(pre_processed_image , 100 , 200)     #using Canny algorithm to generate the edges
		z_index = 0
		for ray in range(min_ray , max_ray + 1):
			for line in range(0,height):                               #loop that compute houghs_plan
				for column in range(0,width):
					if edges.item(line , column) == 255:
						for teta in range(0 , 360):
							xt = int(line - ray * math.cos(teta))
							yt = int(column - ray * math.sin(teta))
							if xt < height and yt < width and xt > 0 and yt > 0:
								houghs_plan[z_index].itemset((xt , yt) , houghs_plan[z_index].item(xt , yt) + 1)
			print('z_index : ' + str(z_index) + ' | ray : ' + str(ray))
			z_index += 1	
		#cv2.imshow('h0' , houghs_plan[0])
		#cv2.imshow('h1' , houghs_plan[1])
		#cv2.waitKey(0)

		bigger = 0             
		bigger_line = 0
		bigger_collumn = 0
		ray = None
		ray_count = 0
		for plan in houghs_plan:
			for line in range(0,height):                               #loop that sweeps intire houghs_plan to find the pupil_centroid
				for column in range(0,width):
					if plan.item(line , column) >= bigger:
						bigger = plan.item(line , column)
						bigger_line = line
						bigger_collumn = column		#self.pupil_centroid = tuple([bigger_line, bigger_collumn])
						ray = min_ray + ray_count
			ray_count += 1
		print('raio : ' + str(ray))
		centroid = tuple([bigger_line , bigger_collumn])
		print('centroid : ' + str(centroid))
		#print('pupil centroid computed')
		#cv2.imshow('rgb_image' , rgb_image)
		#cv2.imshow('edges' , edges)
		cv2.circle(rgb_image , tuple([bigger_collumn , bigger_line]) , ray , (0,255,0))
		cv2.circle(rgb_image , tuple([bigger_collumn , bigger_line]) , 5 , (0,0,255) , -1)
		#cv2.imshow('hough_plan' , hough_plan)
		cv2.imshow('image_method' , rgb_image)
		cv2.waitKey(0)
"""
base = BaseLoader('CASIA-Iris-Lamp-100')
subject = base.subjects[0]
image_path = subject.left_image_paths[0]
segmentation = Segmentation(image_path=image_path)
segmentation.houghs_transform(min_ray = 40 , max_ray = 70)
segmentation.pre_process()
#houghs_transform(image_path = image_path , min_ray = 40 , max_ray = 70)
