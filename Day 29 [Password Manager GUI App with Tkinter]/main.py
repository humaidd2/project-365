from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()

    with open("data.json", mode="r") as file:
        search_file = json.load(file)
        try:
            acc_file = search_file[website]
            email = acc_file["email"]
            password = acc_file["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        except KeyError:
            messagebox.showerror(title="Key Error", message=f"Sorry, Details on {website} does not exist.")
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Opps", message="Please dont leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white", highlightthickness=0)

canvas = Canvas(width=200, height=200, bg="white")
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

website_entry = Entry(width=30)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

email_entry = Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "humaidd2@gmail.com")

password_label = Label(text="Password", bg="white")
password_label.grid(row=3, column=0)

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

generate_p_button = Button(text="Generate Password", command=generate_password)
generate_p_button.grid(row=3, column=2)

add_button = Button(text="Add", width=40, command=save)
add_button.grid(columnspan=2, column=1, row=4)

search_button = Button(text="Search", command=search_password)
search_button.grid(column=2, row=1)

window.mainloop()