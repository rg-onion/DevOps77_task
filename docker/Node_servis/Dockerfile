FROM debian:buster-slim

RUN apt-get update && apt-get install -y wget
WORKDIR /tmp
RUN wget https://github.com/prometheus/node_exporter/releases/download/v1.2.2/node_exporter-1.2.2.linux-amd64.tar.gz
RUN tar xvf node_exporter-1.2.2.linux-amd64.tar.gz
RUN mv node_exporter-1.2.2.linux-amd64/node_exporter /usr/local/bin

EXPOSE 9100

CMD ["node_exporter"]
