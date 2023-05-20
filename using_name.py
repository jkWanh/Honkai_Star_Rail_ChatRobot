import jieba
import jieba.posseg as pseg
import json
from neo4j import GraphDatabase

def clause(text):
    jieba.load_userdict("user1.txt")
    words = pseg.cut(text)  # jieba默认模式
    result = []
    for word, flag in words:
        result.append({'word': word, 'flag': flag})

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False,indent=4)

def chaxun(attribute,name):
    # 连接到Neo4j数据库
    uri = "neo4j+s://1d778504.databases.neo4j.io"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "FN7ZTm3pYbBPQU44creN-H5P8_LvzAlIa284CpkwdIM"))
    #查询节点属性
    query ='MATCH (c:'+attribute+' {name: $name}) RETURN  c' #'MATCH (c:Relics {name: $name}) RETURN  c'
    with driver.session() as session:
        result = session.run(query, name=name)
        #遍历结果
        for record in result:
            print(record)

if __name__ == '__main__':
    text = input("请输入要查询的句子：")
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
            chaxun(flag.capitalize(), word)
        elif flag == 'lightcones':
            flag = 'Light_cones'
            print(f"Flag: {flag}, Word: {word}")
            chaxun(flag, word)





