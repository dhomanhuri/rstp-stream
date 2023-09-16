import cv2

# Alamat RTSP stream
rtsp_url = 'rtsp://admin:IGMYQO@id24.tunnel.my.id:3454//Streaming/Channels/101/'

# Buka koneksi ke stream RTSP
cap = cv2.VideoCapture(rtsp_url)

human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
while True:
    # Ambil frame dari stream
    ret, frame = cap.read()

    if not ret:
        print("Tidak bisa membaca frame dari stream.")
        break

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray, 1.9, 1)

    # Display the resulting frame
    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Tampilkan frame
    cv2.imshow('RTSP Stream', frame)

    # Keluar loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup koneksi dan jendela tampilan
cap.release()
cv2.destroyAllWindows()
