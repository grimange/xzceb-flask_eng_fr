# Author: RA
# Purpose: Test Case
# Created: 28/02/2023

import unittest
from .translator import english_to_french, french_to_english


class TranslatorTest(unittest.TestCase):
    def test_null_input_for_frenchToEnglish(self):
        self.assertIsNone(french_to_english(), None)

    def test_null_input_for_englishToFrench(self):
        self.assertIsNone(english_to_french(), None)

    def test_frenchToEnglish_translation(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_englishToFrench_translation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


unittest.main()
