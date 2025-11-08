# MyFinTech App (Docker Compose Project)

This is a 2-tier web application built to practice Docker Compose. It consists of a Python Flask backend (the API) and an Nginx frontend (the web server), orchestrated entirely by Docker Compose.

## 🏛️ Application Architecture

The application runs as two distinct services in their own containers, which are connected by a custom user-defined bridge network.

![2-tier application architecture with frontend and backend services]

### 1. The `frontend` Service
* **Purpose:** Serves the static `index.html` file to the user.
* **Container:** `nginx:alpine`
* **Directory:** `./frontend`
* **Port:** Exposed on the host at `http://localhost:8080`.

### 2. The `backend` Service
* **Purpose:** Serves a simple Python Flask API.
* **Container:** `python:3.10-slim`
* **Directory:** `./backend`
* **Port:** Exposed on the host at `http://localhost:5000` for direct API testing.

### 3. The `fintech-net` Network
* **Type:** Custom user-defined bridge network.
* **Purpose:** Allows the `frontend` and `backend` services to communicate with each other using their service names (e.g., the frontend can make an API call to `http://backend:5000/api/test`). This provides secure service discovery and isolates the application.

---

## 🚀 How to Run

### Prerequisites
* Docker
* Docker Compose

### 1. Clone the Repository
```bash
git clone https://github.com/voncleph/fintech-app-docker.git
cd fintech-app-docker
```

### 2. Build and Run

Use the `docker compose up` command. The `--build` flag is recommended for the first run to build the images from their Dockerfiles.

```bash
docker compose up -d --build
```

### 3. Verify

* **Frontend:** Open your browser to `http://localhost:8080`
  * You should see: "Welcome to MyFinTech App"
* **Backend:** Open your browser to `http://localhost:5000/api/test`
  * You should see: `{"message":"Hello from the FinTech Backend!"}`

## 🛑 How to Stop

To stop and remove all containers and the network:

```bash
docker compose down
```

---

## 📝 Git Setup

### Add, Commit, and Push Everything

```bash
# Stage all files
git add .

# Make the first commit
git commit -m "Initial 2-tier app (Flask + Nginx) with Docker Compose"

# Set your main branch name
git branch -M main

# Connect to the GitHub repo
git remote add origin https://github.com/voncleph/fintech-app-docker.git

# Push your code
git push -u origin main
```