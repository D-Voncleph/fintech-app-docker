# 3-Tier FinTech Application (Docker Compose)

This is a complete 3-tier web application built with Docker Compose. It consists of:

1. **Frontend:** Nginx (acting as a reverse proxy)
2. **Backend:** Python Flask API
3. **Database:** PostgreSQL

The entire stack is orchestrated by Docker Compose, allowing it to be run with a single command.

## ✨ Key Features
* **3-Tier Architecture:** Complete separation of concerns (Nginx Frontend, Flask Backend, Postgres DB).
* **Docker Compose:** Full stack orchestration with a single entry point.
* **Multi-Stage Builds:** Optimized Dockerfiles for reduced image size and enhanced security.
* **Private Networking:** Backend and Database are isolated on a custom bridge network with no public ports exposed.
* **Reverse Proxy:** Nginx configured to route traffic and hide backend services.

## 🐳 Docker Hub Images

The container images for this project are hosted publicly on Docker Hub:

* **Backend API:** [voncleph/fintech-backend](https://hub.docker.com/r/voncleph/fintech-backend)
* **Frontend Proxy:** [voncleph/fintech-frontend](https://hub.docker.com/r/voncleph/fintech-frontend)

## 🏛️ Application Architecture

The application runs as three distinct services, all connected by a private, custom bridge network.

### 1. The `frontend` Service

* **Purpose:** Public-facing reverse proxy.
* **Image:** `voncleph/fintech-frontend:v1` (or builds locally)
* **Proxy Logic:** Forwards `/api/` requests to the backend.
* **Public Port:** `http://localhost:8080`

### 2. The `backend` Service

* **Purpose:** Private Python Flask API.
* **Image:** `voncleph/fintech-backend:1.0` (Pulled from Docker Hub)
* **Security:** No public ports exposed.
* **Internal Port:** `http://backend:5000`

### 3. The `db` Service

* **Purpose:** Private PostgreSQL database.
* **Image:** `postgres:14-alpine`
* **Persistence:** Uses named volume `db-data`.

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

### 2. Create the Environment File

Create a file named `.env` in the root of the project:

```bash
touch .env
```

Paste the following content:

```
POSTGRES_USER=voncleph
POSTGRES_DB=fintech_db
POSTGRES_PASSWORD=mysecretpassword
DATABASE_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}"
```

### 3. Start the Application

Run the stack. Docker Compose will automatically pull the backend image from Docker Hub.

```bash
docker compose up -d
```

### 4. Verify

* Open browser to `http://localhost:8080`
* Status should read: `Backend Connection Status: Successfully connected to the Postgres database!`

## 🛑 How to Stop

```bash
docker compose down
```
