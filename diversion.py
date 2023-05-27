from query import *
from stringsplit import  *
def clause(text):
    jieba.load_userdict("txt/user1.txt")
    words = pseg.cut(text)  # jieba默认模式
    result = []
    for word, flag in words:
        result.append({'word': word, 'flag': flag})

    with open('txt/result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False,indent=4)
def  diversion(text):
    clause(text)
    # 读取 JSON 文件
    with open('txt/result.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
   # 提取 "flag" 和 "word" 字段的值
    for item in data:
        flag = item['flag']
        word = item['word']
        if flag == 'name':
            print(f"Flag: {flag}, Word: {word}")
            ans = name(text)
            if ans is None:
                return 6,6
            label, ans = split(ans)
            ans.insert(0, ('label', label))
            newlist = [ans]
            new_lst = [[elem[1] for elem in sublst] for sublst in newlist]
            return  0,new_lst
        elif flag == 'twotrue':
            print(f"Flag: {flag}, Word: {word}")
            ans = is_true(text)
            if ans == 6:
                return 6,6
            return 1,ans





