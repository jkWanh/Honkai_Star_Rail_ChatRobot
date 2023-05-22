import jieba
import jieba.posseg as pseg
import json
from using_name import  *
from using_relationship import  *
from  is_true import  *
from stringsplit import  *
def clause(text):
    jieba.load_userdict("txt/user1.txt")
    words = pseg.cut(text)  # jieba默认模式
    result = []
    for word, flag in words:
        result.append({'word': word, 'flag': flag})

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False,indent=4)
def  diversion(text):
    clause(text)
    # 读取 JSON 文件
    with open('result.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
   # 提取 "flag" 和 "word" 字段的值
    for item in data:
        flag = item['flag']
        word = item['word']
        if flag == 'name':
            print(f"Flag: {flag}, Word: {word}")
            ans = name(text)
            print(ans)
            label, ans = split(ans)
            ans.insert(0, ('label', label))
            newlist = [ans]
            new_lst = [[elem[1] for elem in sublst] for sublst in newlist]
            return  new_lst

        elif flag == 'relationship':
            print(f"Flag: {flag}, Word: {word}")
            ans = relationship(text)
            print(ans)
            return ans
        elif flag == 'twotrue':
            print(1)
            print(f"Flag: {flag}, Word: {word}")
            if is_true(text) == True:
                 ans = "是的"
                 return ans
            else :
                ans = "不是的"
                return ans






