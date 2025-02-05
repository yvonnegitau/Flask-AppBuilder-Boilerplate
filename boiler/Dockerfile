FROM python:3.10-slim

# Set environment variables to control the runtime behavior of your application.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]