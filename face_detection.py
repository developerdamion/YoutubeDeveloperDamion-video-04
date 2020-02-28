"""
Hey! Thank you for supporting my youtube channel 
( https://www.youtube.com/channel/UCKrs-v_MlKjzVbe4jyLSrPQ ). 

This is video-04: OpenCV Python Face and Eye Detection | Code Along | Class Wrapped
Please like and subscribe to my video! 
( https://youtu.be/3NTq2DV9Ic0 )

DeveloperDamion
"""
import cv2

class camera():

	cascades = {
		"face": cv2.CascadeClassifier('haarcascade_frontalface_default.xml'),
		"eye": cv2.CascadeClassifier('haarcascade_eye.xml'),
	}
	def __init__(self):
		self.cap = cv2.VideoCapture(0)

		self.face_detection = False
		self.eye_detection = False

	def get_frame(self):
		ret, frame = self.cap.read()
		return frame

	def grayscale(self, frame):
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		return gray

	def display(self, frame): cv2.imshow('img', frame)

	def detect(self, frame):
		if self.face_detection is True:
			self.detect_face(frame)

	def detect_eye(self, gray_frame, color_frame):
		eyes = self.cascades["eye"].detectMultiScale(gray_frame)

		for (x,y,w,h) in eyes:
			cv2.rectangle(color_frame, (x,y), (x+w, y+h), (255,255,255), 1)

	def detect_face(self, frame):
		gray = self.grayscale(frame)
		faces = self.cascades["face"].detectMultiScale(gray, 1.3, 5)

		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2 )

			gray_section = gray[y:y+h, x:x+w]
			color_section = frame[y:y+h, x:x+w]

			if self.eye_detection is True: self.detect_eye(gray_section, color_section)

	def run(self):
		while True:
			new_frame = self.get_frame()
			self.detect(new_frame)
			self.display(new_frame)

			k = cv2.waitKey(30) & 0xff
			if k == 27:
				break

		self.cap.release()
		cv2.destroyAllWindows()


if __name__ == "__main__":
	new_camera = camera()
	new_camera.face_detection = True
	new_camera.eye_detection = True
	new_camera.run()