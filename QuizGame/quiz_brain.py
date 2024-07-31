class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        ques = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {ques.text} (True/False)?: ")
        if user_answer.lower() == ques.answer.lower():
            print("Right Answer!")
            self.score += 1
        else:
            print("Wrong Answer!")

        print(f"The correct answer was: {ques.answer}")
        print(f"Your current score is: {self.score}/{self.question_number + 1}\n")

        self.question_number += 1

    def still_has_question(self) -> bool:
        return self.question_number < len(self.question_list)

    def finalize_result(self):
        print("You've completed the quiz.")
        print(f"Your final score was: {self.score}/{self.question_number + 1}")
