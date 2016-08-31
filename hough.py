from base_loader import BaseLoader
from utils.segmentation import Segmentation
import cv2
import numpy as np
import math	
import PIL


base = BaseLoader('CASIA-Iris-Lamp-100')
subject = base.subjects[0]
image_path = subject.left_image_paths[0]
segmentation = Segmentation(image_path=image_path , ray=47)
segmentation.pre_process()
segmentation.houghs_transform()

pre_processed_image = segmentation.pre_processed_image
centroid = segmentation.pupil_centroid
ray = segmentation.ray
print(centroid)
print(ray)
line_init = centroid[0] - ray
line_end = centroid[0] + ray
column_init = centroid[1] - ray
column_end = centroid[1] + ray
cut_image = pre_processed_image[line_init:line_end , column_init:column_end ]
print(cut_image)
cut_image = np.array(cut_image , np.uint8)
cv2.imshow('sub_image' , cut_image)
cv2.waitKey(0)

