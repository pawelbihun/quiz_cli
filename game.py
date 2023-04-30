import random

from question import Question


class Game:
    def __init__(self):
        self.questions_list: list = []
        self.score: int = 0
        self.player_name: str = 'Nameless player'

    def are_questions_loaded(self) -> bool:
        if len(self.questions_list) > 0:
            return True
        return False

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
            random.shuffle(self.questions_list)
            for count, question in enumerate(self.questions_list, start=1):
                question.show_with_answers(count)
                answer = input('Your answer: ')
                if self.is_score_granted(answer, question.right_answer):
                    self.score += 1

            print('QUIZ END\n')
            self.player_name = input('Type your name: ')
            print(f'\n{self.player_name} you scored {self.score} out of {len(self.questions_list)}')
            if self.score > 0:
                print('Congratulation!\n\n')
            else:
                print('Sorry, you didn\'t score any points. :(')

        else:
            print('no data loaded')
