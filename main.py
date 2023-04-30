import json
from game import Game


if __name__ == '__main__':
    try:
        with open('questions.json', encoding='utf-8') as file:
            data = json.load(file)

        game = Game()
        game.load_questions(data)
        game.run()

    except FileNotFoundError:
        print('No such file or directory, please create or download "questions.json" file.'
              '\nMore details at README file')
