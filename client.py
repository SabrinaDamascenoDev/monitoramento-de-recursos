import platform
import socket
import psutil
import time
import json
import os

SERVER_IP = "0.tcp.sa.ngrok.io"
SERVER_PORT = 10173

def get_ponto_montagem():
    if os.name == "nt":
        return "C:\\"
    else:
        return "/"

def coletar_dados():
    ponto = get_ponto_montagem()
    return {
        "hostname": socket.gethostname(),
        "sistema": platform.system(),
        "cpu": psutil.cpu_percent(interval=1),
        "memoria": psutil.virtual_memory().percent,
        "disco": psutil.disk_usage(ponto).percent
    }
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_IP, SERVER_PORT))
    print("Conectado ao servidor de monitoramento.")

    try:
        while True:
            dados = coletar_dados()
            mensagem = json.dumps(dados)
            sock.sendall(mensagem.encode())
            time.sleep(2)
    except KeyboardInterrupt:
        print("Encerrando cliente.")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
