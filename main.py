from models.YOLOv8.detection import Detector
import cv2

detector = Detector("weights/best.pt")

# drawn_img, crop, box = detector.detect("")

# Open video file
video_capture = cv2.VideoCapture('input/sample.mp4')  # Replace 'video_file.mp4' with your video file

while True:
    # Read a frame from the video
    ret, frame = video_capture.read()
    if not ret:
        break  # Break the loop if no frame is retrieved


    drawn_img, crop, box = detector.detect(frame)

    cv2.namedWindow("drawn_image", cv2.WINDOW_KEEPRATIO)
    cv2.imshow("drawn_image",drawn_img)
    # cv2.imshow("drawn", crop)
    cv2.waitKey(0)
    
video_capture.release()
cv2.destroyAllWindows()


