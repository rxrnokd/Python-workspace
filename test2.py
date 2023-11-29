import tkinter as tk

def create_buttons():
    for i in range(5):
        button = tk.Button(root, text=f"Button {i}", command=lambda i=i: print(f"Button {i} clicked"))
        button.grid(row=i, column=0)
        buttons.append(button)

def delete_all_buttons():
    for button in buttons:
        button.destroy()
    buttons.clear()

root = tk.Tk()
buttons = []

create_buttons_button = tk.Button(root, text="Create Buttons", command=create_buttons)
create_buttons_button.grid(row=0, column=1)

delete_buttons_button = tk.Button(root, text="Delete All Buttons", command=delete_all_buttons)
delete_buttons_button.grid(row=1, column=1)

root.mainloop()
