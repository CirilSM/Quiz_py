import unittest
from unittest.mock import patch
from io import StringIO
from QUIZ_main import run_quiz, quiz_data

class TestQuiz(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '2', '3', '4'])
    def test_run_quiz_correct_answers(self, mock_input):
        topics = list(quiz_data.keys())
        for topic in topics:
            with self.subTest(topic=topic):
                with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                    run_quiz(topic)

                # Replace the following assertions with the correct expected output
                expected_output = f"Your {topic} Quiz Score: "
                self.assertIn(expected_output, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['5', '6', '7', '8'])
    def test_run_quiz_incorrect_answers(self, mock_input):
        topics = list(quiz_data.keys())
        for topic in topics:
            with self.subTest(topic=topic):
                with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                    run_quiz(topic)

                # Replace the following assertions with the correct expected output
                expected_output = f"Your {topic} Quiz Score: "
                self.assertIn(expected_output, mock_stdout.getvalue())
                
    def test_run_quiz_invalid_topic(self):
        with patch('builtins.input', return_value='0'):
            with self.assertRaises(SystemExit):
                run_quiz("Invalid Topic")

if __name__ == '__main__':
    unittest.main()
