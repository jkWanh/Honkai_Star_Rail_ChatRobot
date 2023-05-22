import unittest
from  stringsplit import *
class TestFunctions(unittest.TestCase):

    def test_split(self):
        s = "<Record c=<Node element_id='4:bfe4a058-1be6-45ce-a716-0a2159896c52:685' labels=frozenset({'Character'}) properties={'destiny': '毁灭', 'occupation': '雅利洛-VI', 'faction': '/', 'name': '克拉拉', 'icon': 'https://uploadstatic.mihoyo.com/sr-wiki/2023/03/09/187636729/6b0b412b079a5610d34c2d87a9faf665_5273843714696308389.png', 'id': 414, 'quality': '五星', 'element': '物理'}>>"
        label_value, matches = split(s)
        self.assertEqual(label_value, 'Character')
        self.assertIsInstance(matches, list)
        self.assertGreater(len(matches), 0)


if __name__ == '__main__':
    unittest.main()