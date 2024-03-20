"""
    Some utility functions are defined in this file, which are useful for the project.

"""
from PIL import Image
import cv2


def ocr(crop, mocr):
    
    crop = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(crop)
    
    text = mocr(image)
    
    return text
    
    
def process_text(text):
    
    text = text.replace(" ", "")
    text = [chr(ord(i)-65248) for i in text]
    text = "".join(text)
    final_text = ""
    
    alpha2num = {"C":"0", "O":"0", "I":"1", "D":"0", "S":"5"}
    num2alpha = {"0":"O", "1":"I", "5":"S"}
    
    for i in range(len(text)):
        if i>2:
            if text[i] in list(alpha2num.keys()):
                final_text  = final_text + f"{alpha2num[text[i]]}"
            else:
                final_text = final_text + f"{text[i]}"
                

        else:
            if text[i] in num2alpha:
                final_text = final_text + f"{num2alpha[text[i]]}"
            else:
                final_text = final_text + f"{text[i]}"
                
    return final_text.strip()    


def draw_plate_num(image, text, bounding_box, font_scale=0.5, font_thickness=1):

    x1, y1, x2, y2 = bounding_box
    
    # Calculate font size based on bounding box size
    
    font = cv2.FONT_HERSHEY_SIMPLEX
        
    # Calculate text position
    text_x = x1 - (abs(x2 - x1)) // 2
    text_y = y1 - 20 # Adjust for positioning
        
    # Draw text
    # cv2.putText(image, text, (text_x, text_y), font, font_scale, (0, 255, 0), font_thickness)
    cv2.putText(image, text, (text_x, text_y), font, 1.5, (0,255,0), 2)
        