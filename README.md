# Real-Time ALPR (Automatic License Plate Recognition)

Real-Time ALPR (Automatic License Plate Recognition) is a project aimed at detecting and recognizing license plates in real-time video streams. It utilizes YOLOv8 for license plate detection and manga-ocr for optical character recognition (OCR) to extract the license plate number.

## Features

- Real-time detection and recognition of license plates in video streams.
- Utilizes YOLOv8 for license plate detection.
- Uses manga-ocr for optical character recognition (OCR) to extract license plate numbers.
- Supports detection of single license plates.
- Specifically designed for 6-digit license plate numbers.

## Requirements

- Python 3.x
- OpenCV
- ultralytics
- manga-ocr

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Fahad-H36/ALPR-Pakistan.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Using a Video File

1. Prepare your video for processing.

2. Run the main script:

    ```bash
    python main.py --video path_to_your_video.mp4
    ```

    Replace `path_to_your_video.mp4` with the path to your video file.

   The script will process the video, detect license plates, and recognize the plate numbers in real-time.

### Using a Camera

1. Run the main script with the `--mode c` option:

    ```bash
    python main.py --mode c --cam <camera_number> --video "./"
    ```
    _Use --cam only if you have multiple cameras connected._<br><br>
    This will start capturing video from your camera, detect license plates, and recognize the plate numbers in real-time.
## Output

The output will be an annotated video with detected license plates and recognized plate numbers. You can find the output video in the `output` directory.

## Example

![Example GIF](./assets/car_output.gif)


## Acknowledgments

- [Roboflow - ALPR Dataset](https://universe.roboflow.com/alpr-qggma/alpr-akctv/dataset/24) for providing the dataset used to train YOLOv8.
- [manga-ocr](https://github.com/kha-white/manga-ocr) by kha-white

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact

Fahad Soomro - fahadh936@gmail.com
