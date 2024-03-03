FROM python:3.11-slim
WORKDIR /
RUN mkdir /central
COPY ./serverCentral/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./serverCentral .
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]