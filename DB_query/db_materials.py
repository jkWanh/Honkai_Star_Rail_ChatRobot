from neo4j import GraphDatabase
import json
from tqdm import tqdm
# 连接到Neo4j数据库
uri = "neo4j+s://1d778504.databases.neo4j.io"
driver = GraphDatabase.driver(uri, auth=("neo4j", "FN7ZTm3pYbBPQU44creN-H5P8_LvzAlIa284CpkwdIM"))

# 打开JSON文件
with open('DB_query/db_light_cones.py', 'r') as f:
    data = json.load(f)

# 遍历JSON对象，并将数据导入Neo4j
with driver.session() as session:
    for i, record in tqdm(enumerate(data), desc="Processing records"):
        session.run("""
            MERGE (m:Material {id: $id})
            SET m.name = $name, m.desc = $desc, m.icon = $icon, m.quality = $quality, m.type = $type
        """, id=record['id'], name=record['name'], desc=record['desc'], icon = record['icon'], quality=record['quality'], type=record['type'])