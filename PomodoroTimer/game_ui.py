import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
COUNT_DOWN_FROM_MIN = 5
WORK_MIN = 4

image_holder = []


class GameUI:
    def __init__(self):
        self.reps = 0
        self.timer = None

        self.window = Tk()
        self.window.title("Pomodoro")
        self.window.resizable(False, False)
        self.window.config(padx=100, pady=50, bg=YELLOW)

        self.timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
        self.timer_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=200, height=224, bg=YELLOW, highlightthickness=0)

        global image_holder
        tomato_image = PhotoImage(file="tomato.png")
        image_holder.append(tomato_image)

        self.canvas.create_image(100, 112, image=tomato_image)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(row=1, column=1)

        self.start_button = Button(text="Start", highlightbackground=YELLOW, command=self.start_button_clicked)
        self.start_button.grid(row=2, column=0)

        self.reset_button = Button(text="Reset", highlightbackground=YELLOW, command=self.rest_button_clicked)
        self.reset_button.grid(row=2, column=2)

        self.tick_label = Label(text="", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
        self.tick_label.grid(row=3, column=1)

        self.window.mainloop()

    def start_timer(self):
        self.reps += 1

        if self.reps % 8 == 0:
            self.update_timer_label(text="Break", color=RED)
            self.count_down(LONG_BREAK_MIN * 60)
            self.reps = 0
        elif self.reps % 2 == 0:
            self.update_timer_label(text="Break", color=PINK)
            self.count_down(SHORT_BREAK_MIN * 60)
        else:
            self.update_timer_label(text="Work", color=GREEN)
            self.count_down(WORK_MIN * 60)

    def count_down(self, count):
        self.update_timer(count)
        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()
            if self.reps % 4 == 0 or self.reps % 8 == 0:
                ticks = self.tick_label["text"]
                ticks = "✔" * (len(ticks) + 1)
                self.tick_label.config(text=ticks)

    def update_timer_label(self, color, text):
        self.timer_label.config(text=text, fg=color)

    def update_timer(self, second):
        min_section = math.floor(second / 60)
        sec_section = second % 60

        min_str = f"{min_section}"
        sec_str = f"{sec_section}"

        new_time = f"{min_str.zfill(2)}:{sec_str.zfill(2)}"

        self.canvas.itemconfig(self.timer_text, text=new_time)

    def start_button_clicked(self):
        self.tick_label.config(text="")
        self.start_timer()
        pass

    def rest_button_clicked(self):
        self.window.after_cancel(self.timer)
        self.tick_label.config(text="")
        self.update_timer(0)
        self.update_timer_label(GREEN, "Timer")
        self.reps = 0

