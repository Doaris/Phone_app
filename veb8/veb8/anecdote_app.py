import tkinter as tk
import random


def load_anecdots(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().splitlines()


def show_random_anecdote():
    random_anecdote = random.choice(anecdotes)
    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)  
    text_widget.insert(tk.END, random_anecdote) 
    text_widget.config(state=tk.DISABLED)  


root = tk.Tk()
root.title("Случайный анекдот")


anecdotes = load_anecdots("anecdotes.txt")

button = tk.Button(root, text="Случайный анекдот", command=show_random_anecdote)
text_widget = tk.Text(root, wrap=tk.WORD, width=40, height=10)
text_widget.config(state=tk.DISABLED)  


button.pack(pady=10)
text_widget.pack()


root.mainloop()
