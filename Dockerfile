FROM python:3.9

WORKDIR /tag-counter-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/main.py"]p
