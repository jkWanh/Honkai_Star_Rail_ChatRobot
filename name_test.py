import unittest
from using_name import *
class TestFunctions(unittest.TestCase):

    def test_clause(self):
        text = "这是一段测试文本"
        clause(text)
        with open('result.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.assertIsNotNone(data)

    def test_chaxun(self):
        result = chaxun('Character', '早柚')
        self.assertIsNotNone(result)

    def test_name(self):
        text = "三月七是谁？"
        result = name(text)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()