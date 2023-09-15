import tkinter as tk

def Janela():
    window = tk.Tk()
    window.title('Produto de um skyscraper sheaf por um vector bundle')
    label = tk.Label(window, text='Hello')
    label.grid(column=0, row=0)
    return window