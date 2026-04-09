FROM python:3.13.5
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY /templates/ /app/templates
COPY config.yml ./
COPY flask.main.py ./

EXPOSE 8000
CMD ["python3", "flask.main.py"]