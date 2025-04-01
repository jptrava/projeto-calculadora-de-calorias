import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class Pessoa:
    def __init__(self, peso, altura, idade, nivel_atividade, intensidade_atividade):
        self.peso = peso
        self.altura = altura
        self.idade = idade
        self.nivel_atividade = nivel_atividade
        self.intensidade_atividade = intensidade_atividade

    def calcular_BMR(self):
        return (10 * self.peso) + (6.25 * self.altura) - (5 * self.idade) + 5

    def ajustar_intensidade(self, fator_atividade):
        if self.intensidade_atividade == "leve":
            return fator_atividade * 1.0  
        elif self.intensidade_atividade == "moderada":
            return fator_atividade * 1.1  
        elif self.intensidade_atividade == "pesada":
            return fator_atividade * 1.2 
        else:
            raise ValueError("Intensidade de atividade inválida!")

    def calcular_TDEE(self):
        BMR = self.calcular_BMR()
        if self.nivel_atividade == "sedentário":
            fator_atividade = 1.2
        elif self.nivel_atividade == "levemente ativo":
            fator_atividade = 1.375
        elif self.nivel_atividade == "moderadamente ativo":
            fator_atividade = 1.55
        elif self.nivel_atividade == "muito ativo":
            fator_atividade = 1.725
        else:
            raise ValueError("Nível de atividade inválido!")

        fator_atividade = self.ajustar_intensidade(fator_atividade)
        return BMR * fator_atividade

# Função para exibir gráfico
def exibir_grafico(BMR, TDEE):
    atividades = ["Sedentário", "Levemente ativo", "Moderadamente ativo", "Muito ativo"]
    fatores = [1.2, 1.375, 1.55, 1.725]
    tdee_valores = [BMR * fator for fator in fatores]

    plt.figure(figsize=(8, 5))
    plt.bar(atividades, tdee_valores, color=["skyblue", "orange", "green", "red"])
    plt.axhline(TDEE, color="black", linestyle="--", label=f"Seu TDEE ({TDEE:.2f} kcal)")
    plt.xlabel("Nível de Atividade Física")
    plt.ylabel("TDEE (Calorias)")
    plt.title("TDEE com Base no Nível de Atividade Física")
    plt.legend()
    plt.show()

def calcular_resultados():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        idade = int(entry_idade.get())
        atividade = nivel_atividade_var.get()
        intensidade = intensidade_atividade_var.get()

        pessoa = Pessoa(peso, altura, idade, atividade, intensidade)
        BMR = pessoa.calcular_BMR()
        TDEE = pessoa.calcular_TDEE()

        messagebox.showinfo("Resultados", f"BMR: {BMR:.2f} kcal\nTDEE: {TDEE:.2f} kcal")
        exibir_grafico(BMR, TDEE)
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos!")

# Interface gráfica com Tkinter
janela = tk.Tk()
janela.title("Calculadora de TDEE")
janela.geometry("500x400")
janela.configure(bg="#f0f8ff")

titulo = tk.Label(janela, text="Calculadora de TDEE", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#333")
titulo.pack(pady=10)

frame = tk.Frame(janela, bg="#f0f8ff")
frame.pack(pady=10, padx=10)

tk.Label(frame, text="Peso (kg):", font=("Helvetica", 12), bg="#f0f8ff").grid(row=0, column=0, pady=5, sticky="w")
entry_peso = tk.Entry(frame, font=("Helvetica", 12))
entry_peso.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Altura (cm):", font=("Helvetica", 12), bg="#f0f8ff").grid(row=1, column=0, pady=5, sticky="w")
entry_altura = tk.Entry(frame, font=("Helvetica", 12))
entry_altura.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Idade (anos):", font=("Helvetica", 12), bg="#f0f8ff").grid(row=2, column=0, pady=5, sticky="w")
entry_idade = tk.Entry(frame, font=("Helvetica", 12))
entry_idade.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Nível de Atividade:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=3, column=0, pady=5, sticky="w")
nivel_atividade_var = tk.StringVar(value="sedentário")
tk.OptionMenu(frame, nivel_atividade_var, "sedentário", "levemente ativo", "moderadamente ativo", "muito ativo").grid(row=3, column=1, pady=5)

tk.Label(frame, text="Intensidade da Atividade:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=4, column=0, pady=5, sticky="w")
intensidade_atividade_var = tk.StringVar(value="leve")
tk.OptionMenu(frame, intensidade_atividade_var, "leve", "moderada", "pesada").grid(row=4, column=1, pady=5)

botao_calcular = tk.Button(janela, text="Calcular TDEE", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=calcular_resultados)
botao_calcular.pack(pady=20)

rodape = tk.Label(janela, text="Desenvolvido com ❤️ em Python", font=("Helvetica", 10), bg="#f0f8ff", fg="#555")
rodape.pack(side="bottom", pady=10)

janela.mainloop()
