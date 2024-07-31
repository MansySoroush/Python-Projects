from tkinter import *
import pandas
from tkinter import messagebox
from random import choice
import json

CARD_FRONT_IMAGE = "CardFrontImage"
CARD_BACK_IMAGE = "CardBackImage"
RIGHT_IMAGE = "RightImage"
WRONG_IMAGE = "WrongImage"

image_holder = {}

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"


class GameUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Flashy")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.canvas = Canvas(self.window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

        global image_holder
        card_front_image = PhotoImage(file="./images/card_front.png")
        card_back_image = PhotoImage(file="./images/card_back.png")
        right_image = PhotoImage(file="./images/right.png")
        wrong_image = PhotoImage(file="./images/wrong.png")
        image_holder[CARD_FRONT_IMAGE] = card_front_image
        image_holder[CARD_BACK_IMAGE] = card_back_image
        image_holder[RIGHT_IMAGE] = right_image
        image_holder[WRONG_IMAGE] = wrong_image

        self.canvas_image = self.canvas.create_image(400, 218, image=image_holder[CARD_FRONT_IMAGE])
        self.title_text = self.canvas.create_text(400, 150, fill="black", font=(FONT_NAME, 40, "italic"))
        self.word_text = self.canvas.create_text(400, 263, fill="black", font=(FONT_NAME, 40, "bold"))
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.search_button = Button(image=image_holder[WRONG_IMAGE], width=100, highlightbackground=BACKGROUND_COLOR,
                                    command=self.wrong_button_clicked)
        self.search_button.grid(row=1, column=0)

        self.search_button = Button(image=image_holder[RIGHT_IMAGE], width=100, highlightbackground=BACKGROUND_COLOR,
                                    command=self.right_button_clicked)
        self.search_button.grid(row=1, column=1)

        self.french_english_dict = {}
        self.read_words()

        self.current_card = {}
        self.select_card()

        self.timer = self.window.after(ms=3000, func=self.flip_cards)

        self.window.mainloop()

    def read_words(self):
        try:
            data_frame = pandas.read_csv("./data/words_to_learn.csv")
        except FileNotFoundError:
            data_frame = pandas.read_csv("./data/french_words.csv")
            self.french_english_dict = data_frame.to_dict(orient="records")
        else:
            self.french_english_dict = data_frame.to_dict(orient="records")

    def select_card(self):
        self.current_card = choice(self.french_english_dict)
        self.canvas.itemconfig(self.canvas_image, image=image_holder[CARD_FRONT_IMAGE])
        self.canvas.itemconfig(self.title_text, text="French", fill="black")
        self.canvas.itemconfig(self.word_text, text=self.current_card["French"], fill="black")

    def flip_cards(self):
        self.canvas.itemconfig(self.canvas_image, image=image_holder[CARD_BACK_IMAGE])
        self.canvas.itemconfig(self.title_text, text="English", fill="white")
        self.canvas.itemconfig(self.word_text, text=self.current_card["English"], fill="white")

    def next_card(self):
        self.window.after_cancel(self.timer)
        self.select_card()
        self.timer = self.window.after(ms=3000, func=self.flip_cards)

    def right_button_clicked(self):
        # Remove the word from the dictionary
        self.french_english_dict.remove(self.current_card)

        # Update words_to_learn.csv file
        new_data_frame = pandas.DataFrame(self.french_english_dict)

        # If you don't want to create an index for the new csv, you can set the index parameter to False
        new_data_frame.to_csv("./data/words_to_learn.csv", index=False)

        self.next_card()

    def wrong_button_clicked(self):
        self.next_card()
