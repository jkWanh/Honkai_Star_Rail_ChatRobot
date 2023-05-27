from neo4j import GraphDatabase
import json
from tqdm import tqdm
‘’‘
如此示例连接到Neo4j数据库，请根据实际使用的目标数据库替换URL、用户名和密码
uri = "neo4j+s://1d778504.databases.neo4j.io"
driver = GraphDatabase.driver(uri, auth=("neo4j", "FN7ZTm3pYbBPQU44creN-H5P8_LvzAlIa284CpkwdIM"))
’‘’
uri = ""
driver = GraphDatabase.driver(uri, auth=("", ""))

# 打开JSON文件
with open('DB_query/db_light_cones.py', 'r') as f:
    data = json.load(f)

# 遍历JSON对象，并将数据导入Neo4j
with driver.session() as session:
    for i, record in tqdm(enumerate(data), desc="Processing records"):
        session.run("""
            MERGE (mon:Monster {id :$id})
            SET mon.name = $name, mon.desc = $desc, mon.icon = $icon, mon.big_pic = $big_pic, mon.type = $type, mon.area = $area, mon.resistance = $resistance, mon.find_area = $find_area
        """, id=record['id'], name=record['name'], desc=record['desc'], icon=record['icon'],
                    big_pic=record['big_pic'], type=record['type'], area=record['area'], resistance=record['resistance'],
                    find_area=record['find_area'])
