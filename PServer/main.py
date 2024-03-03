from contextlib import asynccontextmanager
from fastapi import FastAPI, UploadFile, Request, HTTPException
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
import os
import httpx
from typing import Any
from fastapi.middleware.cors import CORSMiddleware
from grpcServer import serve
import threading

url = os.getenv("CENTRAL_HOST")

@asynccontextmanager
async def lifespan(app: FastAPI):
    files = os.listdir("/files")
    data = {"files": files}

    try:
        response = httpx.post(f"{url}/register_node/", json=data)

        if response.status_code == 200:
            print("Node registrado exitosamente.")
        else:
            print(
                f"Error al registrar el nodo. Código de estado: {response.status_code}"
            )
            print(response.content)
    except httpx.RequestError as e:
        print(f"Error en la solicitud: {e}")
    thread1 = threading.Thread(target=serve)
    thread1.start()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

import grpc
import file_pb2
import file_pb2_grpc

MAX_MESSAGE_LENGTH = 1024 * 1024 * 1024  # 1 GB en bytes


@app.get("/download/{filename}")
async def download_file(ip: str, filename: str):
    channel = grpc.insecure_channel(
        f"{ip}:50051",
        options=[
            ("grpc.max_send_message_length", MAX_MESSAGE_LENGTH),
            ("grpc.max_receive_message_length", MAX_MESSAGE_LENGTH),
        ],
    )
    stub = file_pb2_grpc.FileTransferStub(channel)
    response = stub.DownloadFile(file_pb2.FileRequest(filename=filename))
    file_name = f"/files/{filename}"
    with open(file_name, "wb") as f:
        f.write(response.content)

    httpx.post(f"{url}/upload_file/", json={"file_name": filename})
    return FileResponse(file_name)


@app.get("/list_files/")
async def list_files() -> dict[str, Any]:
    response = httpx.get(f"{url}/list_files/")
    return response.json()


@app.get("/get_file/{file_name}")
async def get_file(file_name: str, request: Request) -> FileResponse:
    response = httpx.get(f"{url}/get_file/", params={"file_name": file_name})

    if response.status_code == 200:
        file_path = os.path.join("/files", file_name)
        return FileResponse(file_path, filename=file_name)
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)


@app.post("/upload_file/")
async def upload_file(file: UploadFile) -> dict[str, Any]:
    with open(f"/files/{file.filename}", mode="wb") as f:
        f.write(await file.read())

    response = httpx.post(f"{url}/upload_file/", json={"file_name": file.filename})
    return response.json()
