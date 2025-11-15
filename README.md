# 3-Tier FinTech Application (Docker Compose)

This is a complete 3-tier web application built with Docker Compose. It consists of:

1. **Frontend:** Nginx (acting as a reverse proxy)
2. **Backend:** Python Flask API
3. **Database:** PostgreSQL

The entire stack is orchestrated by Docker Compose, allowing it to be run with a single command.

## 🏛️ Application Architecture

The application runs as three distinct services, all connected by a private, custom bridge network.

### 1. The `frontend` Service

* **Purpose:** The only public-facing service. It serves the static `index.html` file and acts as a **reverse proxy**.
* **Proxy Logic:** All requests starting with `/api/` are forwarded to the `backend` service over the private Docker network.
* **Container:** `nginx:alpine`
* **Directory:** `./frontend`
* **Public Port:** `http://localhost:8080`

### 2. The `backend` Service

* **Purpose:** The Python Flask API. It handles business logic and is the only service that can communicate with the database.
* **Security:** This container is **not** exposed to the public. It has no `ports` mapped and can only be reached by the `frontend` service.
* **Container:** `python:3.10-slim`
* **Directory:** `./backend`
* **Internal Port:** `http://backend:5000` (used by Nginx)

### 3. The `db` Service

* **Purpose:** The PostgreSQL database for storing all application data.
* **Security:** This container is also **not** exposed to the public. It can only be reached by the `backend` service.
* **Data Persistence:** Uses a Docker **named volume** `db-data` to ensure all database data is saved even if the container is stopped or removed.
* **Container:** `postgres:14-alpine`
* **Internal Hostname:** `db` (used by the backend)

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

This is a critical, one-time setup step. The application requires a `.env` file for its secrets and configuration.

Create a file named `.env` in the root of the project:

```bash
touch .env
```

Paste the following content into the new `.env` file:

```
# For the PostgreSQL container
POSTGRES_USER=voncleph
POSTGRES_DB=fintech_db
POSTGRES_PASSWORD=mysecretpassword

# For the Backend (Python) container
DATABASE_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}"
```

(This `.env` file is in the `.gitignore` and will not be committed to GitHub).

### 3. Build and Run

With the `.env` file in place, you can build and run the entire 3-tier stack with a single command. The `--build` flag is recommended for the first run.

```bash
docker compose up -d --build
```

### 4. Verify

Wait about 30 seconds for all services to initialize.

* Open your browser to `http://localhost:8080`
* You should see: `Backend Connection Status: Successfully connected to the Postgres database!`

## 🛑 How to Stop

To stop and remove all containers, networks, and services:

```bash
docker compose down
```

(Note: This command does not remove your `db-data` named volume. Your data is safe.)

## 📝 Push Your Updated Documentation

Save the `README.md` file. Now, commit this final change to GitHub.

```bash
# Add the changed README file
git add README.md

# Commit the change
git commit -m "Docs: Update README for 3-tier architecture"

# Push to GitHub
git push origin main
```
