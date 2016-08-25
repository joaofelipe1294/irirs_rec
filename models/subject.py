class Subject:

	def __init__(self , subject_id):
		self.subject_id = subject_id
		self.left_image_paths = None
		self.right_image_paths = None

	def __str__(self):
		return 'subject_id : ' + self.subject_id + '\n' + 'left_images : ' + str(self.left_image_paths) + '\n' + 'right_images : ' + str(self.right_image_paths)