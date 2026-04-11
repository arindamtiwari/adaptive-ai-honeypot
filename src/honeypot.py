import socket
from datetime import datetime

HOST = '0.0.0.0'
PORT = 2222

def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[+] Honeypot running on port {PORT}")

    while True:
        client, addr = server.accept()
        ip, port = addr

        print(f"[!] Connection from {ip}:{port}")

        log_entry = f"{datetime.now()} | IP: {ip} | Port: {port}\n"

        with open("logs/honeypot.log", "a") as log:
            log.write(log_entry)

        client.send(b"Fake SSH Service\nLogin failed\n")
        client.close()

if __name__ == "__main__":
    start_honeypot()
