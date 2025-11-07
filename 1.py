import cv2
import requests

# --- Pushbullet API Setup ---
API_KEY = ""  # Add your Pushbullet Access Token here

def send_push(title, message):
    """Send a simple Pushbullet notification."""
    print("Sending Pushbullet alert...")

    payload = {
        "type": "note",
        "title": title,
        "body": message
    }

    headers = {
        "Access-Token": API_KEY,
        "Content-Type": "application/json"
    }

    res = requests.post("https://api.pushbullet.com/v2/pushes", json=payload, headers=headers)

    if res.status_code == 200:
        print("Alert sent successfully!")
    else:
        print(f"Push failed ({res.status_code}): {res.text}")

# --- Load the MobileNet SSD Model ---
print("Loading detection model...")
net = cv2.dnn.readNetFromCaffe(
    "MobileNetSSD_deploy.prototxt",
    "MobileNetSSD_deploy.caffemodel"
)

CLASSES = [
    "background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow",
    "diningtable", "dog", "horse", "motorbike", "person",
    "pottedplant", "sheep", "sofa", "train", "tvmonitor"
]

# --- Connect to Camera Stream ---
# Replace with your IP camera or phone stream URL
CAMERA_URL = ""
cap = cv2.VideoCapture(CAMERA_URL)

if not cap.isOpened():
    print("Error: Could not open camera stream.")
    exit()

print("Camera started. Press 'q' to quit.")

alert_sent = False
frame_counter = 0
PROCESS_EVERY = 5  # Only process every 5th frame to save CPU

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Resize frame to speed up processing
    frame = cv2.resize(frame, (640, 480))
    frame_counter += 1

    # Skip frames to reduce load
    if frame_counter % PROCESS_EVERY != 0:
        cv2.imshow("Camera Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    # Prepare the frame for detection
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    person_found = False

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.6:
            class_id = int(detections[0, 0, i, 1])
            if CLASSES[class_id] == "person":
                person_found = True
                break

    if person_found and not alert_sent:
        send_push("Person Detected", "Someone was detected on camera!")
        alert_sent = True

    cv2.imshow("Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- Cleanup ---
cap.release()
cv2.destroyAllWindows()
print("Camera stopped.")
