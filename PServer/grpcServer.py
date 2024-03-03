import grpc
import concurrent.futures
import file_pb2
import file_pb2_grpc
import logging
MAX_MESSAGE_LENGTH = 1024 * 1024 * 1024  # 1 GB en bytes

class FileTransferServicer(file_pb2_grpc.FileTransferServicer):
    def DownloadFile(self, request, context):
        logging.info("recibi una solicitud")
        logging.info(request)
        file_content = b''
        with open(f"/files/{request.filename}", 'rb') as f:
            file_content = f.read()
        return file_pb2.FileResponse(content=file_content)

def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=1), options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
    ],)
    file_pb2_grpc.add_FileTransferServicer_to_server(FileTransferServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    