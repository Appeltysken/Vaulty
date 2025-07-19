FROM python:3.11-alpine3.22

LABEL maintainer="normanrey" \
      version="1.0" \
      description="Minimal Flask-based app for demonstrating NoSQL injections" \
      repository="https://github.com/Appeltysken/Vault" \
      challenge.type="CTF"

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
