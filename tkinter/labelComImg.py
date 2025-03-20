import tkinter as tk
from tkinter import ttk, PhotoImage

def centralizar_imagem(event):
    largura_janela = janela.winfo.width()
    altura_janela = janela.winfo.height()
    largura_imagem = imagem.width()
    altura_imagem = imagem.height()

    posicao_x = (largura_janela - largura_imagem) // 2
    posicao_y = (altura_janela - altura_imagem) // 2

    lbl_imagem.place(x=posicao_x, y=posicao_y)


janela = tk.Tk()
janela.title("Exibindo imagens")
janela.geometry("400x250")

#carregando imagem

imagem = PhotoImage(file = 'imagens/cat.png')

lbl_imagem = ttk.Label(janela, image=imagem)

lbl_gatinho = ttk.Label(
    janela,
    text= "Gatinho Amarelo",
    foreground= "red",
    background= "lightblue",
    anchor= "center",
    borderwidth= 3,
    relief= "groove"
)
lbl_gatinho.pack(pady=20)

#centralizando imagem
janela.bind("<Configure>", centralizar_imagem)

lbl_imagem.pack(pady=20)


janela.mainloop()

