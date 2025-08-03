import cv2 as cv
import mediapipe as mp
from ultralytics import YOLO
import time
import winsound
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
cap = cv.VideoCapture(0)
pTime = 0
model = YOLO('yolov8n.pt')
mpfacedetection = mp.solutions.face_detection
mpeyedetection = mp.solutions.face_mesh
mpdraw = mp.solutions.drawing_utils
drawing_spec = mpdraw.DrawingSpec(thickness=1, circle_radius=1)

facedetection = mpfacedetection.FaceDetection(0.5)
eyedetection = mpeyedetection.FaceMesh(static_image_mode=False,
                                       max_num_faces=1,
                                       refine_landmarks=True,
                                       min_tracking_confidence=0.5,
                                       min_detection_confidence=0.5)
while True:
    success, frame = cap.read()
    videoRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    face_results = facedetection.process(videoRGB)
    eye_results = eyedetection.process(videoRGB)
    print(eye_results)
    print(face_results)
    results = model(frame, stream=True)
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            class_name = model.names[cls]

            if class_name == "person":
                cv.putText(frame, f'{class_name} {conf:.2f}', (x1, y1 - 10),
                           cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
                continue

            if class_name == 'cell phone':
                winsound.Beep(1000, 500)
                status_msg_2 = "Mobile Detected"
                engine.say(status_msg_2)
                engine.runAndWait()
                cv.putText(frame, status_msg_2, (20, 100),
                           cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                filename = f'intrusion_{int(time.time())}.jpg'
                cv.imwrite(filename, frame)
                suspicious_photo = cv.imread(filename)
                cv.imshow("Suspicious Capture", suspicious_photo)

            cv.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv.putText(frame, f'{class_name} {conf:.2f}', (x1, y1 - 10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

    valid_faces = 0
    if face_results.detections:
        for id, detection in enumerate(face_results.detections):
            score = detection.score[0]
            if score > 0.75:
                valid_faces += 1

            if valid_faces >= 2:
                winsound.Beep(1000, 500)
                engine.say("Multiple Face Detected")
                engine.runAndWait()
                cv.putText(frame, "Multiple Face Detected", (20, 100),
                           cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                filename = f'intrusion_{int(time.time())}.jpg'
                cv.imwrite(filename, frame)
                suspicious_photo = cv.imread(filename)
                cv.imshow("Suspicious Capture", suspicious_photo)

            elif valid_faces == 0:
                engine.say("No Face Detected")
                engine.runAndWait()
                cv.putText(frame, "No Face Detected", (20, 100),
                           cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                filename = f'intrusion_{int(time.time())}.jpg'
                cv.imwrite(filename, frame)
                suspicious_photo = cv.imread(filename)
                cv.imshow("Suspicious Capture", suspicious_photo)

    if valid_faces > 0 and eye_results.multi_face_landmarks:
        for face_landmarks in eye_results.multi_face_landmarks:
            mpdraw.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mpeyedetection.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=drawing_spec)

    CTime = time.time()
    fps = 1/(CTime-pTime)
    pTime = CTime
    cv.putText(frame, f'FPS: {int(fps)}', (20, 70),
               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv.imshow("videp", frame)
    if cv.waitKey(10) & 0XFF == ord('l'):
        break

cv.release()
cv.destroyAllWindows()
