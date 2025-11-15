# Use the standard nginx image
FROM nginx:alpine

# Copy our custom nginx.conf
# This file tells Nginx how to act as a proxy
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy our website's files
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
