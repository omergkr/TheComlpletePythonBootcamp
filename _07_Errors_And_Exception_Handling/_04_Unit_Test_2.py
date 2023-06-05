import unittest
from _03_Unit_Test import cap_text, cap_all__word_text


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = "python"
        result = cap_text(text)
        self.assertEqual(result, "Python")

    def test_multiple_words(self):
        text = "monty python"
        result = cap_text(text)
        self.assertEqual(result, "Monty Python")

    def test_multiple_words_with_title(self):
        text = "monty python"
        result = cap_all__word_text(text)
        self.assertEqual(result, "Monty Python")