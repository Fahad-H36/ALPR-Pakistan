from ultralytics import YOLO
import cv2


class Detector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        
    def detect(self, img):
        
        drawn_image = img.copy()
        
        results = self.model(img)
        # for box in results[0].boxes[0].xyxy:
            # x1, y1, x2, y2 = box.numpy()
        try:
            x1, y1, x2, y2 = results[0].boxes[0].xyxy[0].numpy()
        except Exception as e:
            print("NO License Plate detected")
            return drawn_image, drawn_image, [], False
        croped = img[int(y1):int(y2), int(x1):int(x2)]
        
        cv2.rectangle(drawn_image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)  # Green rectangle
        
        return drawn_image, croped, [int(x1), int(y1), int(x2), int(y2)], True

        


        
        