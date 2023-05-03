"""This script contains Question class"""


class Question:
    """The class contains fields with the content of the question, possible answers,
    the correct and chosen by the player answer"""
    answers_letters_list: list = ['a', 'b', 'c', 'd']
    player_answer: str = ''

    def __init__(self,
                 question: str,
                 answers: list,
                 right_answer: str):
        self.question: str = question
        self.answers: list = answers
        self.right_answer: str = right_answer

    def show_with_answers(self, number_of_question: int) -> None:
        print('\n', number_of_question, self.question)
        answers = (tuple(zip(self.answers_letters_list, self.answers)))
        for letter, answer in answers:
            print(f'{letter}: {answer}')

    def show_with_player_answer(self):
        print('\n', self.question)
        answers = (tuple(zip(self.answers_letters_list, self.answers)))
        for letter, answer in answers:
            print(f'{letter}: {answer}')
        print(f'Right answer: {self.right_answer}\t\tYour answer: {self.player_answer}\n')

    def add_player_answer_to_question(self, player_answer: str) -> None:
        self.player_answer = player_answer
