import stanza
if __name__ == '__main__':
    zh_nlp = stanza.Pipeline('zh', use_gpu=True)
    text = "散兵是纳西妲的亲爹"

    doc = zh_nlp(text)
    for sent in doc.sentences:

        print("Sentence：" + sent.text)  # 断句
        print("Tokenize：" + ' '.join(token.text for token in sent.tokens))  # 中文分词
        print("UPOS: " + ' '.join(f'{word.text}/{word.upos}' for word in sent.words))  # 词性标注（UPOS）
        print("XPOS: " + ' '.join(f'{word.text}/{word.xpos}' for word in sent.words))  # 词性标注（XPOS）
        print("NER: " + ' '.join(f'{ent.text}/{ent.type}' for ent in sent.ents))  # 命名实体识别
        print()#刻晴/NN 的/DEC 遗物/NN 搭配/VV 建议/NN


