from tkinter import *
from quiz_brain import QuizBrain

image_holder = []

BACKGROUND_COLOR = "#375362"
CANVAS_BACK_GROUND = "white"
FONT_NAME = "Arial"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

        self.score_label = Label(text="Score:", font=(FONT_NAME, 15, "normal"), fg="white", bg=BACKGROUND_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=300, height=250, bg=CANVAS_BACK_GROUND, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, fill=BACKGROUND_COLOR, width=280,
                                                     font=(FONT_NAME, 20, "italic"),
                                                     text="Some Question Text")
        self.canvas.grid(row=1, column=0, columnspan=2)

        global image_holder
        false_image = PhotoImage(file="./images/false.png")
        true_image = PhotoImage(file="./images/true.png")
        image_holder.append(false_image)
        image_holder.append(true_image)

        self.true_button = Button(image=true_image, width=100, height=97, highlightbackground=BACKGROUND_COLOR,
                                  command=self.true_button_clicked)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_image, width=100, height=97, highlightbackground=BACKGROUND_COLOR,
                                   command=self.false_button_clicked)
        self.false_button.grid(row=2, column=1)

        self.timer = None
        self.quiz_completed = False
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_text)
            self.canvas.config(bg=CANVAS_BACK_GROUND)
            self.score_label.config(text=f"score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz.\nYour final score was: "
                                                            f"{self.quiz.score}/{self.quiz.question_number}")
            self.canvas.config(bg=CANVAS_BACK_GROUND)
            self.quiz_completed = True

    def true_button_clicked(self):
        if not self.quiz_completed:
            self.give_feedback(self.quiz.check_answer("True"))

    def false_button_clicked(self):
        if not self.quiz_completed:
            self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        if self.timer is not None:
            self.window.after_cancel(self.timer)

        self.timer = self.window.after(ms=1000, func=self.get_next_question)
