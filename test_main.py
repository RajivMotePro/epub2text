from unittest import TestCase
from HtmlStripper import MLStripper


class TestMain(TestCase):
    def test_main(self):
        content = "<html><head><title>A Title</title></head><body><p />This is some text.</body></html>"
        s = MLStripper()
        s.feed(content)
        result = s.get_data()
        self.assertEqual(result, "A TitleThis is some text.")

