import socket

def send_to_chatscript(user_id: str, message: str, host: str = "localhost", port: int = 1024) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        msg = f"{user_id}\0{user_id}\0{message}\0"
        s.sendall(msg.encode())
        response = s.recv(10000).decode()
    return response.strip()