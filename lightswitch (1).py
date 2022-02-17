import tkinter as tk
import random
window = tk.Tk()

button = tk.Button(text='klik hier!', bg="white", fg="black")
button.pack(pady = 200, padx = 200)
lst = ['red', 'green', 'purple', 'yellow']

# schijf hier tussen je code
buttonClicked = 0
def functie():
    global buttonClicked
    if buttonClicked == 0:
        print('test1')
        window.config(bg=random.choice(lst))
        button = tk.Button(text='Hello World', bg="black", fg="white")
        buttonClicked += 1
    elif buttonClicked == 1:
        print('test2')
        window.config(bg=random.choice(lst))
        button = tk.Button(text='Hello World', bg="white", fg="black")
        buttonClicked -= 1
button.config(command=functie)
# schijf hier tussen je code

window.mainloop()