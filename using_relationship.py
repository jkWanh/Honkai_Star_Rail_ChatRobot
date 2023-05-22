import jieba
import jieba.posseg as pseg
import json
from neo4j import GraphDatabase
import re
def clause(text):
    jieba.load_userdict("txt/user1.txt")
    words = pseg.cut(text)  # jieba默认模式
    result = []
    for word, flag in words:
        result.append({'word': word, 'flag': flag})

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False,indent=4)

def chaxun(first_letter,attribute,name):
    # 连接到Neo4j数据库
    uri = "neo4j+s://1d778504.databases.neo4j.io"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "FN7ZTm3pYbBPQU44creN-H5P8_LvzAlIa284CpkwdIM"))
    # 查询节点属性
    query = 'MATCH path = ('+first_letter+':'+attribute+' {name: $name})-[*1..3]-(c:Character) RETURN DISTINCT c'
    ans_list = []
    with driver.session() as session:
        result = session.run(query, name=name)
        # 遍历结果
        for record in result:
            xml_string = str(record)

            # Define a regular expression to match the 'name' and 'icon' attributes
            pattern = r"name': '(\w+).*icon': '([^']+)"

            # Find all matches in the XML string
            matches = re.findall(pattern, xml_string)

            # Create a list of tuples containing the name and icon for each match
            name_icon_list = [(match[0], match[1]) for match in matches]
            ans_list.append(name_icon_list)

        ans_list = [[name, icon] for sublist in ans_list for name, icon in sublist]

        return(ans_list)
def relationship(text):
    clause(text)
    # 读取 JSON 文件
    with open('result.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
   # 提取 "flag" 和 "word" 字段的值
    for item in data:
        flag = item['flag']
        word = item['word']
        if flag == 'character' or flag == 'material' or flag == 'monster'or flag == 'occupation'or flag == 'store'or flag == 'soul'or flag == 'relics':
            print(f"Flag: {flag}, Word: {word}")
            first_letter = flag[0]
            return chaxun(first_letter,flag.capitalize(),word)
        elif flag == 'lightcones':
            first_letter = flag[0]
            flag = 'Light_cones'
            print(f"Flag: {flag}, Word: {word}")
            return chaxun(first_letter,flag,word)





