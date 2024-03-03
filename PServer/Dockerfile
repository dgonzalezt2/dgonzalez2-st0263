FROM python:3.11-slim
EXPOSE 50051
WORKDIR /code
COPY ./PServer/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN mkdir /files
COPY ./PServer .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]