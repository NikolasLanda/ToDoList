import tkinter as tk
from tkinter import messagebox
import backend

# Funkce pro aktualizaci seznamu úkolů
def update_listbox():
    listbox.delete(0, tk.END)
    tasks = backend.load_tasks()
    for task in tasks:
        status = "✔" if task["completed"] else "✖"
        listbox.insert(tk.END, f"{status} {task['title']}")

# Přidání nového úkolu
def add_task():
    title = entry.get()
    if title:
        backend.add_task(title)
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Chyba", "Napište úkol!")

# Smazání úkolu
def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        backend.delete_task(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Chyba", "Vyberte úkol k smazání!")

# Označení úkolu jako hotového
def complete_task():
    try:
        selected_index = listbox.curselection()[0]
        backend.complete_task(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Chyba", "Vyberte úkol k označení jako hotový!")

# Označení úkolu jako nesplněného
def uncomplete_task():
    try:
        selected_index = listbox.curselection()[0]
        backend.uncomplete_task(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Chyba", "Vyberte úkol k označení jako nesplněný!")

# Hlavní okno aplikace
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="black")

# Styl tlačítek
button_style = {
    "font": ("Arial", 12),
    "fg": "white",
    "bg": "#007BFF",
    "activebackground": "#0056b3",
    "activeforeground": "white",
    "bd": 2,
    "relief": "ridge",
    "width": 20,
    "pady": 5
}

# Seznam úkolů
listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12), bg="black", fg="white")
listbox.pack(pady=10)

# Vstupní pole
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

# Tlačítka
btn_add = tk.Button(root, text="Přidat úkol", command=add_task, **button_style)
btn_add.pack(pady=5)

btn_complete = tk.Button(root, text="Označit jako hotové", command=complete_task, **button_style)
btn_complete.pack(pady=5)

btn_uncomplete = tk.Button(root, text="Označit jako nesplněné", command=uncomplete_task, **button_style)
btn_uncomplete.pack(pady=5)

btn_delete = tk.Button(root, text="Smazat úkol", command=delete_task, **button_style)
btn_delete.pack(pady=5)

# Aktualizace seznamu na začátku
update_listbox()

# Spuštění aplikace
root.mainloop()
