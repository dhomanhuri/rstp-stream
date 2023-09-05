import cv2
import imutils

# Load pre-trained HOG detector for human detection
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Create VideoCapture object
cap = cv2.VideoCapture('video.mp4')

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Resize the frame for faster processing (optional)
    frame = imutils.resize(frame, width=min(800, frame.shape[1]))

    # Detect humans in the frame
    (rects, weights) = hog.detectMultiScale(
        frame, winStride=(4, 4), padding=(8, 8), scale=1.05)

    # Draw rectangles around detected humans
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Human Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
