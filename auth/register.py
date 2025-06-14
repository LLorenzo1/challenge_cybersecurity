import customtkinter as ctk
from tkinter import messagebox
import json
import os
import re
from security.hashing import hash_password
from logs.logger import registrar_acao

DATA_PATH = os.path.join("data", "users.json")

def senha_segura(senha):
    if len(senha) < 5:
        return False
    if not re.search(r"\d", senha):  # pelo menos um número
        return False
    if not re.search(r"[!@#$%^&*()_+=\\[{\]};:<>|./?,-]", senha):  # pelo menos um caractere especial
        return False
    return True

class TelaCadastro(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(pady=20, padx=20, fill="both", expand=True)
        self.criar_widgets()

    def criar_widgets(self):
        ctk.CTkLabel(self, text="Cadastro", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        self.entry_email = ctk.CTkEntry(self, placeholder_text="Email")
        self.entry_email.pack(pady=10)
        self.entry_senha = ctk.CTkEntry(self, placeholder_text="Senha", show="*")
        self.entry_senha.pack(pady=10)
        ctk.CTkButton(self, text="Cadastrar", command=self.cadastrar).pack(pady=10)
        ctk.CTkButton(self, text="Voltar", command=self.voltar, fg_color="gray").pack(pady=5)

    def cadastrar(self):
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get().strip()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Erro", "Email inválido.")
            return

        if not senha_segura(senha):
            messagebox.showerror(
                "Erro",
                "A senha deve ter no mínimo 5 caracteres,\nconter pelo menos um número e um caractere especial."
            )
            return

        try:
            with open(DATA_PATH, "r") as file:
                usuarios = json.load(file)
        except:
            usuarios = {}

        if email in usuarios:
            messagebox.showerror("Erro", "Usuário já existe.")
            return

        usuarios[email] = hash_password(senha)
        with open(DATA_PATH, "w") as file:
            json.dump(usuarios, file, indent=4)

        registrar_acao(email, "Cadastro realizado")
        messagebox.showinfo("Sucesso", "Cadastro realizado!")
        self.master.after(100, self.voltar)

    def voltar(self):
        from auth.login import TelaLogin
        self.master.destroy()
        root = ctk.CTk()
        TelaLogin(master=root)
        root.mainloop()
