import socket
import threading
import json
import csv
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5000
CSV_FILE = "dados_monitoramento.csv"

lock = threading.Lock()

def salvar_csv(hostname, sistema, cpu, memoria, disco):
    with lock:
        with open(CSV_FILE, mode="a", newline="") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                hostname,
                sistema,
                cpu,
                memoria,
                disco
            ])


def tratar_cliente(conn, addr):
    print(f"[CONECTADO] Cliente {addr}")

    try:
        while True:
            dados = conn.recv(1024)
            if not dados:
                break

            info = json.loads(dados.decode())

            print(f"\nCliente {addr}")
            print(f"CPU: {info['cpu']}% | RAM: {info['memoria']}% | Disco: {info['disco']}%")

            salvar_csv(
                info["hostname"],
                info["sistema"],
                info["cpu"],
                info["memoria"],
                info["disco"]
            )

    except Exception as e:
        print(f"[ERRO] Cliente {addr} - {e}")
    finally:
        conn.close()
        print(f"[DESCONECTADO] Cliente {addr}")

def criar_csv():
    try:
        with open(CSV_FILE, mode="x", newline="") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([
                "timestamp",
                "hostname",
                "sistema",
                "cpu_%",
                "ram_%",
                "disco_%"
            ])

    except FileExistsError:
        pass

def main():
    criar_csv()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[SERVIDOR ATIVO] Escutando na porta {PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=tratar_cliente, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()
