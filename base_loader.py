import os
from models.subject import Subject

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
					subject.left_image_paths = images
				elif side == 'R':
					subject.right_image_paths = images
			self.subjects.append(subject)
			#print('subject_loaded ' + subject.subject_id)


base_load = BaseLoader('CASIA-Iris-Lamp-100')
print(base_load.subjects[0])
