# 📸 ExamGuard+: AI Vision Proctoring System

**ExamGuard+** is a real-time AI-based proctoring system designed to monitor and secure examination environments. Using **YOLOv8** and **MediaPipe**, the system detects suspicious behavior such as the presence of mobile phones, multiple faces, or no face, and instantly triggers alerts with voice feedback, beeps, and snapshot logging.

## 🚀 Features

- ✅ **Mobile Phone Detection** using YOLOv8
- ✅ **Multiple/No Face Detection** using MediaPipe Face Detection
- ✅ **Eye Landmark Tracking** using MediaPipe FaceMesh
- ✅ **Real-time Alerts** via speech and beeps
- ✅ **Snapshot Capture** of suspicious activity
- ✅ **On-screen Warnings** for detected events
- ✅ **Live FPS Display**


## 🧠 Technologies Used

| Tool/Library     | Purpose                          |
|------------------|----------------------------------|
| `OpenCV`         | Image processing and video input |
| `MediaPipe`      | Face & eye landmark detection    |
| `YOLOv8 (Ultralytics)` | Object detection (e.g., mobile phones) |
| `pyttsx3`        | Text-to-speech engine            |
| `winsound`       | Beep alerts (Windows only)       |
| `Python`         | Programming Language             |


## 🔧 How It Works

- ✅ Captures real-time video using OpenCV.
- ✅ YOLOv8 detects mobile phones (class: cell phone).
- ✅ MediaPipe FaceDetection counts number of faces.
- ✅ MediaPipe FaceMesh tracks eye landmarks.
- ✅ If mobile/multiple faces/no face → triggers:
       Beep alert
       Voice warning
       Snapshot saved and displayed
- ✅ Displays FPS and status updates on-screen.


## 🛡️ Use Cases
- ✅Online Exam Monitoring
- ✅Smart Classrooms
- ✅Remote Interview Proctoring
- ✅AI Surveillance Applications


## 👨‍💻 Author
Ayush
IIT | Tech Enthusiast | AI-ML & Computer Vision Projects
