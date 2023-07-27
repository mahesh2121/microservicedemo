FROM python:3.8-slim

WORKDIR /app

COPY microservice.py requirement.txt /app/

RUN pip install -r requirement.txt

CMD ["python", "microservice.py"]