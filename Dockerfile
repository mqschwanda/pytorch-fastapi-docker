FROM python:3.12-slim AS python
 
WORKDIR /app 

COPY app/requirements.txt . 

RUN pip install -r requirements.txt 