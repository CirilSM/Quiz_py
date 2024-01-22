import unittest
from unittest.mock import patch
from io import StringIO
from QUIZ_main import run_quiz, quiz_data

class TestQuiz(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '2', '3', '4'])
    def test_run_quiz_cyber_security_correct_answers(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            run_quiz("Cyber Security")

        expected_output = "Your Cyber Security Quiz Score:"
        self.assertIn(expected_output, mock_stdout.getvalue())
        self.assertIn("Correct!", mock_stdout.getvalue())
        self.assertNotIn("Wrong!", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['4', '3', '2', '1'])
    def test_run_quiz_mathematics_incorrect_answers(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            run_quiz("Mathematics")

        expected_output = "Your Mathematics Quiz Score:"
        self.assertIn(expected_output, mock_stdout.getvalue())
        self.assertIn("Wrong!", mock_stdout.getvalue())
        self.assertNotIn("Correct!", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
