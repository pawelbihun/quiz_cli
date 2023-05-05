"""This script contains Game class"""
import json
import os
import random
from question import Question


class Game:
    """The class contains fields and methods to handle the quiz"""

    def __init__(self):
        self.questions_list: list = []
        self.score: int = 0
        self.player_name: str = 'Nameless player'
        self.wrong_answers_list: list = []
        self.count_questions: int = 0
        self.quizzes: list = []

    def are_questions_loaded(self) -> bool:
        if len(self.questions_list) > 0:
            return True
        return False

    @staticmethod
    def clear_console() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def count_questions_list(self) -> None:
        self.count_questions = len(self.questions_list)

    @staticmethod
    def is_score_granted(answer: str, right_answer: str) -> bool:
        if answer.lower() == right_answer.lower():
            return True
        return False

    def open_quiz_number(self, number: int):
        with open(f'data/{self.quizzes[number]}', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def load_questions(self, data: list) -> None:
        for obj in data:
            question = Question(obj['question'], obj['answers'], obj['right_answer'])
            self.questions_list.append(question)

    def run(self) -> None:
        if self.are_questions_loaded():
            print('\n >>>QUIZ START<<<\n Press CTRL+C to quit\n')
            self.player_name = input(' Type your name: ')
            random.shuffle(self.questions_list)
            self.count_questions_list()
            for count, question in enumerate(self.questions_list, start=1):
                self.clear_console()
                question.show_with_answers(count)
                answer = input('\n\n Your answer: ')
                if self.is_score_granted(answer, question.right_answer):
                    self.score += 1
                else:
                    question.add_player_answer_to_question(answer)
                    self.wrong_answers_list.append(question)
            self.clear_console()

            print(' QUIZ END\n')
            print(f' \n{self.player_name} you scored {self.score} out of {self.count_questions}')
            if self.score == self.count_questions:
                print('Congratulation! You answered all the questions correctly. Well done!\n\n')
            elif self.count_questions > self.score > 0:
                print(f'{self.player_name} you made some mistakes, here they are:')
                for question in self.wrong_answers_list:
                    question.show_with_player_answer()
            elif self.score == 0:
                print(' You are loser, did not earn any points :(\n'
                      ' There are right answers:')
                for question in self.wrong_answers_list:
                    question.show_with_player_answer()
            print(' Press any key to continue...')
            input('')

        else:
            print('no data loaded')

    def search_available_quizzes(self) -> None:
        """Need to be opened in main folder of the game
        and have the data catalog with correct for game json files"""
        try:
            for item in os.listdir(os.getcwd() + r'\data'):
                if item.endswith('.json'):
                    self.quizzes.append(item)
        except FileNotFoundError:
            print(' No such file or directory, please create or download "test_questions.json" file.'
                  '\n More details at README file')

    def select_a_quiz(self) -> int:
        while True:
            try:
                choice = int(input(''))
                if 0 <= choice <= len(self.quizzes):
                    return choice - 1
                else:
                    raise IndexError
            except IndexError:
                print('Choice out of allowed range')
            except Exception:
                print('This is no integer number, try again')

    def show_available_quizzes(self) -> None:
        if len(self.quizzes) > 0:
            print('>>>Choose a quiz by typing its number<<<\n')
            for i, quiz in enumerate(self.quizzes, start=1):
                print(f'{i}. {quiz[0:-5]}')
        else:
            print('Sorry, no quizzes are available')
