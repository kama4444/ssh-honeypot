#Kamron O.
import socket
import paramiko
import threading

HOST = "0.0.0.0"
PORT = 22
LOG_FILE = "data/login_attempts.log"

host_key = paramiko.RSAKey.generate(2048)
class HoneypotServer(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        with open(LOG_FILE, "a") as log:
            log.write(f"Login attempt - Username: {username}, Password: {password}\n")
        return paramiko.AUTH_FAILED

def handle_connection(client):
    transport = paramiko.Transport(client)
    try:
        transport.add_server_key(host_key)
        server = HoneypotServer()
        transport.start_server(server=server)
        chan = transport.accept(5)
        if chan:
            chan.close()
    except paramiko.ssh_exception.SSHException:
        pass
    finally:
        transport.close()

def listen_forever():
    sock = socket.socket()
    sock.bind((HOST, PORT))
    sock.listen(100)
    print(f"[*] SSH Honeypot running on {HOST}:{PORT}")

    while True:
        client, addr = sock.accept()
        threading.Thread(target=handle_connection, args=(client,)).start()

if __name__ == "__main__":
    listen_forever()
