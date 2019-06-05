import cv2

# TODO
# WRITE YOUR CAMERA CAPTURE LIBRARY HERE
def capture():
    while(True):
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
    	break
cap.release()
cv2.destroyAllWindows()
    return
