import cv2

# Alamat RTSP stream
rtsp_url = 'rtsp://admin:IGMYQO@192.168.1.51:554/Streaming/Channels/101/'

# Buka koneksi ke stream RTSP
cap = cv2.VideoCapture(rtsp_url)

while True:
    # Ambil frame dari stream
    ret, frame = cap.read()

    if not ret:
        print("Tidak bisa membaca frame dari stream.")
        break

    # Tampilkan frame
    cv2.imshow('RTSP Stream', frame)

    # Keluar loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup koneksi dan jendela tampilan
cap.release()
cv2.destroyAllWindows()
