import json
if __name__ == '__main__':

    data = {"NN": "刻晴/遗物/建议", "DEC": "的", "VV": "搭配"}
    with open("data.json", "w") as outfile:
     json.dump(data, outfile, ensure_ascii=False, indent=4)
    # 使用json.dumps()函数进行格式化输出，并使用参数 ensure_ascii=False 避免中文显示为Unicode编码
    print(json.dumps(data, indent=4, ensure_ascii=False))
