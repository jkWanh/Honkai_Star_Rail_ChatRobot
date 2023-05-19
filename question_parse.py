from  CORENLP import NLP
import json
import csv
import pandas as pd
from GLOBALVAR import *

# 判断某个NNP是否是Character的name
def is_Character(nnp):
    path = './dicts/Character.csv'
    data = pd.read_csv(path) 
    #data为结构体
    #读取某一列,并转为list
    y = data['name'].values.tolist()
    print(y)
    

    if nnp in y:
        return 1

def json2dict():
    f = open("data.json" , 'r')
    content = f .read()
    a = json.loads(content)

    res = {k:a[k] for k in a if k == "NNP"}
    print(res)
    f.close()

    

    
        

if __name__ == '__main__':

    switch_handler = int(input("请输入查询序号:"))
    text = input("请输入查询内容:")
    NLP(text)
    
    if switch_handler == 1: #进行角色节点内部查询
        f = open("data.json" , 'r')
        content = f .read()
        a = json.loads(content)
        print(a)
        f.close()

        
        if is_Character(a.get('NNP')) == 1: 
            json2dict()
        else:
            print("没有查询到该角色")


    
        

