import cv2
import mediapipe as mp
import pygame
import time
# Initialize Pygame mixer for sound playback
pygame.mixer.init()

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Initialize variables for drowsiness detection
COUNTER = 0
ALARM_ON = False
ALARM_COUNT = 0  # Counter for the number of times the alarm has sounded

# Path to the alert sound file (update this path)
ALERT_SOUND_PATH = "C:\\Users\\PycharmProjects\\DrowsinessDetection\\siren_alert.wav"

# Cooldown flag and duration
cooldown = False
cooldown_start_time = None
COOLDOWN_DURATION = 5  # Cooldown period in seconds

# EAR threshold and frame count threshold
EAR_THRESHOLD = 0.2  # Adjust based on testing
CONSEC_FRAMES = 15  # Consecutive frames of low EAR to trigger alarm

# Function to calculate EAR
def calculate_ear(landmarks, indices):
    # Indices for eye landmarks
    p1, p2, p3, p4, p5, p6 = indices
    # Vertical distances
    vertical1 = abs(landmarks[p2].y - landmarks[p6].y)
    vertical2 = abs(landmarks[p3].y - landmarks[p5].y)
    # Horizontal distance
    horizontal = abs(landmarks[p1].x - landmarks[p4].x)
    # EAR calculation
    ear = (vertical1 + vertical2) / (2.0 * horizontal)
    return ear

# Start video capture
cap = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the BGR image to RGB
            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(image_rgb)

            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    # EAR for left and right eyes
                    left_ear = calculate_ear(face_landmarks.landmark, [33, 159, 145, 133, 153, 144])
                    right_ear = calculate_ear(face_landmarks.landmark, [263, 386, 374, 362, 380, 373])
                    ear_average = (left_ear + right_ear) / 2

                    if ear_average < EAR_THRESHOLD:
                        COUNTER += 1

                        if COUNTER >= CONSEC_FRAMES and not ALARM_ON and not cooldown:
                            print("Drowsiness Detected! Please take a break.")
                            pygame.mixer.music.load(ALERT_SOUND_PATH)
                            pygame.mixer.music.play(-1)  # Play indefinitely
                            ALARM_ON = True
                            ALARM_COUNT += 1
                            cooldown = True
                            cooldown_start_time = time.time()
                    else:
                        COUNTER = 0
                        if ALARM_ON:
                            pygame.mixer.music.stop()
                            ALARM_ON = False

            # Cooldown logic
            if cooldown and time.time() - cooldown_start_time >= COOLDOWN_DURATION:
                cooldown = False

            # Draw face mesh landmarks on the frame.
            mp_drawing.draw_landmarks(
                frame,
                face_landmarks,
                mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1))

            # Display the alarm count on the frame
            cv2.putText(frame, f"Alarm Count: {ALARM_COUNT}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            # Show the frame with detected faces and landmarks
            cv2.imshow("Drowsiness Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("Program interrupted. Exiting...")

    finally:
        cap.release()
        cv2.destroyAllWindows()
        pygame.mixer.music.stop()
        pygame.mixer.quit()





















