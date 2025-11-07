# thief-catcher

thief-catcher is a simple camera security program that can spot a person in front of a camera and send you an alert when someone appears.  
It uses the MobileNet SSD model to detect people in real-time and sends a Pushbullet notification so you can know if someone is near your camera — useful for catching intruders or checking activity when you’re away.

---

## Features

- Detects people in live camera streams
- Sends Pushbullet alerts when someone is seen
- Works with IP or USB cameras
- Lightweight and easy to set up

---

## Requirements

- Python 3
- OpenCV
- Requests
- A Pushbullet account (for notifications)

Install dependencies:
```bash
pip install opencv-python requests

How to Use


Clone this repository:
git clone https://github.com/yourusername/thief-catcher.git
cd thief-catcher



Download the MobileNetSSD model files:


MobileNetSSD_deploy.caffemodel


MobileNetSSD_deploy.prototxt




Add your Pushbullet Access Token in the code:
API_KEY = "YOUR_ACCESS_TOKEN"



Set your camera stream URL:
cap = cv2.VideoCapture("your_camera_stream_url")



Run the script:
python sentry_eye.py



Press Q to quit.



Notes


Works best with decent lighting.


You can adjust detection confidence or frame rate to reduce false alerts.


Tested with regular IP camera streams and USB webcams.



License
This project is open for personal use and learning.
Feel free to modify or improve it for your own setup.

Made with patience and curiosity.

---

