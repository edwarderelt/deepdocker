FROM nvidia/cuda:12.2.2-devel-ubuntu22.04

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    pkg-config \
    libssl-dev \
    libclang-dev \
    python3.10 \
    python3.10-dev \
    python3.10-distutils \
    python3-pip \
    ca-certificates \
    libopus-dev \
    cmake \
    nginx \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv

# Install Rust (stable)
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

ENV CUDA_COMPUTE_CAP=86
ENV CANDLE_CUDA_FORCE=1

# Install moshi-server with CUDA support
RUN cargo install --features cuda moshi-server

# Create app directory
WORKDIR /app

# # Copy configuration files first
# COPY health_server.py /app/
# COPY nginx.conf /app/
# COPY supervisord.conf /app/
# COPY startup.sh /app/

# Make scripts executable
# RUN chmod +x /app/health_server.py /app/startup.sh

# Copy your project files
COPY . /app
RUN chmod +x /app/health_server.py /app/startup.sh
# Create required directories
RUN mkdir -p /var/log/nginx /var/log/supervisor

# Expose only the main port
EXPOSE 8080

# Use the startup script
CMD ["/app/startup.sh"]