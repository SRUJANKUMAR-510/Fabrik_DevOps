# Use the NGINX official image from Docker Hub
FROM nginx

# Copy the content of the local 'editor' folder to the NGINX root directory
COPY editor /usr/share/nginx/html

# Expose port 80 to allow outside access
EXPOSE 80

# Command to start NGINX and run it in the foreground
CMD ["nginx", "-g", "daemon off;"]

