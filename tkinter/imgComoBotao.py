import tkinter as tk

janela = tk.Tk()
janela.title("Botão com imagem")
janela.geometry('300x300')


#funcao fechar janela

def fechar_janela():
    janela.destroy()



imagem = tk.PhotoImage(file='imagens/botao.png')

#criar botao com a image

bota_imagem = tk.Button(janela, image=imagem, command=fechar_janela)

bota_imagem.pack(pady=10)

janela.mainloop()