import re
import tkinter as tk

def check_password():

    password = entry.get()
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search("[A-Z]", password):
        score += 1

    if re.search("[a-z]", password):
        score += 1

    if re.search("[0-9]", password):
        score += 1

    if re.search("[@#$%^&*!]", password):
        score += 1


    if score <= 2:
        result.config(text="Weak", fg="red")
        bar.config(bg="red", width=10)

    elif score <= 4:
        result.config(text="Medium", fg="orange")
        bar.config(bg="orange", width=20)

    else:
        result.config(text="Strong", fg="green")
        bar.config(bg="green", width=30)



root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")


label = tk.Label(root, text="Enter Password")
label.pack(pady=10)


entry = tk.Entry(root, show="*", width=30)
entry.pack()


button = tk.Button(root, text="Check", command=check_password)
button.pack(pady=10)


result = tk.Label(root, text="", font=("Arial", 14))
result.pack()


bar = tk.Label(root, bg="grey", width=5, height=1)
bar.pack(pady=10)


root.mainloop()