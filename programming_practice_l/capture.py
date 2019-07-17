import cv2

WHITE = [255, 255, 255]
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

def draw_box(Image, x, y, w, h):
    cv2.line(Image, (x, y), (x + int(w / 5), y), WHITE, 2)
    cv2.line(Image, (x + int((w / 5) * 4), y), (x + w, y), WHITE, 2)
    cv2.line(Image, (x, y), (x, y + int(h / 5)), WHITE, 2)
    cv2.line(Image, (x + w, y), (x + w, y + int(h / 5)), WHITE, 2)
    cv2.line(Image, (x, (y + int(h / 5 * 4))), (x, y + h), WHITE, 2)
    cv2.line(Image, (x, (y + h)), (x + int(w / 5), y + h), WHITE, 2)
    cv2.line(Image, (x + int((w / 5) * 4), y + h), (x + w, y + h), WHITE, 2)
    cv2.line(Image, (x + w, (y + int(h / 5 * 4))), (x + w, y + h), WHITE, 2)



class Video(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()
    def get_frame(self):
    	ret, frame = self.video.read()
    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5 )
    	for (x, y, w, h) in faces:
    		print(x, y, w, h)
    		roi_gray = gray[y:y+h, x:x+w] #(ycord1 start, ycord2 end)
    		roi_color = frame[y:y+h, x:x+w]
    		draw_box(gray, x, y, w, h)
    	ret, jpeg = cv2.imencode('.jpg', gray)

    	return jpeg.tobytes()
    	cv2.destroyAllWindows()