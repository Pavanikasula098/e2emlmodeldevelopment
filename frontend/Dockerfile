# Dockerfile for Streamlit frontend
FROM python:3.9-slim

WORKDIR /app

COPY ../requirements.txt .

COPY . .
RUN pip install -r requirements.txt

# Copy Streamlit app files


EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
