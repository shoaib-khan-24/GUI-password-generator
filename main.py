from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_button_pressed():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','@','#','$','%','&','*']
    new_password = ""
    for _ in range(4):
        new_password += random.choice(letters)
    for _ in range(2):
        new_password += random.choice(symbols)
    for _ in range(2):
        new_password += random.choice(numbers)
    password_entry.insert(0,new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_pressed():
    website_info = website_entry.get()
    email_info = email_entry.get()
    password_info = password_entry.get()

    if website_info == "" or password_info == "":
        messagebox.showinfo(title="oops" , message="Please don't leave any field empty.")
    else:
        is_ok = messagebox.askokcancel(title="Website",
                                       message=f"Details entered-\nEmail: {email_info}\nPassword: {password_info}\nDo you confirm ?")
        if is_ok:
            with open("data.txt", 'a') as fh:
                fh.write(f"{website_info} | {email_info} | {password_info}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

#window
window = Tk()
window.title("Password generator")
window.config(padx=80 , pady=50)

#canvas
canvas = Canvas(width=200 , height=200)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#labels
website = Label(text="Website:")
website.grid(row=1, column=0)
email = Label(text="Email/Username:")
email.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

#entries
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()                                           #get cursor on it
email_entry = Entry(width=50)
email_entry.insert(0,"khanshoaib@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

#buttons
generate_button = Button(text="Generate password" , command=generate_button_pressed)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=add_button_pressed)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()