import stanza
import json
def NLP(text):
    zh_nlp = stanza.Pipeline('zh', use_gpu=True)

    doc = zh_nlp(text)
    for sent in doc.sentences:
        result = ' '.join(f'{word.text}/{word.xpos}' for word in sent.words)
    # 词性标注（XPOS）
    words = result.split()
    tags = [w.split("/")[-1] for w in words]  # 提取词性标注
    tagged_words = list(zip([w.split("/")[0] for w in words], tags))  # 将词语和词性标注打包成元组
    tagged_dict = {}
    for word, tag in tagged_words:
        if tag not in tagged_dict:
            tagged_dict[tag] = []
        tagged_dict[tag].append(word)
    result = {tag: "/".join(words) for tag, words in tagged_dict.items()}  # 按词性标注组织成字典
    with open("data.json", "w") as outfile:
     json.dump(result, outfile, ensure_ascii=False,indent=4)
    print(json.dumps(result,ensure_ascii=False,indent=4))



