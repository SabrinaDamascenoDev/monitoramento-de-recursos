import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_monitoramento.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

clientes = df["hostname"].unique()

for cliente in clientes:
    dados_cliente = df[df["hostname"] == cliente]

    plt.figure()
    plt.plot(dados_cliente["timestamp"], dados_cliente["cpu_%"], label="CPU (%)")
    plt.plot(dados_cliente["timestamp"], dados_cliente["ram_%"], label="RAM (%)")
    plt.plot(dados_cliente["timestamp"], dados_cliente["disco_%"], label="Disco (%)")

    plt.xlabel("Tempo")
    plt.ylabel("Uso (%)")
    plt.title(f"Uso de Recursos - {cliente}")
    plt.legend()
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
