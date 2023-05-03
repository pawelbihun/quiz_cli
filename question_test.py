from question import Question
import pytest


class TestQuestion:

    @pytest.fixture
    def question(self) -> Question:
        tst_dict: dict = {'question': 'Test question',
                          'answers': ['aaa', 'bbb', 'ccc', 'ddd'],
                          'right_answer': 'b'}
        question = Question(tst_dict['question'], tst_dict['answers'], tst_dict['right_answer'])
        return question

    def test_question_init(self, question):
        assert isinstance(question, Question)

    def test_question_has_answers_letters(self, question):
        assert question.answers_letters_list == ['a', 'b', 'c', 'd']

    def test_question_has_empty_player_answer(self, question):
        assert question.player_answer == ''

    def test_add_player_answer_to_question(self, question):
        question.add_player_answer_to_question('a')
        assert question.player_answer == 'a'
