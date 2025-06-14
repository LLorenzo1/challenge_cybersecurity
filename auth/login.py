import customtkinter as ctk
from tkinter import messagebox
import json
import os
from security.hashing import verify_password
from security.token import gerar_token
from form.questions import TelaFormulario
from logs.logger import registrar_acao

USERS_PATH = os.path.join("data", "users.json")
SESSION_PATH = os.path.join("data", "session.json")

class TelaLogin(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(pady=20, padx=20, fill="both", expand=True)
        self.criar_widgets()

    def criar_widgets(self):
        ctk.CTkLabel(self, text="Login", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        self.entry_email = ctk.CTkEntry(self, placeholder_text="Email")
        self.entry_email.pack(pady=10)
        self.entry_senha = ctk.CTkEntry(self, placeholder_text="Senha", show="*")
        self.entry_senha.pack(pady=10)
        ctk.CTkButton(self, text="Entrar", command=self.login).pack(pady=10)
        ctk.CTkButton(self, text="Cadastre-se", command=self.abrir_cadastro, fg_color="gray").pack(pady=5)

    def login(self):
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get().strip()

        if not os.path.exists(USERS_PATH):
            messagebox.showerror("Erro", "Nenhum usuário cadastrado.")
            return

        with open(USERS_PATH, "r") as file:
            try:
                usuarios = json.load(file)
            except:
                usuarios = {}

        if email not in usuarios or not verify_password(senha, usuarios[email]):
            messagebox.showerror("Erro", "Email ou senha inválidos.")
            return

        token = gerar_token()
        with open(SESSION_PATH, "w") as file:
            json.dump({"email": email, "token": token}, file, indent=4)

        registrar_acao(email, "Login bem sucedido")

        messagebox.showinfo("Sucesso", "Login bem sucedido!")
        self.master.destroy()
        root = ctk.CTk()
        TelaFormulario(master=root)
        root.mainloop()

    def abrir_cadastro(self):
        from auth.register import TelaCadastro
        self.master.destroy()
        root = ctk.CTk()
        TelaCadastro(master=root)
        root.mainloop()
