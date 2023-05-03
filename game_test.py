from game import Game
import pytest

class TestGame:

    @pytest.fixture
    def game(self) -> Game:
        return Game()

    @pytest.fixture
    def right_answer_a(self) -> str:
        return 'a'

    def test_game_init(self, game):
        assert isinstance(game, Game)
        assert game.questions_list == []
        assert game.score == 0
        assert game.player_name == 'Nameless player'
        assert game.wrong_answers_list == []
        assert game.count_questions == 0
        assert game.quizzes == []

    def test_is_score_granted_with_correct_lowercase_answer(self, game, right_answer_a):
        answer = 'a'
        assert game.is_score_granted(answer, right_answer_a)

    def test_is_score_granted_with_correct_uppercase_answer(self, game, right_answer_a):
        answer = 'A'
        assert game.is_score_granted(answer, right_answer_a)

    def test_is_score_granted_with_wrong_lowercase_answer(self, game, right_answer_a):
        answer = 'b'
        assert not game.is_score_granted(answer, right_answer_a)

    def test_is_score_granted_with_wrong_uppercase_answer(self, game, right_answer_a):
        answer = 'B'
        assert not game.is_score_granted(answer, right_answer_a)

    def test_are_questions_loaded(self, game):
        game.questions_list.append('some_question')
        assert game.are_questions_loaded()

    def test_are_not_questions_loaded(self, game):
        assert not game.are_questions_loaded()

    def test_count_questions_list(self, game):
        game.questions_list.append('some_question')
        game.count_questions_list()
        assert game.count_questions == 1
