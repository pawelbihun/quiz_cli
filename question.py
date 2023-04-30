class Question:
    answers_letters_list = ['a', 'b', 'c', 'd']
    player_answer = ''

    def __init__(self,
                 question: str,
                 answers: list,
                 right_answer: str):
        self.question = question
        self.answers = answers
        self.right_answer = right_answer

    def show_with_answers(self, number_of_question) -> None:
        print('\n', number_of_question, self.question)
        answers = (tuple(zip(self.answers_letters_list, self.answers)))
        for letter, answer in answers:
            print(f'{letter}: {answer}')

    def show_with_player_answer(self):
        print('\n', self.question)
        answers = (tuple(zip(self.answers_letters_list, self.answers)))
        for letter, answer in answers:
            print(f'{letter}: {answer}')
        print(f'Right answer: {self.right_answer}\t\tYour answer: {self.player_answer}')

    def add_player_answer_to_question(self, player_answer: str) -> None:
        self.player_answer = player_answer
