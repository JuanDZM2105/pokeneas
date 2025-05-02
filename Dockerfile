FROM python:3.11-slim

WORKDIR /app

COPY . .

# Install Flask
RUN pip install -r requirements.txt

# Expose the required port
EXPOSE 80

CMD ["python", "app.py"]