import random
import string
import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Ramdom Password Generator")
root.configure(bg="skyblue")

def generate_random_password():
    # Define character sets
    length = entry.get()
    if length.isdigit():
        entry.delete(0,tk.END)
        num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
        upper_str = list(string.ascii_uppercase)
        lower_str = list(string.ascii_lowercase)

    # Convert num to strings
        num = [str(x) for x in num]

    # Combine character sets
        combine = num + symbols + upper_str + lower_str

    # Generate random password
        password = ''.join(random.choices(combine, k=int(length)))
        output.delete(0,tk.END)
        output.insert(0, password)
    else:
        output.delete(0,tk.END)
        output.insert(0,"Enter the Correct Number")
        entry.delete(0, tk.END)
def clearoutput():
    output.delete(0,tk.END)
#create label text
text  = tk.Label(root,text="Enter length of Password",font="arial 15 bold",width=50, height=2,bg="skyblue").pack()
# create entry box for getting length
entry = tk.Entry(root,text = "Enter The Number", width=10, font="arial 20")
entry.pack()
# "create" button created.
submit = tk.Button(root, text = "Create", font="arial 15", bg="#1e02f2", fg="white", width=15, command=generate_random_password).place(x = 109,y =100)
output = tk.Entry(root,text = "Output", font="arial 15",fg = "red", bg = "lightyellow", width=25, background = "skyblue", borderwidth=0)
output.place(x = 80, y = 150)
clear = tk.Button(root, text = "Clear", font="arial 15", bg="red", fg="white", width=15, command=clearoutput).place(x = 109,y =200)
root.mainloop()

