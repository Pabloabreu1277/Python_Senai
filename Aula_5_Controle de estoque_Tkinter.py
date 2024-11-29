import tkinter as tk
from tkinter import messagebox
#pip install tk
# Inicializando o estoque
Produto_Led_6W = 1000
produto = "LED 6W"


# Função para atualizar o estoque e mostrar mensagens
def atualizar_estoque():
    global Produto_Led_6W

    # Pegando a quantidade de retirada do campo de entrada
    try:
        Retirada_Estoque = int(entry_retirada.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")
        return

    # Atualizando o estoque
    Produto_Led_6W -= Retirada_Estoque

    # Exibindo a quantidade retirada e o saldo atual
    label_resultado.config(text=f"Sua solicitação: {Retirada_Estoque}\nSaldo atual: {Produto_Led_6W}")

    # Verificando condições de alerta
    if Produto_Led_6W <= 100 and Produto_Led_6W >= 0:
        messagebox.showwarning("Alerta", "Você atingiu o limite mínimo de 100 unidades. Solicite uma compra.")
    elif Produto_Led_6W < 0:
        messagebox.showerror("Erro", "Solicitação não permitida. Você não tem mais estoque.")
        Produto_Led_6W += Retirada_Estoque  # Reverte a retirada inválida


# Criando a janela principal
root = tk.Tk()
root.title("Controle de Estoque")
root.geometry("300x250")
root.configure(bg="#f4e1d2")  # Cor de fundo em tom pastel

# Criando widgets da interface
label_instrucoes = tk.Label(root, text="Controle de movimentação de estoque", bg="#f4e1d2", font=("Arial", 12))
label_instrucoes.pack(pady=10)

label_estoque = tk.Label(root, text=f"Estoque atual: {Produto_Led_6W} unidades", bg="#f4e1d2", font=("Arial", 10))
label_estoque.pack(pady=5)

label_retirada = tk.Label(root, text=f"Quantidade de retirada do produto {produto}:", bg="#f4e1d2", font=("Arial", 10))
label_retirada.pack(pady=5)

entry_retirada = tk.Entry(root, font=("Arial", 10))
entry_retirada.pack(pady=5)

button_atualizar = tk.Button(root, text="Atualizar Estoque", command=atualizar_estoque, bg="#d0b9b9",
                             font=("Arial", 10))
button_atualizar.pack(pady=10)

label_resultado = tk.Label(root, text="", bg="#f4e1d2", font=("Arial", 10))
label_resultado.pack(pady=5)

# Executando o loop da interface
root.mainloop()
