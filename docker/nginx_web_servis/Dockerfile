FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y nginx

COPY default.conf /etc/nginx/sites-available/default
COPY index.html /var/www/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
