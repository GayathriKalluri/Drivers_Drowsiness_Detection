# Drivers_Drowsiness_Detection
A real-time Driver Drowsiness Detection System using OpenCV and dlib to monitor driver alertness by analyzing eye aspect ratio (EAR) and sounding an alarm if drowsiness is detected.

# Features
Real-time video capture and face/eye detection  
. Eye Aspect Ratio (EAR) based drowsiness detection
. Alarm sound to alert the driver
. Lightweight and easy to run on most systems

# Technologies Used
Python 3.11
OpenCV
dlib
imutils
scipy
playsound

# How It Works
. Captures video frames from the webcam.
. Detects the face and eyes using dlib's 68 facial landmarks.
. Calculates the Eye Aspect Ratio (EAR).
. If the EAR is below a set threshold for several frames, an alarm is triggered.

# Installation
bash
git clone https://github.com/your-username/driver-drowsiness-detection.git
cd driver-drowsiness-detection
pip install -r requirements.txt
Important:
Download the pre-trained facial landmark model:
shape_predictor_68_face_landmarks.dat
Extract and place it in your project folder.

# Usage
bash
python drowsiness_detection.py
Optional arguments:
--alarm : Custom alarm sound path
--webcam : Webcam index (default is 0)

# Example:
bash
python drowsiness_detection.py --alarm alarm.wav --webcam 1

# Eye Aspect Ratio (EAR)
The EAR is calculated as:
ini
EAR = (||p2 - p6|| + ||p3 - p5||) / (2 * ||p1 - p4||)
A low EAR over consecutive frames signals drowsiness.

# Project Structure
driver-drowsiness-detection/
│
├── drowsiness_detection.py
├── shape_predictor_68_face_landmarks.dat
├── alarm.wav
├── README.md
└── requirements.txt

# Future Enhancements
. Night mode support using IR cameras
. Advanced blink detection
. Vehicle control system integration
