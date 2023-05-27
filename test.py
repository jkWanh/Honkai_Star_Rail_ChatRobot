import unittest
from diversion import *
from query import *
from stringsplit import *
from neo4j import GraphDatabase

uri = "neo4j+s://1d778504.databases.neo4j.io"
auth = ("neo4j", "FN7ZTm3pYbBPQU44creN-H5P8_LvzAlIa284CpkwdIM")
class TestFunctions(unittest.TestCase):
    #diversion.py的测试
    #测试 if-else的name分支
    def test_diversion_name(self):
        text = "介绍一下史瓦罗图片图像"
        flag,result = diversion(text)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    # 测试 if-else的is_true分支
    def test_diversion_is_true(self):
        text = "克拉拉升级需要什么材料"
        flag,result = diversion(text)
        self.assertIsNotNone(result)
    #测试query函数
    #测试clause函数
    def test_clause(self):
        text = "请介绍一下三月七"
        clause(text)
        with open('txt/result.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(data)
        self.assertIsNotNone(data)
    # 测试chaxunname函数
    def test_chaxunname(self):
        result = chaxunname('Character', '三月七')
        self.assertIsNotNone(result)

    # 测试name函数
    def test_name(self):
        text = "请介绍一下三月七"
        result = name(text)
        self.assertIsNotNone(result)

    # 测试is_true函数
    def test_is_true(self):
        text = "户籍在星穹列车的角色有哪些"
        result = is_true(text)
        print(result)
        self.assertIsNotNone(result)

    # 测试chaxunis_true函数
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

    # 测试string_split.py的split函数
    def test_split(self):
        s = "<Record c=<Node element_id='4:bfe4a058-1be6-45ce-a716-0a2159896c52:685' labels=frozenset({'Character'}) properties={'destiny': '毁灭', 'occupation': '雅利洛-VI', 'faction': '/', 'name': '克拉拉', 'icon': 'https://uploadstatic.mihoyo.com/sr-wiki/2023/03/09/187636729/6b0b412b079a5610d34c2d87a9faf665_5273843714696308389.png', 'id': 414, 'quality': '五星', 'element': '物理'}>>"
        label_value, matches = split(s)
        self.assertEqual(label_value, 'Character')
        self.assertIsInstance(matches, list)
        self.assertGreater(len(matches), 0)

    def test_neo4j_connection(self):
        # 建立数据库连接
        driver = GraphDatabase.driver(uri, auth=auth)
        session = driver.session()
        query = "MATCH path = (o:Occupation {name: '星穹列车'})-[*1..2]-(ad:Character) RETURN DISTINCT path"
        # 执行查询
        result = session.run(query)

        self.assertIsNotNone(result)
        # 关闭数据库连接
        session.close()
        driver.close()

if __name__ == '__main__':
    unittest.main()