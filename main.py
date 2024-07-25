from tkinter import *
from tkinter import messagebox
import random
import json

#---------------------------- FIND PASSWORD -------------------------------------#

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f" Email: {email}\n Password: {password}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exist.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear_entries():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def save():
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get(),
        }
    }
    is_empty = website_entry.get() == "" or password_entry.get() == ""

    if is_empty:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            save_file = open("data.json", "r")
            data = json.load(save_file)
            data.update(new_data)
            save_file.close()
        except FileNotFoundError:
            save_file = open("data.json", "w")
            json.dump(new_data, save_file, indent=4)
            save_file.close()
        else:
            save_file = open("data.json", "w")
            json.dump(data, save_file, indent=4)
            save_file.close()
        finally:
            clear_entries()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row =2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries

website_entry = Entry(width=27)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=37)
email_entry.grid(column=1, row=2, columnspan = 2)
email_entry.insert(0, "Default@email.com")

password_entry = Entry(width=27)
password_entry.grid(column=1, row=3)

# buttons
generate_ps_button = Button(text="Generate Password", command=generate_password, width=15)
generate_ps_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()