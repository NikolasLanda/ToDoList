import tkinter as tk
from tkinter import messagebox
import backend

def update_listbox():
    listbox.delete(0, tk.END)
    tasks = backend.load_tasks()
    for index, task in enumerate(tasks):
        status = "[✓]" if task["completed"] else "[ ]"
        listbox.insert(tk.END, f"{status} {task['title']}")

def add_task():
    title = entry.get()
    if title:
        backend.add_tasks(title)
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Chyba", "Napište úkol!")

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        backend.delete_tasks(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Chyba", "Vyberte úkol k smazání!")

def complete_task():
    try:
        selected_index = listbox.curselection()[0]
        backend.complete_tasks(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Chyba", "Vyberte úkol k označení jako hotový!")

def uncomplete_task():
    try:
        selected_index = listbox.curselection()[0]
        backend.uncomplete_tasks(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Chyba", "Vyberte úkol k označení jako nesplněný!")

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack()

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

btn_add = tk.Button(root, text="Přidat úkol", command=add_task)
btn_add.pack(pady=2)

btn_complete = tk.Button(root, text="Označit jako hotové", command=complete_task)
btn_complete.pack(pady=2)

btn_uncomplete = tk.Button(root, text="Označit jako nesplněné", command=uncomplete_task)
btn_uncomplete.pack(pady=2)

btn_delete = tk.Button(root, text="Smazat úkol", command=delete_task)
btn_delete.pack(pady=2)

update_listbox()

root.mainloop()
