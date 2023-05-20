import os
import openai

key1 = "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"
key2 = "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"


def GPT(question):
    """
    根据messages指导ChatGPT让其生成想要的回答
    """
    messages = [{"role": "system",
                 "content": "假如你是一个智能机器人，会根据用户提出的问题提取关键字，并生成在Neo4j数据库中的查询语句。数据库中包含节点label：Character，Light_cones，Material，Monster，Occupation，Promote，Relics，Soul，Store"},
                {"role": "user", "content": "三月七突破60级需要什么材料"}, {"role": "assistant",
                                                                "content": "```cypher\nMATCH (c:Character {name: \"三月七\"})\nMATCH (m:Material)\nMATCH (c)-[:Promote]->(p:Promote)-[:Material]->(m)\nWHERE p.level = 60\nRETURN m.name\n```"},
                {"role": "user", "content": "篡夺的野心是谁的材料"}, {"role": "assistant",
                                                            "content": "```cypher\nMATCH (m:Material {name: \"篡夺的野心\"})\nMATCH (m)<-[:Material]-(p:Promote)<-[:Promote]-(c:Character)\nRETURN p.level\n```"},
                {"role": "user", "content": question}]
    openai.api_key = os.getenv("gpt_key")   # 获得API—key
    if openai.api_key is None:
        openai.api_key = key1
    try:
        completion = openai.ChatCompletion.create(  # 调用API生成回答
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=1.3,
            max_tokens=200,
            top_p=0.6,
            presence_penalty=-1,
            frequency_penalty=0
        )
        return completion.choices[0].message["content"].strip()
    except Exception as exc:
        print(exc)
        return None


if __name__ == "__main__":
    print(GPT("三月七突破60级需要什么材料"))
