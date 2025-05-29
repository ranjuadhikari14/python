import tkinter as tk
def greet():
    label.config("hello miss")

root=tk.Tk()
root.title("Hello world GUI ")
root.geometry("300x200")

label=tk.Label(root,text="hello Nepalese people!")


button=tk.Button(root,text="Greet me",command=greet)
button.pack(pady=10)
label.pack()

root.mainloop()