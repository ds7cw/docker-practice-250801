FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy notebooks into the container
COPY notebooks/ notebooks/

# Jupyter listens on 8888 by default
EXPOSE 8888

# Launch Jupyter Notebook server
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token="]

# docker build -t pandas-notebook-demo .
# docker run -p 8888:8888 pandas-notebook-demo
# docker run -p 127.0.0.1:8888:8888 pandas-notebook-demo