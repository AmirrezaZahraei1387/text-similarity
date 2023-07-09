import unittest
import synreco

class test(unittest.TestCase):

    def test_tokenize_test_case_1(self):
        """in this case we give a sentence with
        a name including _"""
        sent = "hello = good"
        print(synreco.tokenizer.tokenize(sent))

