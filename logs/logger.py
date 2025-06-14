import datetime
import os

LOG_PATH = os.path.join("data", "logs.txt")

def registrar_acao(usuario, acao):
    with open(LOG_PATH, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {usuario} - {acao}\n")
