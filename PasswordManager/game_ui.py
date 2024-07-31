from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

image_holder = []


class GameUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50, bg="white")

        self.canvas = Canvas(self.window, width=200, height=200, bg="white", highlightthickness=0)

        global image_holder
        logo_image = PhotoImage(file="logo.png")
        image_holder.append(logo_image)

        self.canvas.create_image(100, 100, image=logo_image)
        self.canvas.grid(row=0, column=1)

        self.web_site_label = Label(text="Website:", font=("Arial", 12, "normal"), fg="black", bg="white")
        self.web_site_label.grid(row=1, column=0)

        self.web_site_input = Entry(width=21, fg="black", bg="white", highlightthickness=0)
        self.web_site_input.grid(row=1, column=1)

        self.search_button = Button(text="Search", width=12, highlightbackground="white", command=self.find_password)
        self.search_button.grid(row=1, column=2)

        self.email_label = Label(text="Email/Username:", font=("Arial", 12, "normal"), fg="black", bg="white")
        self.email_label.grid(row=2, column=0)

        self.email_input = Entry(width=38, fg="black", bg="white", highlightthickness=0)
        self.email_input.insert(0, "mansy@gmail.com")
        self.email_input.grid(row=2, column=1, columnspan=2)

        self.pass_label = Label(text="Password:", font=("Arial", 12, "normal"), fg="black", bg="white")
        self.pass_label.grid(row=3, column=0)

        self.pass_input = Entry(width=21, fg="black", bg="white", highlightthickness=0)
        self.pass_input.grid(row=3, column=1)

        self.generate_pass_button = Button(text="Generate Password", width=12, highlightbackground="white",
                                           command=self.generate_password)
        self.generate_pass_button.grid(row=3, column=2)

        self.add_button = Button(text="Add", width=36, highlightbackground="white", command=self.save_to_json_file)
        self.add_button.grid(row=34, column=1, columnspan=2)

        self.web_site_input.focus_set()

        self.window.mainloop()

    def generate_password(self):
        password_list = [choice(letters) for _ in range(randint(8, 10))]
        password_list += [choice(numbers) for _ in range(randint(2, 4))]
        password_list += [choice(symbols) for _ in range(randint(2, 4))]

        shuffle(password_list)

        psw = "".join(password_list)

        self.pass_input.delete(0, END)
        self.pass_input.insert(0, psw)

        pyperclip.copy(psw)

    def save_to_file(self):
        if self.validated():
            web_site = self.web_site_input.get()
            email = self.email_input.get()
            psw = self.pass_input.get()
            is_ok = messagebox.askokcancel(title="Website", message=f"These are details entered:\nWebsite: "
                                                                    f"{web_site}\nEmail/Username: "
                                                                    f"{email}\nPassword: {psw}\n\nDo you want to save?")
            if is_ok:
                with open(file="PasswordEntries.txt", mode="a") as f:
                    f.writelines(f"{web_site} | {email} | {psw}\n")

                self.web_site_input.delete(0, END)
                self.pass_input.delete(0, END)
                self.web_site_input.focus()

    def validated(self):
        web_site = self.web_site_input.get()
        if len(web_site) == 0:
            messagebox.showerror(title="Website", message="Please don't leave  Website empty!")
            self.web_site_input.focus()
            return False

        psw = self.pass_input.get()
        if len(psw) == 0:
            messagebox.showerror(title="Website", message="Please don't leave Password empty!")
            self.pass_input.focus()
            return False

        return True

    def save_to_json_file(self):
        if self.validated():
            web_site = self.web_site_input.get().title()
            email = self.email_input.get()
            psw = self.pass_input.get()

            is_ok = messagebox.askokcancel(title="Website", message=f"These are details entered:\nWebsite: "
                                                                    f"{web_site}\nEmail/Username: "
                                                                    f"{email}\nPassword: {psw}\n\nDo you want to save?")
            if is_ok:
                new_data = {
                    web_site: {
                        "Email": email,
                        "Password": psw,
                    }
                }

                try:
                    with open(file="PasswordEntries.json", mode="r") as data_file:
                        # Reading old data
                        data = json.load(data_file)
                except FileNotFoundError as e:
                    print(e)
                    # Creating the file: PasswordEntries.json
                    # Saving the new & first data
                    with open(file="PasswordEntries.json", mode="w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                    # Updating the old data, just appending the new data
                    data.update(new_data)

                    # Saving the updated data into the file:PasswordEntries.json
                    with open(file="PasswordEntries.json", mode="w") as data_file:
                        json.dump(data, data_file, indent=4)
                finally:
                    self.web_site_input.delete(0, END)
                    self.pass_input.delete(0, END)
                    self.web_site_input.focus()

    def find_password(self):
        web_site = self.web_site_input.get().title()
        email = self.email_input.get()
        if len(web_site) == 0 or len(email) == 0:
            messagebox.showerror(title="Website", message="Please enter Website and Email to search.")

            if len(web_site) == 0:
                self.web_site_input.focus()
            elif len(email) == 0:
                self.email_input.focus()

            return

        password = ""
        try:
            with open(file="PasswordEntries.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Password Manager", message="No Data File Found!")
        else:
            if web_site in data:
                password = data[web_site]["Password"]
                messagebox.showinfo(title=web_site, message=f"Email/Username: {email}\n Password: {password}")
            else:
                messagebox.showinfo(title="Password Manager", message=f"No details for {web_site} exist!")
        finally:
            self.pass_input.delete(0, END)
            self.pass_input.insert(0, password)
