FROM debian:buster-slim

RUN apt-get update && apt-get install -y python3 daemontools

WORKDIR /app

COPY /home/aid/DevOps_77task/docker/daemon_servis/myservice/run /app/myservice/run
COPY /home/aid/DevOps_77task/docker/daemon_servis/daemon_script.py /app/daemon_script.py

RUN chmod +x /app/myservice/run
RUN chmod +x /app/daemon_script.py

CMD ["svscan", "/app"]
