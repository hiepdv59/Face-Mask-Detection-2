from bound_box import bound_box_and_predict
from show_frame import show_frames
import cv2

def mask_image(window, imagePath):
	# load input image and preprocess
	frame = cv2.imread(imagePath)

	bound_box_and_predict(frame)
	# show output image
	#cv2.imshow("Output", frame)
	show_frames(window = window, frame = frame)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
