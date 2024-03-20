from models.YOLOv8.detection import Detector
import cv2
from manga_ocr import MangaOcr
import util


detector = Detector("models/YOLOv8/weights/best.pt")
mocr = MangaOcr()



# Open video file
video_capture = cv2.VideoCapture(r'D:\projects\ANPR\localization\localization\automatic-number-plate-recognition-python-yolov8\sample.mp4')  # Replace 'video_file.mp4' with your video file

while True:
    # Read a frame from the video
    ret, frame = video_capture.read()
    if not ret:
        break  # Break the loop if no frame is retrieved


    drawn_img, crop, box, detected = detector.detect(frame)
    
    if not detected:
        continue
    
    cv2.imwrite("crop.jpg", crop)
    text = util.ocr(crop, mocr)
    processed_text = util.process_text(text)
    util.draw_plate_num(drawn_img, processed_text)

    cv2.namedWindow("drawn_image", cv2.WINDOW_KEEPRATIO)
    cv2.imshow("drawn_image",drawn_img)
    # cv2.imshow("drawn", crop)
    cv2.waitKey(0)
    
video_capture.release()
cv2.destroyAllWindows()

# img = cv2.imread("input/car1.jpg")

# drawn_img, crop, box = detector.detect(img)

# text = util.ocr(crop, mocr)
# processed_text = util.process_text(text)
# print(processed_text)
# util.draw_plate_num(drawn_img, processed_text, box)

# cv2.namedWindow("drawn_image", cv2.WINDOW_KEEPRATIO)
# cv2.imshow("drawn_image",drawn_img)
# # cv2.imshow("drawn", crop)
# cv2.waitKey(0)