# Face Detection and Mesh Detection Project

This repository contains three Python programs for face detection using OpenCV and MediaPipe. The first code implements face mesh detection, the second code detects faces and marks bounding boxes with additional edge highlighting, and the third code combines both functionalities into one.

## Table of Contents
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Program 1: Face Mesh Detection](#program-1-face-mesh-detection)
- [Program 2: Face Detection with Bounding Boxes](#program-2-face-detection-with-bounding-boxes)
- [Program 3: Combined Face Mesh and Bounding Box Detection](#program-3-combined-face-mesh-and-bounding-box-detection)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Real-time face mesh detection** using MediaPipe.
- **Face detection** with bounding boxes and additional edge highlighting.
- **Combined face mesh and bounding box detection** in a single program.
- **Frame rate display (FPS)** for performance tracking.
- Supports live video feeds from a webcam and recorded video files.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/face-detection-mesh-bbox.git
    ```

2. **Install required dependencies**:
    ```bash
    pip install opencv-python mediapipe
    ```

3. **Run the programs**:
    - For face mesh detection:
      ```bash
      python face_mesh_module.py
      ```
    - For face detection with bounding boxes:
      ```bash
      python face_detection_module.py
      ```
    - For combined face mesh and bounding box detection:
      ```bash
      python combined_face_detection_mesh.py
      ```

## Usage

### Face Mesh Detection
This program detects faces and draws facial landmarks (mesh) on the detected faces in real-time. It also displays the frame rate (FPS) on the video feed.

### Face Detection with Bounding Boxes
This program detects faces in real-time, draws bounding boxes around the faces, and marks edges on the boxes for emphasis. The FPS is displayed on the video feed as well.

### Combined Face Mesh and Bounding Box Detection
This program combines the face mesh and bounding box detection into one, detecting face landmarks and bounding boxes simultaneously. The FPS is also displayed on the video feed.

To stop the video feed in any program, press the `p` key.

## Technologies Used
- **Python**
- **OpenCV** for image and video processing.
- **MediaPipe** for face mesh and detection models.
- **NumPy** for numerical operations.

## Program 1: Face Mesh Detection
The `faceMeshDectection` class detects facial landmarks using the MediaPipe FaceMesh module. It identifies facial landmarks and draws them onto the video frame.

### Key Features:
- Detects facial landmarks (face mesh) on up to 2 faces at a time.
- Customizable mesh appearance through drawing specifications.

## Program 2: Face Detection with Bounding Boxes
The `faceDetection` class detects faces using MediaPipe's face detection module and draws bounding boxes around the faces. It also highlights the corners of the bounding boxes with red lines.

### Key Features:
- Detects faces and draws bounding boxes.
- Adds decorative edge lines to the bounding boxes for better visibility.
- Prints the detection score and face bounding box information on the console.

## Program 3: Combined Face Mesh and Bounding Box Detection
This combined program uses both the `faceMeshDectection` and `faceDetection` classes to detect face meshes and bounding boxes in real-time. The face mesh and bounding box detections are drawn simultaneously, providing a comprehensive visualization of facial features.

### Key Features:
- Combines face mesh detection and bounding box marking in real-time.
- Displays detection results with both face mesh landmarks and bounding boxes.
- Prints bounding box information (ID, box, and confidence score) on the console.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License.
