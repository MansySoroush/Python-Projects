from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


def fill_question_bank():
    for q in question_data:
        question_bank.append(Question(q["text"], q["answer"]))


fill_question_bank()
quiz_brain = QuizBrain(q_list=question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

quiz_brain.finalize_result()
