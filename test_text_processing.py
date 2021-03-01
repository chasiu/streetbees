import unittest
import text_processing as tp


class TestTextProcessing(unittest.TestCase):
    def test_tokenise(self):
        s = "This is a test string!"
        self.assertEqual(tp.tokenise(s), ["This", "is", "a", "test", "string!"])

    def test_stopwords(self):
        s = "This is a test string!"
        stop = ["this", "is", "a"]
        self.assertEqual(tp.drop_stop(s, stop), "test string!")

        self.assertEqual(tp.drop_stop(s, stop, ignore_case=False), "This test string!")

    def test_drop_chars(self):
        s = "This is & a test@string!"

        self.assertEqual(tp.drop_chars(s), "This is  a teststring")

    def test_drop_whitespace(self):
        s = "This    is \n a test \n\n\t string"

        self.assertEqual(tp.drop_whitespace(s), "This is a test string")


if __name__ == "__main__":
    unittest.main()