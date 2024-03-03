FROM python

WORKDIR /service/
COPY ./grpcServer/requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY ./grpcServer/file.proto .
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. file.proto

COPY ./grpcServer/server.py .
RUN mkdir /files

EXPOSE 50051
ENTRYPOINT [ "python", "server.py" ]