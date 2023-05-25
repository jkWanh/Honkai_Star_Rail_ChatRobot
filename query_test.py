import unittest
from query import *
class TestFunctions(unittest.TestCase):

    def test_clause(self):
        text = "掉落出升级雅利洛-VI"
        clause(text)
        with open('result.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(data)
        self.assertIsNotNone(data)

    def test_chaxunname(self):
        result = chaxunname('Character', '三月七')
        self.assertIsNotNone(result)

    def test_name(self):
        text = "三月七是谁？"
        result = name(text)
        self.assertIsNotNone(result)



    def test_is_true(self):
        text = "户籍在星穹列车的角色有哪些"
        result = is_true(text)
        self.assertIsNotNone(result)

    def test_chaxunis_true(self):
        first_letter1 = "c"
        first_letter2 = "M"
        flag1 = "Character"
        flag2 = "Monster"
        word1 = "克拉拉"
        word2 = "史瓦罗"
        n = 2
        result = chaxunis_true(first_letter1, first_letter2, flag1, flag2, word1, word2, n)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()