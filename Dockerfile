# ---------- Stage 1: Build ----------
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build dependencies for psycopg2-binary
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------- Stage 2: Runtime ----------
FROM python:3.12-slim

WORKDIR /app

# Only the minimal runtime library needed by psycopg2
RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq5 && \
    rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

# Render injects PORT env var; default to 10000
ENV PORT=10000

# Expose the port
EXPOSE ${PORT}

# Run with gunicorn — bind to 0.0.0.0:$PORT
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT main:app"]
