from tkinter import *
import requests


image_holder = []

BACKGROUND_COLOR = "white"
FONT_NAME = "Arial"


class QuoteUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Kanye Says...")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.canvas = Canvas(self.window, width=300, height=414, bg=BACKGROUND_COLOR, highlightthickness=0)

        global image_holder
        background_img = PhotoImage(file="background.png")
        kanye_img = PhotoImage(file="kanye.png")
        image_holder.append(background_img)
        image_holder.append(kanye_img)

        self.canvas.create_image(150, 207, image=background_img)
        self.quote_text = self.canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250,
                                                  font=("Arial", 30, "bold"), fill=BACKGROUND_COLOR)
        self.canvas.grid(row=0, column=0)

        self.kanye_button = Button(image=kanye_img, highlightthickness=0, command=self.get_quote,
                                   highlightbackground=BACKGROUND_COLOR)
        self.kanye_button.grid(row=1, column=0)

        self.window.mainloop()

    def get_quote(self):
        response = requests.get("https://api.kanye.rest")
        response.raise_for_status()
        quote = response.json()["quote"]
        self.canvas.itemconfig(self.quote_text, text=quote, fill=BACKGROUND_COLOR)

