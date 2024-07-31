from question_model import Question
from data import make_data
from quiz_brain import QuizBrain
from quiz_ui import QuizUI

question_data = make_data()

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)
