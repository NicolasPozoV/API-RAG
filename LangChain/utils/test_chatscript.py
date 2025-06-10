import socket

HOST = "localhost"
PORT = 1024

user_id = "usuario1"
message = "hola"

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(f"{user_id}\0{message}\0".encode("utf-8"))
        response = s.recv(4096).decode("utf-8")
        print(f"Respuesta ChatScript: {response!r}")
except Exception as e:
    print(f"[ERROR ChatScript] {e}")
