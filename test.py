if __name__ == '__main__':
    records = "<Record c.name='开拓者·存护'><Record c.name='瓦尔特'><Record c.name='开拓者·毁灭'><Record c.name='姬子'><Record c.name='丹恒'><Record c.name='三月七'>"

    new_lst = [name.split("'")[1] for name in records.split("<Record c.name=")[1:]]

    print(new_lst)