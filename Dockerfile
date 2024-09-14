FROM python:3-alpine

WORKDIR /app

COPY ./ /app

RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0:8000"]

# docker build -t image_name
# docker exec -it con_name sh -c 'python3 manage.py makemigrations && python3 manage.py migrate'
# docker run -p 8000:8000 -d image_nam
