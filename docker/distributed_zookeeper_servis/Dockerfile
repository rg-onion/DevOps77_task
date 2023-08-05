FROM debian:buster-slim

RUN apt-get update && \
    apt-get install -y wget openjdk-11-jdk-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV ZOOKEEPER_VERSION 3.9.0
ARG MY_ID

RUN wget "https://downloads.apache.org/zookeeper/zookeeper-$ZOOKEEPER_VERSION/apache-zookeeper-$ZOOKEEPER_VERSION-bin.tar.gz" && \
    tar -xzf "apache-zookeeper-$ZOOKEEPER_VERSION-bin.tar.gz" && \
    mv "apache-zookeeper-$ZOOKEEPER_VERSION-bin" zookeeper && \
    rm "apache-zookeeper-$ZOOKEEPER_VERSION-bin.tar.gz"

COPY zoo.cfg /app/zookeeper/conf/
RUN mkdir -p /tmp/zookeeper && echo "${ZOO_MY_ID}" > /tmp/zookeeper/myid


CMD ["/app/zookeeper/bin/zkServer.sh", "start-foreground"]
