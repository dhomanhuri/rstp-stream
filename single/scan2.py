import socket


def check_rtsp_support(ip, port=554):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout koneksi setiap IP
            s.connect((ip, port))
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False


def main():
    start_ip = "192.168.1.1"  # Ganti dengan alamat IP awal
    end_ip = "192.168.1.254"  # Ganti dengan alamat IP akhir
    port = 554

    print("Mencari perangkat dengan dukungan RTSP...")

    for i in range(int(start_ip.split('.')[-1]), int(end_ip.split('.')[-1]) + 1):
        ip = start_ip.rsplit('.', 1)[0] + '.' + str(i)
        if check_rtsp_support(ip, port):
            print(f"Perangkat dengan alamat IP {ip} mendukung RTSP.")


if __name__ == "__main__":
    main()
