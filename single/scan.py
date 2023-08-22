import socket


def check_rtsp(ip, port, rtsp_path):
    try:
        # Buat koneksi socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(1)  # Batasi waktu tunggu koneksi

        # Coba terhubung ke alamat IP dan port yang diberikan
        client_socket.connect((ip, port))

        # Kirim permintaan RTSP OPTIONS dengan path yang diberikan
        request = f"OPTIONS {rtsp_path} RTSP/1.0\r\n\r\n"
        client_socket.send(request.encode())

        # Terima data dari server
        response = client_socket.recv(1024).decode()

        # Periksa apakah respons mengandung "RTSP" dan "200 OK"
        if "RTSP" in response and "200 OK" in response:
            print(f"IP {ip} memiliki protokol RTSP dengan path {rtsp_path}")
        else:
            print(f"IP {ip} tidak memiliki protokol RTSP dengan path {rtsp_path}")

        # Tutup koneksi
        client_socket.close()

    except Exception as e:
        print(f"Terjadi kesalahan saat memeriksa IP {ip}: {e}")


def main():
    rtsp_path = "/Streaming/Channels/101/"
    # Ganti dengan daftar IP yang ingin Anda periksa
    start_ip = "192.168.1.1"
    end_ip = "192.168.1.255"

    start_octets = list(map(int, start_ip.split('.')))
    end_octets = list(map(int, end_ip.split('.')))

    for octet3 in range(start_octets[2], end_octets[2] + 1):
        for octet4 in range(start_octets[3], end_octets[3] + 1):
            target_ip = f"{start_octets[0]}.{start_octets[1]}.{octet3}.{octet4}"
            check_rtsp(target_ip, 554, rtsp_path)


if __name__ == "__main__":
    main()
