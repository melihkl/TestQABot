# Base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies
RUN npm install

# Build the Vue.js app
RUN npm run build

# Expose port 8080
EXPOSE 8080

# Serve the app
CMD ["npm", "run", "serve"]
