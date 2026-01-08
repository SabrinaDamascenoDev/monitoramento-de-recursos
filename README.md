# 🖧 Sistema de Monitoramento Remoto via TCP Sockets

Sistema cliente-servidor para monitoramento remoto de CPU, memória RAM e disco,
utilizando **comunicação TCP via sockets**.  
Desenvolvido como trabalho final da disciplina de **Redes de Computadores**.

---

## 🚀 Funcionalidades

- Comunicação TCP via sockets
- Suporte a múltiplos clientes simultâneos
- Monitoramento de CPU, RAM e Disco
- Armazenamento dos dados em CSV
- Funciona em Windows e Linux
- Comunicação entre máquinas em redes diferentes (via túnel TCP)

---

## 🛠️ Tecnologias

- Python 3
- socket / threading
- psutil
- ngrok (tunelamento TCP)

---

## 📦 Requisitos

- Python 3.8+
- pip

Instalar dependência:
```bash
pip install psutil
