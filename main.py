from detection.detection import Detector
import cv2
from manga_ocr import MangaOcr
import util
from collections import Counter
import time
import argparse

parser = argparse.ArgumentParser(description="Real-Time ALPR (Automatic License Plate Recognition)")
parser.add_argument("--mode",default="v", required=False, help="'c' for webcam mode")
parser.add_argument("--video",default="./", required=True, help="Path to the input video file")
parser.add_argument("--cam",default="0", required=True, help="0 for default camera (i.e., laptop camera). 1 if you have different camera connected")

# Parse the command-line arguments
args = parser.parse_args()




detector = Detector("detection/models/YOLOv8/weights/best.pt")
mocr = MangaOcr()


if args.mode != "c":
    input_video_path = args.video
    file_name = input_video_path.split("/")[-1].split(".")[0]
    output_video_path = f"output/{file_name}_output.mp4"

    # Open video file
    video_capture = cv2.VideoCapture(input_video_path)  # Replace 'video_file.mp4' with your video file
    cv2.namedWindow("drawn_image", cv2.WINDOW_KEEPRATIO)

else:
    try:
        cam_no = int(args.cam)
        video_capture = cv2.VideoCapture(0)
    except Exception as e:
        print("Invalid camera option passed")
        exit()
    
    if not video_capture.isOpened():
        print("Error opening camera")
        exit()

    output_video_path = "output/output.mp4"
    
ret, first_frame = video_capture.read()
# Check if the frame was read successfully
if not ret:
    print("Error: Unable to read first frame.")
    exit()
frame_height, frame_width, _ = first_frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
out = cv2.VideoWriter(output_video_path, fourcc, 25.0, (frame_width, frame_height))

predictions = []
counter = Counter(predictions)

while True:
    # Read a frame from the video
    ret, frame = video_capture.read()
    if not ret:
        break  # Break the loop if no frame is retrieved


    drawn_img, crop, box, detected = detector.detect(frame)
    
    if not detected:
        cv2.imshow("drawn_image", frame)
        # time.sleep(0.1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        out.write(frame)

        continue
    
    text = util.ocr(crop, mocr)
    processed_text = util.process_text(text)
    if len(processed_text) == 6:
        # predictions.append(processed_text)
        util.append_with_limit(predictions, processed_text, 10)
        counter.update(predictions)
        
    if len(predictions)>5:
        if len(processed_text)!=6:
            processed_text = counter.most_common(1)[0][0]
            
    if processed_text != "":
        util.draw_plate_num(drawn_img, processed_text, box)

    # cv2.namedWindow("drawn_image", cv2.WINDOW_KEEPRATIO)
    cv2.imshow("drawn_image",drawn_img)
    out.write(drawn_img)
    # cv2.imshow("drawn", crop)
    # cv2.waitKey(0)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video_capture.release()
out.release()
cv2.destroyAllWindows()
