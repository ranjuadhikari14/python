import tkinter as tk
from tkinter import messagebox
def findsum():
    num1=entry1.get()
    num2=entry2.get()
    if num1.isdigit() and num2.isdigit():
        result= int(num1)+int(num2)
        messagebox.showinfo("result", f"sum:{result}")
    else:
        messagebox.showerror("Error","Enter valid number")




root=tk.Tk()
root.title("calculator")
root.geometry("500x500")
#label=tk.Label(root,text="Add")
entry1=tk.Entry(root)
entry1.pack(pady=5)

entry2=tk.Entry(root)
entry2.pack(pady=5)
button=tk.Button(root,text="Add",command="findsum()")


button.pack(pady=10)

root.mainloop()