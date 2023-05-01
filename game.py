import os
import random

from question import Question


class Game:
    def __init__(self):
        self.questions_list: list = []
        self.score: int = 0
        self.player_name: str = 'Nameless player'
        self.wrong_answers_list: list = []
        self.count_questions: int = 0

    def are_questions_loaded(self) -> bool:
        if len(self.questions_list) > 0:
            return True
        return False

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def count_questions_list(self) -> None:
        self.count_questions = len(self.questions_list)

    def load_questions(self, data: list):
        for obj in data:
            question = Question(obj['question'], obj['answers'], obj['right_answer'])
            self.questions_list.append(question)

    @staticmethod
    def is_score_granted(answer, right_answer) -> bool:
        if answer.lower() == right_answer.lower():
            return True
        return False

    def run(self):
        if self.are_questions_loaded():
            print('\n>>>QUIZ START<<<')
            self.player_name = input('Type your name: ')
            random.shuffle(self.questions_list)
            self.count_questions_list()
            for count, question in enumerate(self.questions_list, start=1):
                self.clear_console()
                question.show_with_answers(count)
                answer = input('Your answer: ')
                if self.is_score_granted(answer, question.right_answer):
                    self.score += 1
                else:
                    question.add_player_answer_to_question(answer)
                    self.wrong_answers_list.append(question)
            self.clear_console()

            print('QUIZ END\n')
            print(f'\n{self.player_name} you scored {self.score} out of {self.count_questions}')
            if self.score == self.count_questions:
                print('Congratulation! You answered all the questions correctly. Well done!\n\n')
            elif self.count_questions > self.score > 0:
                print(f'{self.player_name} you made some mistakes, here they are:')
                for question in self.wrong_answers_list:
                    question.show_with_player_answer()
            elif self.score == 0:
                print('You are loser, did not earn any points :(\n'
                      'There are right answers:')
                for question in self.wrong_answers_list:
                    question.show_with_player_answer()

        else:
            print('no data loaded')
