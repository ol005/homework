FROM python:3.12.4

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY import_taxi_data.py import_taxi_data.py

ENTRYPOINT ["python", "import_taxi_data.py"]