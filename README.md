# Drivers_Drowsiness_Detection
A real-time Driver Drowsiness Detection System using OpenCV and dlib to monitor driver alertness by analyzing eye aspect ratio (EAR) and sounding an alarm if drowsiness is detected.

# Features
1. Real-time video capture and face/eye detection  
2. Eye Aspect Ratio (EAR) based drowsiness detection  
3. Alarm sound to alert the driver  
4. Lightweight and easy to run on most systems  

# Technologies Used
1. Python 3.11  
2. OpenCV  
3. dlib  
4. imutils  
5. scipy  
6. playsound  

# How It Works
1. Captures video frames from the webcam.  
2. Detects the face and eyes using dlib's 68 facial landmarks.  
3. Calculates the Eye Aspect Ratio (EAR).  
4. If the EAR is below a set threshold for several frames, an alarm is triggered.  

# Installation
bash  
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
1. Night mode support using IR cameras  
2. Advanced blink detection  
3. Vehicle control system integration  
