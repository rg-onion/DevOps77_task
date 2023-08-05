FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y nginx

COPY default.conf /etc/nginx/nginx.conf
COPY reverse_proxy.conf /etc/nginx/nginx.conf

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
