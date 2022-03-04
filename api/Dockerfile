FROM python:3.9-slim-buster

RUN apt-get update && apt-get install git -y
#RUN apt-get update && apt-get install build-essential -y

COPY . /api

WORKDIR /api

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]