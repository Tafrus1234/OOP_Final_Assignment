import cv2

class CameraAI:
	def __init__(self):
		self.camera = cv2.VideoCapture(0)  # Initialize camera

	def detect_faces(self):
		ret, frame = self.camera.read()  # Read frame from camera
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
		faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml').detectMultiScale(gray)  # Detect faces
		return faces

	def display_output(self, faces):
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Draw rectangle around face
		cv2.imshow('Camera AI', frame)  # Display output

	def run(self):
		while True:
			faces = self.detect_faces()
			self.display_output(faces)
			if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' 
to quit
				break
		self.camera.release()
		cv2.destroyAllWindows()

if __name__ == '__main__':
	ai = CameraAI()
	ai.run()






