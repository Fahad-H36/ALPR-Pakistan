from detection.detection import Detector
import cv2
from manga_ocr import MangaOcr
import util
from collections import Counter
import argparse

parser = argparse.ArgumentParser(description="Real-Time ALPR (Automatic License Plate Recognition)")
parser.add_argument("--video", required=True, help="Path to the input video file")

# Parse the command-line arguments
args = parser.parse_args()




detector = Detector("detection/models/YOLOv8/weights/best.pt")
mocr = MangaOcr()

input_video_path = args.video
file_name = input_video_path.split("/")[-1].split(".")[0]
output_video_path = f"output/{file_name}_output.mp4"

# Open video file
video_capture = cv2.VideoCapture(input_video_path)  # Replace 'video_file.mp4' with your video file
cv2.namedWindow("drawn_image", cv2.WINDOW_KEEPRATIO)


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
        out.write(frame)
        continue
    
    text = util.ocr(crop, mocr)
    processed_text = util.process_text(text)
    if len(processed_text) == 6:
        predictions.append(processed_text)
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
