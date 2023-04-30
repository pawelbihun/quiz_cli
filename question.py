class Question:
    answers_letters_list = ['a', 'b', 'c', 'd']

    def __init__(self,
                 question: str,
                 answers: list,
                 right_answer: str):
        self.question = question
        self.answers = answers
        self.right_answer = right_answer

    def show_with_answers(self, number_of_question):
        print('\n', number_of_question, self.question)
        answers = (tuple(zip(self.answers_letters_list, self.answers)))
        for letter, answer in answers:
            print(f'{letter}: {answer}')
