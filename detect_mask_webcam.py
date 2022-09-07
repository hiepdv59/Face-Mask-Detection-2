# import the necessary packages
from bound_box import bound_box_and_predict
from show_frame import show_frames
from imutils.video import VideoStream
import imutils
import cv2


def mask_video(window, videoPath):
	# initialize the video stream
	print("[INFO] starting video stream...")
	
	vs = VideoStream(src=videoPath).start()

	# loop over the frames from the video stream
	while True:
		# grab the frame from the threaded video stream and resize it
		# to have a maximum width of 400 pixels
		frame = vs.read()
		frame = imutils.resize(frame, width=600)

		bound_box_and_predict(frame)
		# show the output frame
		cv2.imshow("Output", frame)
		key = cv2.waitKey(1) & 0xFF

		# if the `q` key was pressed, break from the loop
		if key == ord("q") or key == 13:
			break

	# do a bit of cleanup
	cv2.destroyAllWindows()
	vs.stop()