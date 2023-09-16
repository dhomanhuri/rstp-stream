docker build -t fs_rtsp_stream-app:latest .
docker run -d -it -v /var/www/html/fs_rtsp_stream:/python-docker -p 1895:5000 --name fs_rtsp_stream fs_rtsp_stream-app:latest