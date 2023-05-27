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
            MERGE (c:Character {id: $id})
            SET c.name = $name, c.icon = $icon, c.quality = $quality, c.destiny = $destiny, c.element = $element, c.occupation = $occupation, c.faction = $faction
        """, id=record['id'], name=record['name'], icon=record['icon'], quality=record['quality'],
                    destiny=record['destiny'], element=record['element'], occupation=record['information']['occupation'], faction=record['information']['faction'])

        for p in record['promote']:
            result = session.run("""
                CREATE (p:Promote {required_level: $required_level, promote_level: $promote_level, max_level: $max_level, coin: $coin})
                RETURN id(p) AS p_id
            """, required_level=p['required_level'], promote_level=p['promote_level'], max_level=p['max_level'],
                        coin=p['coin'])
            p_id = result.single()['p_id']

            session.run("""
                MATCH (c:Character {id: $id}), (p:Promote) WHERE id(p) = $p_id
                CREATE (c)-[:PROMOTES]->(p)
            """, id=record['id'], p_id=p_id)

            for item in p['items']:
                session.run("""
                    MERGE (i:Item {id: $id})
                    SET i.name = $name, i.desc = $desc, i.icon = $icon, i.quality = $quality, i.type = $type
                """, id=item['item']['id'], name=item['item']['name'], desc=item['item']['desc'],
                            icon=item['item']['icon'], quality=item['item']['quality'], type=item['item']['type'])

                session.run("""
                    MATCH (i:Item {id: $item_id}), (p:Promote) WHERE id(p) = $p_id
                    CREATE (p)-[:REQUIRES {count: $count}]->(i)
                """, p_id=p_id, item_id=item['item']['id'], count=item['count'])

        stage = 1
        for so in record['soul']:
            session.run("""
                CREATE (so:Soul {stage: $stage, name: $name, desc: $desc})
            """, name=so['name'], desc=so['desc'], stage=stage)

            session.run("""
                MATCH (c:Character {id: $id}), (so:Soul {name: $name})
                CREATE (c)-[:SOUL]->(so)
            """, id = record['id'], name=so['name'])

            stage += 1
