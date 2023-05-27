import os
import openai
from neo4j import GraphDatabase

key1 = "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"
key2 = "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"
background1 = '''我配置了一个图数据库用于设计聊天机器人，以下是数据库的一些信息
节点及其属性有：
(:Character {destiny,occupation,faction,name,icon,id,quality,element})
(:Light_cones {destiny,name,icon,id,big_pic,quality,desc}) 
(:Material {name,icon,id,type,desc,quality})  
(:Monster {area,icon,name,find_area,id,big_pic,type,resistance,desc})
(:Occupation {name})
(:Promote {required_level,coin})
(:Relics {access,affect,name,icon,id}) 
(:Soul {stage,name,desc}) 
(:Store {notes,name,id,place,type}) 
关系有：
Currency(在Store和Material之间）
Fall（在Monster和Material之间）
HAS_Character(在Character和Occupation之间）
HAS_Monster(在Monster和Occupation之间）
PROMOTES（在Character/Light_cones和Promote之间）
REQUIRES（在Promote和Material之间，并有属性count）
SOUL（在Character和Soul之间）
Sales（在Material和Store之间）
请注意，为了减少查询错误，请你在查询的时候只匹配节点的属性，对关系都使用-[:<关系名>]-而不要用关系的属性作为查询条件！！！
同时请使用用-[]-这样不含箭头的方法构建查询条件！！！
下面是各类节点名称的表：[character: '三月七', '黑塔', '艾丝妲', '虎克', '希儿', '阿兰', '桑博', '丹恒', '姬子', '开拓者·毁灭', '素裳', '克拉拉', '佩拉', '希露瓦', '杰帕德', '布洛妮娅', '青雀', '瓦尔特', '停云', '白露',  '彦卿', '开拓者·存护'],
[monster:'永冬灾影', '银鬃尉官', '自动机兵「战犬」', '自动机兵「灰熊」', '守护者之影', '银鬃近卫', '虚卒·掠夺者', '虚卒·抹消者', '虚卒·篡改者', '重子', '外宇宙之炎', '炎华造物', '霜晶造物', '银鬃射手', '外宇宙之冰','自动机兵「蜘蛛」', '次元扑满', '炽燃徘徊者', '可可利亚，虚妄之母', '流浪者', '虚卒·践踏者', '无想面具','可可利亚', '杰帕德', '自动机兵「齿狼」', '银鬃炮手', '兴风者', '火焚灾影', '反重子','自动机兵「甲虫」', '虚数织叶者', '布洛妮娅', '史瓦罗', '深寒徘徊者', '末日兽', '魔阴身士卒', '巽风造物', '金人司阍', '「药王秘传」炼形者', '入魔机巧·灯昼龙鱼', '入魔机巧·率从狻猊', '入魔机巧·浓云金蟾', '鸣雷造物', '「星核猎手」卡芙卡', '云骑巡防士卒', '蚕食者之影', '丰饶玄鹿', '「药王秘传」内丹士'],
[soul:'辨识药理', '临床研学', '对症下药', '妙手回春', '医治未病', '医者仁心', '记忆中的你', '记忆中的它','记忆中的一切', '不愿再失去', '不想再忘却', '就这样，一直...', '落井当下石', '得胜必追击','我就是这样女子', '打人要打脸', '骂人不留口', '世上没人能负我', '星有无言之歌', '月见圆缺之意','黄道陨石之变', '极光显现之时', '深空天体之迷', '眠于银河之下', '早睡早起很健康', '吃好喝好长身体','不挑不选全都要', '稀里糊涂没关系', '好事留名鼹鼠党', '随时准备打坏人', '斩尽', '蝶舞', '缭乱', '掠影','锋锐', '离析', '万死不辞', '除制去缚', '重剑强攻', '绝处反击', '全力倾注', '以身作引', '加码的爱', '热情会传染', '大数字！', '爱之深，恨之切', '超大数字！', '消费升级', '穷高极天，亢盈难久','威制八毒，灭却炎烟', '幽明变化，自在蟠跃', '奋迅三昧，如日空居', '一谛天水，六虚洪流', '须绳缚身，沉潜勿用','童年', '邂逅', '自我', '投入', '梦想', '开拓！', '坠临万界的星芒', '因缘假合的人身','揭示前路的言灵', '凝眸毁灭的瞬间', '劫余重生的希望', '拓宇行天的意志', '游刃有余', '其身百炼', '传古剑流', '其心百辟', '太虚神意', '上善若水', '高大的背影', '紧紧的拥抱', '冰冷的钢甲', '家人的温暖', '小小的承诺', '长久的陪伴', '胜利反馈', '疾进不止', '压制升级', '完全剖析', '零度妨害', '疲弱追击','余音绕梁', '安可！', '听，齿轮的心跳', '制造噪音吧！', '贝洛伯格最强音！', '这一曲，贯穿天穹！', '恪尽职守', '余寒', '永不陷落', '精诚所至', '拳似寒铁', '不屈的决意', '养精蓄锐', '快速行军', '鼓炮齐鸣', '攻其不备', '所向克捷', '气贯长虹', '散勇化骁摸幺鱼', '棋枰作枕好入眠', '观琼视茕门前清', '帝垣翔鳞和绝张', '七星流离全不靠', '虚心平意候枭卢', '名的传承', '星的凝聚', '和平的祈愿', '义的名号','善的力量', '光明的未来', '春风得意，时运驰骋', '君子惠渥，晏笑承之', '青丘遗泽', '鸣火机变，度时察势','绥绥狐魅', '和气生财，泽盈四方', '百脉甘津宁神久', '壶中洞天云螭眠', '掌间乾坤便通玄', '肘后备急除外障','方定一倾浣俗尘', '龙漦吐哺胜金丹', '素刃', '空明', '剑胎', '霜厉', '武骨', '自在', '大地芯髓的鸣动', '古老寒铁的坚守', '砌造未来的蓝图', '驻留文明的誓言', '点燃光焰的勇气', '永屹城垣的壁垒']
[light_cones:'唯有沉默', '「我」的诞生', '别让世界静下来', '一场术后对话', '秘密誓心', '晚安与睡颜', '猎物的视线','鼹鼠党欢迎你', '记忆中的模样', '与行星相会', '于夜色中', '余生的第一天', '以世界之名', '论剑', '天倾', '乐圮', '灵钥', '锋镝', '离弦', '智库', '轮契', '齐颂', '琥珀', '渊环', '幽邃', '戍御','物穰', '嘉果', '同一种心情', '但战斗还未结束', '无可取代的东西', '制胜的瞬间', '银河铁道之夜', '朗道的选择', '暖夜不会漫长', '这就是我啦！', '后会有期', '镂月裁云之意', '早餐的仪式感','今日亦是和平的一日', '重返幽冥', '汪！散步时间！', '无处可逃', '调和', '匿影', '开疆', '蕃息','睿见', '相抗', '俱殁', '如泥酣眠', '时节不居', '记一位星神的陨落', '在蓝天下', '此时恰好','等价交换', '宇宙市场趋势', '我们是地火', '延长记号', '舞！舞！舞！', '过往未来', '决心如汗珠般闪耀','点个关注吧！', '春水初生', '天才们的休憩', '星海巡航', '记忆的质料'],
[store:'商店「光锥呈现」', '⿊塔的商店', '宝饵堂', '杂货⼩摊', '三余书肆', '杂货⼩摊', '不夜候', '售货机','⼩吃摊', '小吃摊', '售货机', '书商', '行政区商店', '卖报⼈', '赎珠阁', '空间站[⿊塔]','地底商店']
接下来我将模拟用户提出问题，请你生成查询语句"
'''
background2 = '''我设计了一个基于图数据库的崩坏：星穹铁道聊天机器人，请你根据数据库的查询结果和用户的问题给出用户回答。'''


def get_ask_message(question, background=background1):
    messages = [
        {"role": "system",
         "content": background},
        {"role": "user", "content": question}]
    return messages


def get_answer(question, result, background=background2):
    messages = [{"role": "system", "content": background},
                {"role": "user", "content": question},
                {"role": "system", "content": result}]
    return messages


def GPT(messages):
    """
    根据messages指导ChatGPT让其生成想要的回答
    """
    openai.api_key = os.getenv("gpt_key")  # 获得API—key
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


def chaxun(query):
    # 连接到Neo4j数据库
    uri = "neo4j+s://1d778504.databases.neo4j.io"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "FN7ZTm3pYbBPQU44creN-H5P8_LvzAlIa284CpkwdIM"))
    record_str = []
    with driver.session() as session:
        result = session.run(query)
        # 遍历结果
        for record in result:
            record_str.append(str(record))
        return str(record_str)


def gpt(question):
    ask_message = get_ask_message(question=question)
    query = GPT(messages=ask_message)
    # print(query)
    if query is None:
        return "无法连接到ChatGPT，请检查您的网络与API-key配置"
    else:
        result = chaxun(query)
    # print(result)
        answer_messege = get_answer(question=question, result=result)
        answer = GPT(messages=answer_messege)
    # print(answer)
    return answer