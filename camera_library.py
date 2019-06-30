import cv2
WHITE = [255, 255, 255]


class Video(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    def __del__(self):
        self.video.release()
        cv2.destroyAllWindows()

    def get_frame(self):
        ret, frame = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        
        out = '--app\n'.encode()
        out += b'Content-type: image/jpeg\n'
        out += 'Content-length: {}\n'.format(len(jpeg)).encode()
        out += b'\n'
        out += jpeg.tostring()
        out += b'\n'
        return out

    def remove_everything():
        cv2.destroyAllWindows()