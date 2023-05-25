from neo4j import GraphDatabase

uri = "neo4j+s://1d778504.databases.neo4j.io"
auth = ("neo4j", "FN7ZTm3pYbBPQU44creN-H5P8_LvzAlIa284CpkwdIM")

def test_neo4j_connection(query):
    # 建立数据库连接
    driver = GraphDatabase.driver(uri, auth=auth)
    session = driver.session()

    # 执行查询
    result = session.run("MATCH (n) RETURN count(n) as count")
    count = result.single()["count"]
    assert count >= 0

    # 关闭数据库连接
    session.close()
    driver.close()