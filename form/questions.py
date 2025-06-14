import customtkinter as ctk
from tkinter import messagebox

class TelaFormulario(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        if not self.validar_sessao():
            messagebox.showerror("Sessão inválida", "Você precisa estar logado para acessar o formulário.")
            master.destroy()
            return

        self.pack(fill="both", expand=True)
        self.respostas = {}
        self.criar_widgets()

    def validar_sessao(self):
        import os
        import json
        session_path = os.path.join("data", "session.json")

        if not os.path.exists(session_path):
            return False

        try:
            with open(session_path, "r") as f:
                dados = json.load(f)
                token = dados.get("token", "")
                email = dados.get("email", "")
                return bool(token and email)
        except:
            return False

    def criar_widgets(self):
        ctk.CTkLabel(self, text="Perfil de Apostador", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)

        scroll = ctk.CTkScrollableFrame(self, width=500, height=400)
        scroll.pack(padx=10, pady=10, fill="both", expand=True)

        # 1. Já apostou?
        ctk.CTkLabel(scroll, text="1. Você já apostou alguma vez?").pack(anchor="w", pady=5)
        self.var_apostou = ctk.StringVar(value="")
        ctk.CTkRadioButton(scroll, text="Sim", variable=self.var_apostou, value="Sim").pack(anchor="w")
        ctk.CTkRadioButton(scroll, text="Não", variable=self.var_apostou, value="Não").pack(anchor="w")

        # 2. Quanto aposta por mês?
        ctk.CTkLabel(scroll, text="2. Em média, quanto você aposta por mês?").pack(anchor="w", pady=5)
        self.var_valor = ctk.StringVar(value="")
        opcoes_valor = ["Menos de R$ 50", "De R$ 50 a R$ 200", "De R$ 200 a R$ 1.000", "Mais de R$ 1.000"]
        for op in opcoes_valor:
            ctk.CTkRadioButton(scroll, text=op, variable=self.var_valor, value=op).pack(anchor="w")

        # 3. Como você se sente após apostar?
        ctk.CTkLabel(scroll, text="3. Como você se sente após apostar?").pack(anchor="w", pady=5)
        self.var_sentimento = ctk.StringVar(value="")
        opcoes_sentimento = ["Muito bem", "Indiferente", "Arrependido", "Ansioso"]
        for op in opcoes_sentimento:
            ctk.CTkRadioButton(scroll, text=op, variable=self.var_sentimento, value=op).pack(anchor="w")
        self.entry_sentimento_outro = ctk.CTkEntry(scroll, placeholder_text="Outro (especifique)")
        self.entry_sentimento_outro.pack(anchor="w", padx=20, pady=5)

        # 4. Você gostaria de receber orientações financeiras?
        ctk.CTkLabel(scroll, text="4. Você gostaria de receber orientações financeiras?").pack(anchor="w", pady=5)
        self.var_orientacao = ctk.StringVar(value="")
        ctk.CTkRadioButton(scroll, text="Sim", variable=self.var_orientacao, value="Sim").pack(anchor="w")
        ctk.CTkRadioButton(scroll, text="Não", variable=self.var_orientacao, value="Não").pack(anchor="w")

        # Botão Enviar
        ctk.CTkButton(self, text="Enviar", command=self.enviar_formulario).pack(pady=15)

    def enviar_formulario(self):
        self.respostas["Já apostou?"] = self.var_apostou.get()
        self.respostas["Valor médio apostado"] = self.var_valor.get()
        self.respostas["Sentimento após apostar"] = self.var_sentimento.get() or self.entry_sentimento_outro.get()
        self.respostas["Quer orientação financeira?"] = self.var_orientacao.get()

        if "" in self.respostas.values():
            messagebox.showerror("Erro", "Responda todas as perguntas.")
            return

        
        self.mostrar_resumo()

    def mostrar_resumo(self):
        self.master.destroy()

        perfil = self.avaliar_perfil()

        janela = ctk.CTk()
        janela.title("Resumo do Perfil")
        janela.geometry("1000x400")

        ctk.CTkLabel(janela, text="Análise do seu Perfil", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

        box = ctk.CTkTextbox(janela, width=460, height=200, corner_radius=10)
        box.pack(padx=10, pady=10)
        box.insert("0.0", perfil)
        box.configure(state="disabled")

        ctk.CTkButton(janela, text="Fechar", command=janela.destroy).pack(pady=5)
        janela.mainloop()

    def avaliar_perfil(self):
        apostou = self.respostas.get("Já apostou?")
        valor = self.respostas.get("Valor médio apostado")
        sentimento = self.respostas.get("Sentimento após apostar")
        orientacao = self.respostas.get("Quer orientação financeira?")

        risco = 0

        if apostou == "Sim":
            risco += 1
        if valor in ["De R$ 200 a R$ 1.000", "Mais de R$ 1.000"]:
            risco += 2
        if sentimento in ["Ansioso", "Arrependido"]:
            risco += 2
        if orientacao == "Sim":
            risco += 1

        if risco <= 1:
            return ("Seu perfil indica um comportamento de **baixo risco**.\n"
                    "Você demonstra pouco envolvimento com apostas e sinais de bom autocontrole.")
        elif risco <= 3:
            return ("Seu perfil indica um comportamento de **risco moderado**.\n"
                    "Você já aposta com alguma frequência e mostra sinais de atenção ao seu comportamento.")
        else:
            return ("⚠️ Atenção: seu perfil sugere um comportamento de **alto risco com apostas**.\n"
                    "É importante buscar apoio, refletir sobre os impactos financeiros e emocionais, e considerar ajuda especializada.")
