FROM python:alpine

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY app.py app.py

CMD ["python", "-m", "flask", "run"]