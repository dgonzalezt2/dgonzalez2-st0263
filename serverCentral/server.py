from fastapi import FastAPI, HTTPException, Request
from typing import List, Dict, Any
import json
import os
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class UploadFileBody(BaseModel):
    file_name: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Archivos JSON
peers_file = "/central/peers.json"
files_file = "/central/files.json"


# Función para cargar archivos JSON
def load_json_file(filename: str) -> Dict[str, Any]:
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    return {}


# Función para guardar archivos JSON
def save_json_file(filename: str, data: Dict[str, Any]) -> None:
    with open(filename, "w") as file:
        json.dump(data, file)


# Método POST para registrar un nodo
@app.post("/register_node/")
def register_node(node_data: Dict[str, Any], request: Request) -> Dict[str, str]:
    ip = request.client.host
    files = node_data.get("files")
    peers = load_json_file(peers_file)
    peers_list = peers.get("peers", [])
    if ip not in peers_list:
        peers_list.append(ip)
    peers["peers"] = peers_list
    save_json_file(peers_file, peers)

    files_data = load_json_file(files_file)
    files_data[ip] = files
    save_json_file(files_file, files_data)

    return {"message": "Node registered successfully"}


# Método GET para listar los archivos disponibles
@app.get("/list_files/")
def list_files() -> Dict[str, Dict[str, List[str]]]:
    files_data = load_json_file(files_file)
    return {"files": files_data}


# Método POST para subir un archivo
@app.post("/upload_file/")
def upload_file(request: Request, body: UploadFileBody) -> Dict[str, str]:
    files_data = load_json_file(files_file)
    ip = request.client.host
    files_data[ip].append(body.file_name)
    save_json_file(files_file, files_data)
    return {"message": "File uploaded successfully"}


# Método GET para obtener un archivo en específico
@app.get("/get_file/")
def get_file(file_name: str) -> Dict[str, str]:
    files_data = load_json_file(files_file)
    for ip, files in files_data.items():
        if file_name in files:
            return {"ip": ip, "file_name": file_name}
    raise HTTPException(status_code=404, detail="File not found")


# Verificar y cargar los archivos JSON al iniciar la aplicación
@app.on_event("startup")
async def startup_event():
    if not os.path.exists(peers_file):
        save_json_file(peers_file, {"peers": []})
    if not os.path.exists(files_file):
        save_json_file(files_file, {})
