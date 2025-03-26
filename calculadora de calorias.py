# Para estimar **quantos minutos de treino por dia** e **quantas calorias consumir por dia** com base na sua massa muscular atual e na sua meta de massa muscular, precisamos considerar alguns fatores:

# ### 1️⃣ **Gasto energético diário total (TDEE)**
# O TDEE inclui:
#    - Taxa Metabólica Basal (BMR) → calorias que seu corpo queima em repouso.  
#    - Gasto com atividades físicas e treino.  

# ### 2️⃣ **Superávit calórico necessário para ganhar massa muscular**  
#    - Para ganhar músculo, é necessário consumir **calorias acima do TDEE**.  
#    - O crescimento muscular médio para um iniciante pode ser de **0,2 a 0,5 kg/mês** (ou seja, **~200 a 500 g por mês**).requer cerca de **5.000 a 7.000 kcal de superávit**.  

# ### 3️⃣ **Tempo de treino ideal**  
#    - O tempo de treino varia, mas geralmente é recomendado **45 a 75 minutos por dia**, 4 a 6 vezes por semana.  
#    - Volume de treino (séries e repetições) é mais importante que a duração exata.  


#    \[
#    BMR = (10 \times \text{peso}) + (6.25 \times \text{altura}) - (5 \times \text{idade}) + 5
#    \]

# 2. **Estimamos seu TDEE** multiplicando o BMR pelo fator de atividade:

#    - Sedentário (pouco exercício) → × 1.2  
#    - Levemente ativo (1 a 3 treinos/semana) → × 1.375  
#    - Moderadamente ativo (3 a 5 treinos/semana) → × 1.55  
#    - Muito ativo (6 a 7 treinos/semana) → × 1.725  

# 3. **Calculamos a ingestão calórica necessária** para ganho de músculo:  

#    \[
#    \text{Calorias diárias} = TDEE + 250 \text{ a } 500 \text{ kcal (superávit)}
#    \]

# ---
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class Pessoa:
    def __init__(self, peso, altura, idade, nivel_atividade):
        self.peso = peso
        self.altura = altura
        self.idade = idade
        self.nivel_atividade = nivel_atividade

    def calcular_BMR(self):
        return (10 * self.peso) + (6.25 * self.altura) - (5 * self.idade) + 5

    def calcular_TDEE(self):
        BMR = self.calcular_BMR()
        if self.nivel_atividade == "sedentário":
            return BMR * 1.2
        elif self.nivel_atividade == "levemente ativo":
            return BMR * 1.375
        elif self.nivel_atividade == "moderadamente ativo":
            return BMR * 1.55
        elif self.nivel_atividade == "muito ativo":
            return BMR * 1.725
        else:
            raise ValueError("Nível de atividade inválido!")

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

        pessoa = Pessoa(peso, altura, idade, atividade)
        BMR = pessoa.calcular_BMR()
        TDEE = pessoa.calcular_TDEE()

        messagebox.showinfo("Resultados", f"BMR: {BMR:.2f} kcal\nTDEE: {TDEE:.2f} kcal")
        exibir_grafico(BMR, TDEE)
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos!")

janela = tk.Tk()
janela.title("Calculadora de TDEE")
janela.geometry("400x300")
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

botao_calcular = tk.Button(janela, text="Calcular TDEE", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=calcular_resultados)
botao_calcular.pack(pady=20)

rodape = tk.Label(janela, text="Desenvolvido com ❤️ em Python", font=("Helvetica", 10), bg="#f0f8ff", fg="#555")
rodape.pack(side="bottom", pady=10)

janela.mainloop()
