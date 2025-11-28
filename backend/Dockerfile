# ---------- STAGE 1: Builder ----------
# We name this stage "builder"
FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .

# We install dependencies into the user's local directory (~/.local)
# This makes it easy to copy them later.
RUN pip install --user --no-cache-dir -r requirements.txt


# ---------- STAGE 2: Final (Runtime) ----------
# We start fresh with a clean image
FROM python:3.10-slim

WORKDIR /app

# The Magic: Copy only the installed libraries from the "builder" stage
# We copy them to the same location in this new image
COPY --from=builder /root/.local /root/.local

# We must update the PATH so Python finds the installed packages
ENV PATH=/root/.local/bin:$PATH

# Copy the actual application code
COPY app.py .

# Expose the port (internal documentation)
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
