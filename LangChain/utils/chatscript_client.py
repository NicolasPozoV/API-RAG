import socket

def send_to_chatscript(user_id: str, message: str) -> str:
    HOST = "localhost"  # O la IP del contenedor si usás Docker en red puente
    PORT = 1024

    def receive_full_response(sock: socket.socket, buffer_size=4096) -> str:
        data = b""
        while True:
            part = sock.recv(buffer_size)
            if not part:
                break
            data += part
            if b"\0" in part:
                break
        return data.decode("utf-8").strip("\0").strip()

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(f"{user_id}\0{message}\0".encode("utf-8"))
            response = receive_full_response(s)
            return response
    except Exception as e:
        print(f"[ERROR ChatScript] {e}")
        return ""
