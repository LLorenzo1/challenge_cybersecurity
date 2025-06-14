import customtkinter as ctk
from auth.login import TelaLogin

def main():
    ctk.set_appearance_mode("dark")  # ou "light"
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Sistema Seguro")
    root.geometry("400x350")
    TelaLogin(master=root)
    root.mainloop()

if __name__ == "__main__":
    main()
