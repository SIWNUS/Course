class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        self.user_answer = input(f"Q.{self.question_no + 1}: {self.question_list[self.question_no].text} (true/false): ").title()
        self.check_answer()
        self.question_no += 1
        print("\n\n")

    def check_answer(self):
        if self.user_answer == self.question_list[self.question_no].answer:
            self.score += 1
            print("You got it right!")
        else:
            print(f"You got it wrong! The correct answer is '{self.question_list[self.question_no].answer}'")

        print(f"Your current score is: {self.score}/{self.question_no + 1}")