import socket
import datetime

HOST = '0.0.0.0'
PORT = 2222

def log_connection(addr):
    with open("logs/honeypot.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - Connection from {addr}\n")

def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[+] Honeypot running on port {PORT}")

    while True:
        client, addr = server.accept()
        print(f"[!] Connection from {addr}")

        log_connection(addr)

        client.send(b"Access Denied\n")
        client.close()

if __name__ == "__main__":
    start_honeypot()
