import unittest
from diversion import *
class TestFunctions(unittest.TestCase):

    def test_diversion_name(self):
        text = "介绍一下史瓦罗图片图像"
        flag,result = diversion(text)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
    def test_diversion_is_true(self):
        text = "克拉拉和史瓦罗先生有没有联系？"
        flag,result = diversion(text)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()