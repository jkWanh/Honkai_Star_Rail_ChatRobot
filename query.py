import jieba
import jieba.posseg as pseg
import json
from neo4j import GraphDatabase
import re
#分词函数
def clause(text):
    jieba.load_userdict("txt/user1.txt")
    words = pseg.cut(text)  # jieba默认模式
    result = []
    for word, flag in words:
        result.append({'word': word, 'flag': flag})

    with open('txt/result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False,indent=4)
#单节点查询函数
def chaxunname(attribute,name):
    # 连接到Neo4j数据库
    uri = "neo4j+s://1d778504.databases.neo4j.io"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "FN7ZTm3pYbBPQU44creN-H5P8_LvzAlIa284CpkwdIM"))
    #查询节点属性
    query ='MATCH (c:'+attribute+' {name: $name}) RETURN  c' #'MATCH (c:Relics {name: $name}) RETURN  c'
    record_str = ''
    with driver.session() as session:
        result = session.run(query, name=name)
        #遍历结果
        for record in result:
            record_str += str(record)
            print(record)
        return record_str
#调用单节点查询
def  name(text):
    clause(text)
    # 读取 JSON 文件
    with open('txt/result.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
   # 提取 "flag" 和 "word" 字段的值
    for item in data:
        flag = item['flag']
        word = item['word']
        if flag == 'character' or flag == 'material' or flag == 'monster'or flag == 'occupation'or flag == 'store'or flag == 'soul'or flag == 'relics':
            print(f"Flag: {flag}, Word: {word}")
            return chaxunname(flag.capitalize(), word)
        elif flag == 'lightcones':
            flag = 'Light_cones'
            print(f"Flag: {flag}, Word: {word}")
            return chaxunname(flag, word)


#路径查询
def chaxunis_true(first_letter1,first_letter2,flag1,flag2,word1,word2,n):
    # 连接到Neo4j数据库
    uri = "neo4j+s://1d778504.databases.neo4j.io"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "FN7ZTm3pYbBPQU44creN-H5P8_LvzAlIa284CpkwdIM"))
    # 查询节点属性
    query = 'MATCH path = ('+first_letter1+':'+flag1+' {name: "'+word1+'"})-[*1..'+str(n)+']-('+first_letter2+':'+flag2+') RETURN path'
    print(query)
    ans_list = []
    with driver.session() as session:
        result = session.run(query)
        # 遍历结果
        for record in result:
            xml_string = str(record)
            print(record)
            half = len(xml_string) // 2

            xml_string =xml_string[half:]
            # 正则表达式匹配
            pattern = r"name': '(\w+).*icon': '([^']+)"
            # 发现所有的匹配
            matches = re.findall(pattern, xml_string)
            # 把数据转换成list
            name_icon_list = [(match[0], match[1]) for match in matches]
            ans_list.append(name_icon_list)
        ans_list = [[name, icon] for sublist in ans_list for name, icon in sublist]
        return ans_list
#调用路径查询
def is_true(text):
    clause(text)
    # 读取 JSON 文件
    with open('txt/result.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
   # 提取 "flag" 和 "word" 字段的值
    first_letter_array = []
    flag_array = []  # 创建空列表
    word_array = []  # 创建空列表
    for item in data:
        flag = item['flag']
        word = item['word']
        if flag == 'character' or flag == 'material' or flag == 'occupation'or flag == 'store'or flag == 'relics':
            print(f"Flag: {flag}, Word: {word}")
            first_letter = flag[0]
            first_letter_array.append(first_letter)
            flag_array.append(flag.capitalize())
            word_array.append(word)
        elif flag == 'monster':
            print(f"Flag: {flag}, Word: {word}")
            first_letter = 'a'
            first_letter_array.append(first_letter)
            flag_array.append(flag.capitalize())
            word_array.append(word)
        elif flag == 'soul':
            print(f"Flag: {flag}, Word: {word}")
            first_letter = 'b'
            first_letter_array.append(first_letter)
            flag_array.append(flag.capitalize())
            word_array.append(word)
        elif flag == 'lightcones':
            first_letter = flag[0]
            flag = 'Light_cones'
            print(f"Flag: {flag}, Word: {word}")
            first_letter_array.append(first_letter)
            flag_array.append(flag.capitalize())
            word_array.append(word)
    for item in data:
         flag = item['flag']
         word = item['word']
         if word == "材料":
            first_letter_array.append('ac')
            flag_array.append('Material')
            word_array.append(word)
         elif word == "角色":
            first_letter_array.append('ad')
            flag_array.append('Character')
            word_array.append(word)
         elif word == "遗物":
            first_letter_array.append('ae')
            flag_array.append('Relics')
            word_array.append(word)
         elif word == "商店":
            first_letter_array.append('af')
            flag_array.append('Store')
            word_array.append(word)
    n = 2
    if  len(word_array) != 2 :
        return 6
    return chaxunis_true(first_letter_array[0],first_letter_array[1],flag_array[0],flag_array[1],word_array[0],word_array[1],n)






