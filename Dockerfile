FROM python:3.10.0-bullseye

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "my_app.py"]
