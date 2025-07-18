FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install flask && \
    pip install pymongo

EXPOSE 5000

CMD ["python", "app.py"]
