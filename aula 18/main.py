import tkinter as tk

def mostrar(event = None):
    mostrar_nome  = entry_nome.get() 
    mostrar_text.config(text= mostrar_nome)
    # mostrar_text.

janela = tk.Tk()
janela.geometry('500x500')
nome = tk.Label(janela, text = 'Nome')  

entry_nome = tk.Entry(janela)
entry_nome.pack(pady=10)

entry_nome.bind("<Return>", mostrar)

btn = tk.Button(janela, text='clique aqui', command=mostrar)
btn.pack(pady=10)



mostrar_text = tk.Label(janela, text = '')
mostrar_text.pack(pady=10)

janela.mainloop()