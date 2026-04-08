FROM python:latest
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

#COPY flask.main.py /app
#COPY config.yml /app
COPY . /app

EXPOSE 8000
CMD ["python3", "flask.main.py"]