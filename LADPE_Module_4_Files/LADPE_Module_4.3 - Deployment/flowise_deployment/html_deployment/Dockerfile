# Use nginx alpine for a lightweight image
FROM --platform=linux/amd64 nginx:alpine

# Copy the HTML file to nginx's default public directory
COPY flowise.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# nginx starts automatically with the base image
CMD ["nginx", "-g", "daemon off;"]

