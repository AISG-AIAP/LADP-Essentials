# Flowise Chat Docker Deployment

This project contains a simple HTML page with an embedded Flowise chatbot, deployed using Docker and nginx.

## Prerequisites

- Docker installed on your system
- Docker Compose (optional, but recommended)

## Quick Start

### Option 1: Using Docker Compose (Recommended)

```bash
# Build and start the container
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the container
docker-compose down
```

The application will be available at: http://localhost:8080

### Option 2: Using Docker Commands

```bash
# Build the Docker image
docker build -t flowise-chat .

# Run the container
docker run -d -p 8080:80 --name flowise-chat-app flowise-chat

# View logs
docker logs -f flowise-chat-app

# Stop and remove the container
docker stop flowise-chat-app
docker rm flowise-chat-app
```

## Configuration

- **Port**: The application runs on port 8080 by default. You can change this in `docker-compose.yml` or the docker run command.
- **HTML Content**: Modify `flowise.html` to update your chatbot configuration.

## Deployment Notes

The Docker image uses:
- **Base Image**: nginx:alpine (lightweight, ~24MB)
- **Web Server**: nginx
- **Port**: 80 (internal), mapped to 8080 (host)

## Troubleshooting

### Check if container is running
```bash
docker ps
```

### View container logs
```bash
docker logs flowise-chat-app
```

### Access container shell
```bash
docker exec -it flowise-chat-app sh
```

### Rebuild after changes
```bash
# With docker-compose
docker-compose up -d --build

# With docker
docker build -t flowise-chat . && docker run -d -p 8080:80 --name flowise-chat-app flowise-chat
```

