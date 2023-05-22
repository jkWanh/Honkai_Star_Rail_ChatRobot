import unittest
from query import *
import os
class TestFunctions(unittest.TestCase):

    def test_clause(self):
        text = "这是一段测试文本"
        clause(text)
        print(os.getcwd())
        with open('result.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.assertIsNotNone(data)

    def test_chaxunname(self):
        result = chaxunname('Character', '早柚')
        self.assertIsNotNone(result)

    def test_name(self):
        text = "三月七是谁？"
        result = name(text)
        self.assertIsNotNone(result)

    def test_chaxunrealtionship(self):
        result = chaxunrelationship('C', 'Character', '克拉拉')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_relationship(self):
        text = "篡改的野心是谁的天赋升级材料？"
        result = relationship(text)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_is_true(self):
        text = "克拉拉和史瓦罗先生有没有联系？"
        result = is_true(text)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, bool)

    def test_chaxunis_true(self):
        first_letter1 = "c"
        first_letter2 = "M"
        flag1 = "Character"
        flag2 = "Monster"
        word1 = "克拉拉"
        word2 = "史瓦罗"
        n = 2
        result = chaxunis_true(first_letter1, first_letter2, flag1, flag2, word1, word2, n)
        assert result is not None
        assert isinstance(result, str)

if __name__ == '__main__':
    unittest.main()