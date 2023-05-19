from neo4j import GraphDatabase
# 连接到Neo4j数据库
uri = "neo4j+s://1d778504.databases.neo4j.io"
driver = GraphDatabase.driver(uri, auth=("neo4j", "FN7ZTm3pYbBPQU44creN-H5P8_LvzAlIa284CpkwdIM"))

def SingalNode_Query(label:str, condition:str):
    query = f'MATCH (c:{label} {{{condition}}}) RETURN  c'
    return query
'''
This is an example about how to use this function

x = SingalNode_Query('Character', 'name:"三月七"')

with driver.session() as session:
    result = session.run(x)
    #遍历结果
    for record in result:
        print(record)
'''
