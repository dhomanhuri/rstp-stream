import cv2
# To read from a video file
cap = cv2.VideoCapture('video.mp4')

# To read from the default camera (usually the built-in webcam)
# cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # If the video has ended, break the loop
    if not ret:
        break

    # Display the frame (you can replace this with any processing you want)
    cv2.imshow('Video', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
