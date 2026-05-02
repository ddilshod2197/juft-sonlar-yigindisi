import tkinter as tk

def chiqar():
    for widget in root.winfo_children():
        widget.destroy()

    for i in range(1, 101):
        label = tk.Label(root, text=str(i))
        label.pack()

root = tk.Tk()
root.title("1 dan 100 gacha sonlar")

button = tk.Button(root, text="Chiqar", command=chiqar)
button.pack()

chiqar()

root.mainloop()
