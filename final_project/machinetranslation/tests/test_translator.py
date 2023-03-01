import unittest
from machinetranslation.translator import english_to_french, french_to_english


class TranslatorTest(unittest.TestCase):
    def test_frenchToEnglish_assertEqual(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test_frenchToEnglish_assertNotEqual(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

    def test_englishToFrench_assertEqual(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_englishToFrench_assertNotEqual(self):
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
    
unittest.main(verbosity=2)
