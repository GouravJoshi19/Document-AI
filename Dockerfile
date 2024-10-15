# Use the official Python image from Docker Hub
FROM python:3.8-slim
COPY . /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN  pip install -r requirements.txt  # Install Python dependencies

CMD streamlit run streamlit_app.py
 