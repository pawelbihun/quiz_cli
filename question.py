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
        # print(f'Nr {number_of_question}:\n\t\t\t?????\n{self.question}\n\t\t\t?????\n\n')
        print(f' Question nr {number_of_question}')
        self.print_question(self.question, self.do_tabs())
        answers = (tuple(zip(self.answers_letters_list, self.answers)))
        print(' Answers:\n')
        for letter, answer in answers:
            print(f' {letter}: {answer}\n')

    def show_with_player_answer(self):
        print(f'\n{self.question}\n')
        answers = (tuple(zip(self.answers_letters_list, self.answers)))
        for letter, answer in answers:
            print(f' {letter}: {answer}')
        print(f' Right answer: {self.right_answer}\t\tYour answer: {self.player_answer}\n')

    def add_player_answer_to_question(self, player_answer: str) -> None:
        self.player_answer = player_answer

    @staticmethod
    def print_question(quest, tabs) -> None:
        print(f'\n{tabs}\n\n {quest}\n\n{tabs}\n\n')

    @staticmethod
    def do_tabs() -> str:
        return 5 * '?\t\t'
