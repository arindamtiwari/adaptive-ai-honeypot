import socket

HOST = '0.0.0.0'
PORT = 2222

def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    
    print(f"Honeypot listening on port {PORT}")

    while True:
        client, addr = server.accept()
        print(f"Connection from {addr}")
        client.send(b"Access Denied\n")
        client.close()

if __name__ == "__main__":
    start_honeypot()
