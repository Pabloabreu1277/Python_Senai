#pip install tk
import tkinter as tk
from tkinter import messagebox

#Função para calcular notas
def calcular_media():
    try:
        # Obtém as notas inseridas
        nota1 = float(entry_nota1.get())
        nota2 = float(entry_nota2.get())
        nota3 = float(entry_nota3.get())
        nota4 = float(entry_nota4.get())

        # Calcula a média
        media = (nota1 + nota2 + nota3 + nota4) / 4

        # Exibe a média para o usuário
        label_resultado.config(text=f'Média: {media:.2f}')

    except ValueError:
        # Caso o usuário insira um valor inválido
        messagebox.showerror("Erro", "Por favor, insira valores válidos para as notas.")


# Criação da janela principal
root = tk.Tk()
root.title("Calculadora de Média")

# Layout
label_instrucao = tk.Label(root, text="Insira as 4 notas do aluno:")
label_instrucao.grid(row=0, column=0, columnspan=2, pady=10)

# Labels para as notas
label_nota1 = tk.Label(root, text="Nota 1:")
label_nota1.grid(row=1, column=0, padx=10, pady=5)

label_nota2 = tk.Label(root, text="Nota 2:")
label_nota2.grid(row=2, column=0, padx=10, pady=5)

label_nota3 = tk.Label(root, text="Nota 3:")
label_nota3.grid(row=3, column=0, padx=10, pady=5)

label_nota4 = tk.Label(root, text="Nota 4:")
label_nota4.grid(row=4, column=0, padx=10, pady=5)

# Entradas para as notas
entry_nota1 = tk.Entry(root)
entry_nota1.grid(row=1, column=1, padx=10, pady=5)

entry_nota2 = tk.Entry(root)
entry_nota2.grid(row=2, column=1, padx=10, pady=5)

entry_nota3 = tk.Entry(root)
entry_nota3.grid(row=3, column=1, padx=10, pady=5)

entry_nota4 = tk.Entry(root)
entry_nota4.grid(row=4, column=1, padx=10, pady=5)

# Botão para calcular a média
botao_calcular = tk.Button(root, text="Calcular Média", command=calcular_media)
botao_calcular.grid(row=5, column=0, columnspan=2, pady=20)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="Média: ")
label_resultado.grid(row=6, column=0, columnspan=2)

# Inicia a interface gráfica
root.mainloop()
