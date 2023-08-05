FROM debian:buster-slim

RUN apt-get update && apt-get install -y wget
WORKDIR /tmp
RUN wget https://github.com/prometheus/prometheus/releases/download/v2.30.3/prometheus-2.30.3.linux-amd64.tar.gz
RUN tar xvf prometheus-2.30.3.linux-amd64.tar.gz
RUN mv prometheus-2.30.3.linux-amd64/prometheus /usr/local/bin
RUN mv prometheus-2.30.3.linux-amd64/promtool /usr/local/bin
RUN mkdir /etc/prometheus
RUN mkdir /var/lib/prometheus
RUN mv prometheus-2.30.3.linux-amd64/consoles /etc/prometheus
RUN mv prometheus-2.30.3.linux-amd64/console_libraries /etc/prometheus

COPY prometheus.yml /etc/prometheus/prometheus.yml

EXPOSE 9090

CMD ["prometheus", "--config.file=/etc/prometheus/prometheus.yml", "--storage.tsdb.path=/var/lib/prometheus"]
