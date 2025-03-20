import tkinter as tk

def abrir_segunda_janela():
    segunda_janela = tk.Toplevel()
    segunda_janela.title("Segunda Janela")
    segunda_janela. config(bg = "lightpink")

    #tamanho da janela

    largura_janela = 300
    altura_janela = 200

    #obtendo dimensão da janela do usuario

    largura_tela = segunda_janela.winfo_screenwidth()
    altura_tela = segunda_janela.winfo_screenheight()


    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2

    segunda_janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")



#criando janela principal

janela_principal = tk.Tk()
janela_principal.title("Janela Principal")
janela_principal.geometry("600x500")

#evento de click
janela_principal.bind("<Button-1>", lambda event: abrir_segunda_janela())


#abrir janela

janela_principal.mainloop()


