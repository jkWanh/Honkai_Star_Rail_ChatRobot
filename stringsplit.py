import re
def split(s):
    # 定义正则表达式模式
    pattern = r"<Record c=<Node element_id='[^']*' labels=frozenset\((.*?)\) properties=\{(.*?)\}>"
    # 从字符串中匹配出 labels 和 properties 的内容
    match = re.search(pattern, s)
    labels = match.group(1)
    properties = match.group(2)
    # 使用正则表达式匹配 labels 中的值
    match = re.search(r"{\s*'(.*)'\s*}", labels)
    if match:
        label_value = match.group(1)

    # 使用正则表达式匹配每个键值对
    pattern2 = r"'([^']+)': '([^']+)'"
    matches = re.findall(pattern2, properties)
    # 打印每个键值对的内容
    for key, value in matches:
        if key != 'id':
            print(key, ":", value)
    return label_value,matches
