import os
import cv2
from models.subject import Subject
import numpy as np

class BaseLoader:

	def __init__(self , base_path):
		self.base_path = base_path
		self.subjects = []
		self.load()

	def load(self):
		dirs = os.listdir(self.base_path)
		dirs.sort()
		for directory in dirs:
			eye_sides = os.listdir(self.base_path + '/' + directory)
			subject = Subject(subject_id = directory)
			for side in eye_sides:
				images = os.listdir(self.base_path + '/' + directory + '/' + side)
				images.sort()
				if side == 'L':
					left_images = []
					for image in images:
						left_images.append(self.base_path + '/' + directory + '/' + side + '/' + image)
					subject.left_image_paths = left_images
				elif side == 'R':
					right_images = []
					for image in images:
						right_images.append(self.base_path + '/' + directory + '/' + side + '/' + image)
					subject.right_image_paths = right_images
			self.subjects.append(subject)


"""base_load = BaseLoader('CASIA-Iris-Lamp-100')
image = cv2.imread(base_load.subjects[0].right_image_paths[0])
print(base_load.subjects[0].right_image_paths[0])
cv2.imshow('iris' , image)
cv2.waitKey(0)"""