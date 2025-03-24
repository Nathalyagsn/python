import tkinter as tk
from tkinter import ttk, messagebox

#caixa de dialogo

def mostrar_mensagem():
    messagebox.showinfo("Login", "Login efetuado com sucesso.")
    janela.destroy


janela = tk.Tk()
janela.title("Exemplo de Pack")
janela.geometry("200x180")
janela.resizable(False,False)


#widget
lbl_login = ttk.Label(text='Login', background="lightblue")
lbl_login.configure(anchor="center")
lbl_usuario = ttk.Label(text='Usuário:')
txt_usuario = ttk.Entry()
lbl_senha = ttk.Label(text='Senha:')
txt_senha = ttk.Entry(show="*")
btn_login = ttk.Button(text='Login', command=mostrar_mensagem)

lbl_login.pack(fill="both", expand=True)
lbl_usuario.pack(anchor="w", padx=10, pady=5)
txt_usuario.pack(anchor="w", padx=10, pady=5, fill="x")
lbl_senha.pack(anchor="w",padx=10, pady=5)
txt_senha.pack(anchor="w", padx=10, pady=5, fill="x")
btn_login.pack(anchor="e", padx=10, pady=5)

janela.mainloop()