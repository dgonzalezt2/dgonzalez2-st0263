FROM python:3.11-slim
WORKDIR /code
COPY ./PClient/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./PClient .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]