import cv2
import imutils

camera = cv2.VideoCapture(
    "rtsp://admin:IGMYQO@192.168.1.49:554/Streaming/Channels/101/")

human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')


def gen_frames():
    while True:
        success, frame = camera.read()  # read the camera frame

        try:
            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            humans = human_cascade.detectMultiScale(gray, 1.9, 1)

            if human_cascade.empty():
                print("Gagal memuat model cascade.")
            else:
                print("Model cascade berhasil dimuat.")
                human_cascade = cv2.CascadeClassifier(
                    'haarcascade_fullbody.xml')
            # Mencoba mendeteksi manusia
            # # Display the resulting frame
            for (x, y, w, h) in humans:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

        except cv2.error as e:
            print(f"Error saat mendeteksi manusia: {e}")
