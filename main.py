"""This is main script of quiz.
It tries open a json-format file with a questions and starts a game"""

from game import Game


if __name__ == '__main__':
    try:
        while True:
            game = Game()
            game.clear_console()
            game.search_available_quizzes()
            game.show_available_quizzes()
            game.load_questions(game.open_quiz_number(game.select_a_quiz()))
            game.clear_console()
            game.run()

    except KeyboardInterrupt:
        print('\n\nDetected CTRL+C... Quiz over')
