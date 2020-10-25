FROM python:3.7-alpine

WORKDIR /app/backend
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

