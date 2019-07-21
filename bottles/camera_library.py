import cv2
import time

class VideoWorker():

    on_img = None
    on_vid = None
    on_end = None
    interval = 0.1
    started = False
    screenshot = False
    bottle_result = None

    def __init__(self, camera_number: int = 0):
        self.webcam = cv2.VideoCapture(camera_number)
        self.webcam.release()
        self.webcam = cv2.VideoCapture(0)
        return

    def start(self):
        print('Webcam start')
        self.started = True
        # default : 848x480 on MacBook

        while True:
            if self.webcam.isOpened():
                rc, frame = self.webcam.read()
                if not rc:
                    print('Camera image capture failed')
                    continue

                if self.on_vid is not None:
                    self.on_vid(frame)

                if self.screenshot and self.on_img is not None:
                    self.bottle_result = self.on_img(frame)
                    self.screenshot = False

                time.sleep(self.interval)
            else:
                print('No available camera')
                break

        self.end()

    def end(self):
        print('End webcam')

        if self.webcam is not None:
            self.webcam.release()
            cv2.destroyAllWindows()

        if self.on_end is not None:
            self.on_end()

vid_worker = VideoWorker()
