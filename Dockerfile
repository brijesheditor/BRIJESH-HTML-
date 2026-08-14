FROM python:3.9.6-alpine3.14

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD gunicorn app:app & python3 main.py


