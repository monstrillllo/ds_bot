import socket
import json


class Connection:
    def __init__(self):
        self.sock = socket.socket()
        self.sock.connect(('25.43.15.16', 8888))
        print('Connected')

    async def send_request(self, request_json: str):
        print('Request: ', request_json)
        self.sock.send(len(request_json).to_bytes(4, 'little', signed=True))
        self.sock.send(request_json.encode())
        data = self.sock.recv(1024).decode()
        print('Data: ', data)
        json_data = json.loads(data)
        return json_data
