import re
def split(s):


    # 定义正则表达式模式
    pattern = r"<Record c=<Node element_id='[^']*' labels=frozenset\((.*?)\) properties=\{(.*?)\}>"
    #s= "<Record c=<Node element_id='4:bfe4a058-1be6-45ce-a716-0a2159896c52:685' labels=frozenset({'Character'}) properties={'destiny': '毁灭', 'occupation': '雅利洛-VI', 'faction': '/', 'name': '克拉拉', 'icon': 'https://uploadstatic.mihoyo.com/sr-wiki/2023/03/09/187636729/6b0b412b079a5610d34c2d87a9faf665_5273843714696308389.png', 'id': 414, 'quality': '五星', 'element': '物理'}>>"
    # 从字符串中匹配出 labels 和 properties 的内容
    match = re.search(pattern, s)
    labels = match.group(1)
    properties = match.group(2)
    # 使用正则表达式匹配 labels 中的值
    match = re.search(r"{\s*'(.*)'\s*}", labels)
    if match:
        label_value = match.group(1)

    print(label_value)
    # 使用正则表达式匹配每个键值对
    pattern2 = r"'([^']+)': '([^']+)'"
    matches = re.findall(pattern2, properties)
    # 打印每个键值对的内容
    for key, value in matches:
        if key != 'id':
            print(key, ":", value)
    return label_value,matches