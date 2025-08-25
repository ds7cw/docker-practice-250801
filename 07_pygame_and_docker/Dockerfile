FROM python:3.11-slim

# Install system dependencies for Pygame/SDL
RUN apt-get update && apt-get install -y --no-install-recommends \
    libSDL2-2.0-0 \
    libSDL2-image-2.0-0 \
    libSDL2-mixer-2.0-0 \
    libSDL2-ttf-2.0-0 \
    libportmidi0 \
    libfreetype6 \
    libjpeg62-turbo \
    libpng16-16 \
    fonts-dejavu-core \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Optional: avoid ALSA warnings when no audio device is present
ENV SDL_AUDIODRIVER=dummy
# We'll use X11 for graphics; adapt at runtime in docker run command
ENV SDL_VIDEODRIVER=x11

# Create app directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole tetris source tree
COPY . .

# Set default run command
CMD ["python", "main.py"]