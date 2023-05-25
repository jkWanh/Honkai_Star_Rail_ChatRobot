import re

import pyperclip
import requests
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QIcon, QPainter, QBrush, QPixmap
from ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QVBoxLayout, QLabel, QPushButton, \
    QHBoxLayout, QSpacerItem, QFrame, QMessageBox, QDialog, QLineEdit, QGraphicsDropShadowEffect, QFileDialog, QComboBox
import sys
from ChatGPT import *
from shutil import copyfile
import jieba
import jieba.posseg as pseg
import json
from diversion import  *
class ChatRobot(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(ChatRobot, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("./static/icon.png"))
        # 记录每次的问题和回答内容，增加聊天导出功能
        self.Questions = []
        self.Questions2 = []
        self.Answers = []
        self.Answers2 = []
        self.heros = ["三月七", '丹恒', '佩拉', '停云', '克拉拉', '姬子', '娜塔莎']
        # 调用圆形图片控件
        self.label = CircleImage(self, 150, 150)
        self.label.set_image(QPixmap('./static/avatar.png'))
        self.label.move(58, 37)
        self.label_2.setPixmap(QPixmap('./static/昵称.png'))
        self.label_2.setScaledContents(True)  # 设置图片自适应大小
        self.label_3.setPixmap(QPixmap("./static/id  ID.png"))
        self.label_3.setScaledContents(True)
        self.label_4.setPixmap(QPixmap("./static/level.png"))
        self.label_4.setScaledContents(True)
        self.set_heros()
        self.more.setIcon(QIcon("./static/省略.png"))
        self.more.setIconSize(QSize(81, 81))
        self.more.setToolTip("点击以选择角色")
        self.cha1.clicked.connect(lambda: self.hero_detail(0))
        self.cha2.clicked.connect(lambda: self.hero_detail(1))
        self.cha3.clicked.connect(lambda: self.hero_detail(2))
        self.cha4.clicked.connect(lambda: self.hero_detail(3))
        self.cha5.clicked.connect(lambda: self.hero_detail(4))
        self.cha6.clicked.connect(lambda: self.hero_detail(5))
        self.cha7.clicked.connect(lambda: self.hero_detail(6))
        self.more.clicked.connect(self.select_heros)

    def set_heros(self):
        # 设置默认常用英雄
        self.cha1.setIcon(QIcon("./static/Chatacter/%s.png" % self.heros[0]))
        self.cha1.setIconSize(QSize(81, 81))
        self.cha1.setToolTip("角色：%s\n点击以查看攻略" % self.heros[0])
        self.cha2.setIcon(QIcon("./static/Chatacter/%s.png" % self.heros[1]))
        self.cha2.setIconSize(QSize(81, 81))
        self.cha2.setToolTip("角色：%s\n点击以查看攻略" % self.heros[1])
        self.cha3.setIcon(QIcon("./static/Chatacter/%s.png" % self.heros[2]))
        self.cha3.setIconSize(QSize(81, 81))
        self.cha3.setToolTip("角色：%s\n点击以查看攻略" % self.heros[2])
        self.cha4.setIcon(QIcon("./static/Chatacter/%s.png" % self.heros[3]))
        self.cha4.setIconSize(QSize(81, 81))
        self.cha4.setToolTip("角色：%s\n点击以查看攻略" % self.heros[3])
        self.cha5.setIcon(QIcon("./static/Chatacter/%s.png" % self.heros[4]))
        self.cha5.setIconSize(QSize(81, 81))
        self.cha5.setToolTip("角色：%s\n点击以查看攻略" % self.heros[4])
        self.cha6.setIcon(QIcon("./static/Chatacter/%s.png" % self.heros[5]))
        self.cha6.setIconSize(QSize(81, 81))
        self.cha6.setToolTip("角色：%s\n点击以查看攻略" % self.heros[5])
        self.cha7.setIcon(QIcon("./static/Chatacter/%s.png" % self.heros[6]))
        self.cha7.setIconSize(QSize(81, 81))
        self.cha7.setToolTip("角色：%s\n点击以查看攻略" % self.heros[6])

    def select_heros(self):
        """
        选择常用英雄
        """
        dialog = SelectHeroDialog()
        if dialog.exec_() == QDialog.Accepted:
            self.heros = dialog.heros
            self.set_heros()
        else:
            print("Form submission canceled")

    def hero_detail(self, hero_id):
        QMessageBox.information(self, "提示", "%s" % self.heros[hero_id], QMessageBox.Ok)
        s = "介绍一下" + self.heros[hero_id]
        sign, ans = diversion(s)
        res = []
        res.append(ans[0][6])
        self.add_record("Robot",res, True, 0, 4)
    def Query(self):
        """
        此函数用于接收用户的查询内容，即search_text
        传给函数Process进行关键词提取等处理
        """
        search_text = self.lineEdit.text()
        # 如果消息不为空，则将其添加到聊天历史记录中
        if search_text:
            # 记录问题内容
            self.Questions.append(search_text)
            self.add_record("我", search_text, False, 0, 0)
            # 清空文本框中的消息
            self.lineEdit.setText('')

            # 生成回答
            answer, sign = self.Processing(search_text)
            self.add_record("Robot", answer, True, 0, sign)
        else:
            QMessageBox.information(self, "提示", "不能发送空消息！", QMessageBox.Ok)

    def Query2(self):
        """
        此函数用于接收用户的查询内容，即search_text
        交由ChatGPT进行关键词提取等处理
        """
        search_text = self.lineEdit_2.text()
        # 如果消息不为空，则将其添加到聊天历史记录中
        if search_text:
            # 记录问题内容
            self.Questions2.append(search_text)
            self.add_record("我", search_text, False, 1, 0)
            # 清空文本框中的消息
            self.lineEdit.setText('')
            # 生成回答
            answer = GPT(search_text)
            # 记录回答内容
            self.Answers2.append(answer)
            self.add_record("GPT", answer, True, 1, 0)
        else:
            QMessageBox.information(self, "提示", "不能发送空消息！", QMessageBox.Ok)

    def add_record(self, character, content, ans, mode, sign):
        """
        新增一条消息到记录框
        ans为真表示回答，否则表示问题
        mode为0表示Robot，1表示GPT
        """
        # 创建消息控件，并添加到聊天历史记录控件中
        item = QListWidgetItem()
        itemWidget = QWidget()
        itemLayout = QVBoxLayout(itemWidget)

        # 添加回答者昵称
        Label = QLabel(character)
        if ans:
            Label.setStyleSheet('font-size: 25px; color: #007d65; font-weight:bold;')
        else:
            Label.setStyleSheet('font-size: 25px; color: #f58220; font-weight:bold;')
        Label.setAlignment(Qt.AlignLeft)
        itemLayout.addWidget(Label)

        # 添加复制按钮
        copyButton = QPushButton()
        copyButton.setFixedSize(30, 30)
        copyButton.setIcon(QIcon("./static/copy.png"))
        copyButton.clicked.connect(lambda checked, message=content: self.copyMessage(content))

        # 创建水平布局，将昵称和复制按钮放在一起
        displayLayout = QHBoxLayout()
        displayLayout.addWidget(Label)
        displayLayout.addWidget(copyButton)
        spacer = QSpacerItem(40, 30)
        displayLayout.addItem(spacer)
        itemLayout.addLayout(displayLayout)

        # 判断提问或是回答
        if ans:
            match sign:
                case 0:
                    for message in content:
                        text, url = self.TextShow(message, message[0])
                        # 添加消息文本控件
                        answerLabel = QLabel(text)
                        answerLabel.setWordWrap(True)  # 设置自动换行
                        answerLabel.setStyleSheet('font-size: 20px; color: #333333;')
                        answerLabel.setFrameShape(QFrame.Panel)
                        answerLabel.setFrameShadow(QFrame.Sunken)
                        # 放入图片标签
                        try:
                            response = requests.get(url)
                            image_data = response.content
                            # 将图片数据加载到QPixmap中
                            pixmap = QPixmap()
                            pixmap.loadFromData(image_data)
                        except Exception as exc:
                            print(exc)
                            pixmap = QPixmap("./static/avatar.png")
                            # 设置QLabel的图片
                        iconlabel = QLabel()
                        iconlabel.setPixmap(pixmap)
                        iconlabel.setScaledContents(True)  # 设置图片自适应大小
                        iconlabel.setFixedSize(280, 280)
                        # 创建水平布局
                        displayLayout = QHBoxLayout()
                        displayLayout.addWidget(iconlabel)
                        spacer = QSpacerItem(30, 30)
                        displayLayout.addItem(spacer)
                        displayLayout.addWidget(answerLabel)

                        itemLayout.addLayout(displayLayout)
                        itemWidget.setStyleSheet('background-color: #afdfe4; border-radius: 10px; margin: 5px;')
                case 1:
                    for message in content:
                        text = message[0]
                        url = message[1]
                        # 添加消息文本控件
                        answerLabel = QLabel(text)
                        answerLabel.setWordWrap(True)  # 设置自动换行
                        answerLabel.setStyleSheet('font-size: 20px; color: #333333;')
                        answerLabel.setFrameShape(QFrame.Panel)
                        answerLabel.setFrameShadow(QFrame.Sunken)
                        # 放入图片标签
                        try:
                            response = requests.get(url)
                            image_data = response.content
                            # 将图片数据加载到QPixmap中
                            pixmap = QPixmap()
                            pixmap.loadFromData(image_data)
                        except Exception as exc:
                            print(exc)
                            pixmap = QPixmap("./static/avatar.png")
                            # 设置QLabel的图片
                        iconlabel = QLabel()
                        iconlabel.setPixmap(pixmap)
                        iconlabel.setScaledContents(True)  # 设置图片自适应大小
                        iconlabel.setFixedSize(80, 80)
                        # 创建水平布局
                        displayLayout = QHBoxLayout()
                        displayLayout.addWidget(iconlabel)
                        spacer = QSpacerItem(10, 30)
                        displayLayout.addItem(spacer)
                        displayLayout.addWidget(answerLabel)

                        itemLayout.addLayout(displayLayout)
                        itemWidget.setStyleSheet('background-color: #afdfe4; border-radius: 10px; margin: 5px;')
                case 2:  # 只显示图片
                    for url in content:
                        # 放入图片标签
                        try:
                            response = requests.get(url)
                            image_data = response.content
                            # 将图片数据加载到QPixmap中
                            pixmap = QPixmap()
                            pixmap.loadFromData(image_data)
                        except Exception as exc:
                            print(exc)
                            pixmap = QPixmap("./static/avatar.png")
                            # 设置QLabel的图片
                        iconlabel = QLabel()
                        iconlabel.setPixmap(pixmap)
                        iconlabel.setScaledContents(True)  # 设置图片自适应大小
                        iconlabel.setFixedSize(300, 300)
                        itemLayout.addWidget(iconlabel)
                        itemWidget.setStyleSheet('background-color: #afdfe4; border-radius: 10px; margin: 5px;')
                case 3:  # 只显示文字
                    for answer in content:
                        # 添加消息文本控件
                        ansLabel = QLabel(answer)
                        ansLabel.setWordWrap(True)  # 设置自动换行
                        ansLabel.setStyleSheet('font-size: 20px; color: #333333;')
                        ansLabel.setFrameShape(QFrame.Panel)
                        ansLabel.setFrameShadow(QFrame.Sunken)
                        itemLayout.addWidget(ansLabel)
                        itemWidget.setStyleSheet('background-color: #cde6c7; border-radius: 10px; margin: 5px;')
                case 4:  # 显示角色的攻略
                    for url in content:
                        # 放入图片标签
                        try:
                            response = requests.get(url)
                            image_data = response.content
                            # 将图片数据加载到QPixmap中
                            pixmap = QPixmap()
                            pixmap.loadFromData(image_data)
                        except Exception as exc:
                            print(exc)
                            pixmap = QPixmap("./static/avatar.png")
                            # 设置QLabel的图片
                        iconlabel = QLabel()
                        iconlabel.setPixmap(pixmap)
                        iconlabel.setScaledContents(True)  # 设置图片自适应大小
                        iconlabel.setFixedSize(1000, 800)
                        itemLayout.addWidget(iconlabel)
                        itemWidget.setStyleSheet('background-color: #afdfe4; border-radius: 10px; margin: 5px;')
                case 5:  # 显示gpt回答
                    pass
        else:
            # 添加消息文本控件
            questionLabel = QLabel(content)
            questionLabel.setWordWrap(True)  # 设置自动换行
            questionLabel.setStyleSheet('font-size: 20px; color: #333333;')
            questionLabel.setFrameShape(QFrame.Panel)
            questionLabel.setFrameShadow(QFrame.Sunken)
            itemLayout.addWidget(questionLabel)
            itemWidget.setStyleSheet('background-color: #cde6c7; border-radius: 10px; margin: 5px;')

        # 将消息控件添加到聊天历史记录控件中
        item.setSizeHint(itemWidget.sizeHint())
        if mode:
            self.listWidget_2.addItem(item)
            self.listWidget_2.setItemWidget(item, itemWidget)
            self.listWidget_2.scrollToBottom()
        else:
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, itemWidget)
            self.listWidget.scrollToBottom()

    def TextShow(self, mess_list, label):
        """
        将从数据库中获得的，经过预处理的列表数据加以充实
        """
        text = ""
        match label:
            case "Character":
                text += "角色：" + mess_list[4] + "\n\n"
                text += "属性：" + mess_list[7] + "\n\n品质：" + mess_list[6] + "\n\n"
                text += "命运：" + mess_list[1] + "\n\n"
                text += "职业：" + mess_list[2] + "\n\n"
                text += "派别：" + mess_list[3]
                url = mess_list[5]
                print(url)
                return text, url
            case "Monster":
                text += "怪物名：" + mess_list[3] + "\n\n"
                text += "地域：" + mess_list[1] + "\n\n"
                text += "发现地：" + mess_list[4] + "\n\n"
                text += "类型：" + mess_list[6] + "\n\n"
                text += "抵抗：" + mess_list[7] + "\n\n"
                text += "描述：" + mess_list[8]
                url = mess_list[5]
                return text, url
            case "Material":
                text += "名称：" + mess_list[1] + "\n\n"
                text += "类型：" + mess_list[3] + "\n\n"
                text += "品质：" + mess_list[5] + "\n\n"
                text += "描述：" + mess_list[4]
                url = mess_list[2]
                return text, url

    def copyMessage(self, message):
        """
        复制消息到剪贴板
        """
        pyperclip.copy(message)

    def Process(self, search_text):
        flag, ans = diversion(search_text)
        return ans, flag
        pass

    def Processing(self, search_text):
        ans, sign = self.Process(search_text)
        print(ans)
        clause(search_text)
        # 读取 JSON 文件
        with open('result.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            # 提取 "flag" 和 "word" 字段的值
            for item in data:
                flag = item['flag']
                word = item['word']
                if word == "图像":
                    for item in data:
                        flag = item['flag']
                        word = item['word']
                        if flag == 'character':
                            res = []
                            res.append(ans[0][5])
                            print(res)
                            return res, 2
                        elif flag == 'material':
                            res = []
                            res.append(ans[0][2])
                            print(res)
                            return res, 2
                        elif flag == 'monster':
                            res = []
                            res.append(ans[0][2])
                            print(res)
                            return res, 2

                elif flag == 'type':
                    res = []
                    res.append(ans[0][8])
                    print(res)
                    return res, 3
                elif flag == 'fate':
                    res = []
                    res.append(ans[0][1])
                    result = []
                    result.append(res)
                    print(result)
                    return res, 3
            return ans, sign

    def clause(text):
        jieba.load_userdict("txt/user1.txt")
        words = pseg.cut(text)  # jieba默认模式
        result = []
        for word, flag in words:
            result.append({'word': word, 'flag': flag})

        with open('result.json', 'w', encoding='utf-8') as file:
            json.dump(result, file, ensure_ascii=False, indent=4)

    def EditInfo(self):
        """
        修改个人信息
        """
        dialog = FormDialog()
        if dialog.exec_() == QDialog.Accepted:
            self.label_6.setText(dialog.name)
            self.label_7.setText(dialog.UID)
            self.label_8.setText(dialog.level)
            if dialog.file_path is not None:
                try:
                    os.remove("./static/avatar.png")
                    copyfile(dialog.file_path, "./static/avatar.png")
                    self.label.set_image(QPixmap('./static/avatar.png'))
                except Exception as exc:
                    print(exc)
        else:
            print("Form submission canceled")


class QSSLoader:
    """
    加载QSS样式类
    """

    def __init__(self):
        pass

    @staticmethod
    def read_qss_file(qss_file_name):
        with open(qss_file_name, 'r', encoding='UTF-8') as file:
            return file.read()


class CircleImage(QLabel):
    """
    绘制圆形图片工具类
    """

    def __init__(self, parent, width, height):
        super(CircleImage, self).__init__(parent)
        self.resize(width, height)
        self.circle_image = None

    def set_image(self, image):
        # 设置绘制的图片
        self.circle_image = image.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.update()

    def paintEvent(self, event):
        # 重写绘制事件
        super(CircleImage, self).paintEvent(event)
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        brush = QBrush(self.circle_image)
        painter.setBrush(brush)
        painter.setRenderHints(QPainter.Antialiasing, True)
        painter.drawEllipse(QRect(0, 0, self.width(), self.height()))


class FormDialog(QDialog):
    """
    提交表单对话类
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("更改个人信息")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setFixedSize(500, 400)
        self.file_path = None
        self.label0 = QLabel("头像：")
        self.avatar = QPushButton("点击选择文件")
        self.avatar.clicked.connect(self.upload)
        self.label = QLabel("昵称：")
        self.line_edit = QLineEdit()
        self.label2 = QLabel("UID：")
        self.line_edit2 = QLineEdit()
        self.label3 = QLabel("等级")
        self.line_edit3 = QLineEdit()

        self.submit_button = QPushButton("确定")
        self.submit_button.clicked.connect(self.submit_form)

        self.layout.addWidget(self.label0)
        self.layout.addWidget(self.avatar)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.line_edit2)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.line_edit3)
        self.layout.addWidget(self.submit_button)

    def submit_form(self):
        self.name = self.line_edit.text()
        self.UID = self.line_edit2.text()
        self.level = self.line_edit3.text()
        self.accept()

    def upload(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        # file_dialog.setNameFilter("(*.png);;(*.jpg)")
        file_dialog.setNameFilter("(*.png)")

        if file_dialog.exec_():
            self.file_path = file_dialog.selectedFiles()[0]
            self.avatar.setText(re.search('(\w*.png)$', self.file_path).group(1))


class SelectHeroDialog(QDialog):
    """
    选择英雄对话类
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("选择常用角色")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.heros = []

        self.label1 = QLabel("角色一")
        self.label2 = QLabel("角色二")
        self.label3 = QLabel("角色三")
        self.label4 = QLabel("角色四")
        self.label5 = QLabel("角色五")
        self.label6 = QLabel("角色六")
        self.label7 = QLabel("角色七")

        self.cha1 = QComboBox()
        self.cha1.addItem("三月七", 0)
        self.cha1.addItem("丹恒", 1)
        self.cha1.addItem("佩拉", 2)
        self.cha1.addItem("停云", 3)
        self.cha1.addItem("克拉拉", 4)
        self.cha1.addItem("姬子", 5)
        self.cha1.addItem("娜塔莎", 6)
        self.cha1.addItem("布洛妮娅", 7)
        self.cha1.addItem("希儿", 8)
        self.cha1.addItem("希露瓦", 9)
        self.cha1.addItem("开拓者·存护", 10)
        self.cha1.addItem("开拓者·毁灭", 11)
        self.cha1.addItem("彦卿", 12)
        self.cha1.addItem("杰帕德", 13)
        self.cha1.addItem("桑博", 14)
        self.cha1.addItem("瓦尔特", 15)
        self.cha1.addItem("白露", 16)
        self.cha1.addItem("素裳", 17)
        self.cha1.addItem("艾丝妲", 18)
        self.cha1.addItem("虎克", 19)
        self.cha1.addItem("阿兰", 20)
        self.cha1.addItem("青雀", 21)
        self.cha1.addItem("黑塔", 22)
        self.cha2 = QComboBox()
        self.cha2.addItem("丹恒", 0)
        self.cha2.addItem("三月七", 1)
        self.cha2.addItem("佩拉", 2)
        self.cha2.addItem("停云", 3)
        self.cha2.addItem("克拉拉", 4)
        self.cha2.addItem("姬子", 5)
        self.cha2.addItem("娜塔莎", 6)
        self.cha2.addItem("布洛妮娅", 7)
        self.cha2.addItem("希儿", 8)
        self.cha2.addItem("希露瓦", 9)
        self.cha2.addItem("开拓者·存护", 10)
        self.cha2.addItem("开拓者·毁灭", 11)
        self.cha2.addItem("彦卿", 12)
        self.cha2.addItem("杰帕德", 13)
        self.cha2.addItem("桑博", 14)
        self.cha2.addItem("瓦尔特", 15)
        self.cha2.addItem("白露", 16)
        self.cha2.addItem("素裳", 17)
        self.cha2.addItem("艾丝妲", 18)
        self.cha2.addItem("虎克", 19)
        self.cha2.addItem("阿兰", 20)
        self.cha2.addItem("青雀", 21)
        self.cha2.addItem("黑塔", 22)
        self.cha3 = QComboBox()
        self.cha3.addItem("佩拉", 0)
        self.cha3.addItem("丹恒", 1)
        self.cha3.addItem("三月七", 2)
        self.cha3.addItem("停云", 3)
        self.cha3.addItem("克拉拉", 4)
        self.cha3.addItem("姬子", 5)
        self.cha3.addItem("娜塔莎", 6)
        self.cha3.addItem("布洛妮娅", 7)
        self.cha3.addItem("希儿", 8)
        self.cha3.addItem("希露瓦", 9)
        self.cha3.addItem("开拓者·存护", 10)
        self.cha3.addItem("开拓者·毁灭", 11)
        self.cha3.addItem("彦卿", 12)
        self.cha3.addItem("杰帕德", 13)
        self.cha3.addItem("桑博", 14)
        self.cha3.addItem("瓦尔特", 15)
        self.cha3.addItem("白露", 16)
        self.cha3.addItem("素裳", 17)
        self.cha3.addItem("艾丝妲", 18)
        self.cha3.addItem("虎克", 19)
        self.cha3.addItem("阿兰", 20)
        self.cha3.addItem("青雀", 21)
        self.cha3.addItem("黑塔", 22)
        self.cha4 = QComboBox()
        self.cha4.addItem("停云", 0)
        self.cha4.addItem("丹恒", 1)
        self.cha4.addItem("佩拉", 2)
        self.cha4.addItem("三月七", 3)
        self.cha4.addItem("克拉拉", 4)
        self.cha4.addItem("姬子", 5)
        self.cha4.addItem("娜塔莎", 6)
        self.cha4.addItem("布洛妮娅", 7)
        self.cha4.addItem("希儿", 8)
        self.cha4.addItem("希露瓦", 9)
        self.cha4.addItem("开拓者·存护", 10)
        self.cha4.addItem("开拓者·毁灭", 11)
        self.cha4.addItem("彦卿", 12)
        self.cha4.addItem("杰帕德", 13)
        self.cha4.addItem("桑博", 14)
        self.cha4.addItem("瓦尔特", 15)
        self.cha4.addItem("白露", 16)
        self.cha4.addItem("素裳", 17)
        self.cha4.addItem("艾丝妲", 18)
        self.cha4.addItem("虎克", 19)
        self.cha4.addItem("阿兰", 20)
        self.cha4.addItem("青雀", 21)
        self.cha4.addItem("黑塔", 22)
        self.cha5 = QComboBox()
        self.cha5.addItem("克拉拉", 0)
        self.cha5.addItem("丹恒", 1)
        self.cha5.addItem("佩拉", 2)
        self.cha5.addItem("停云", 3)
        self.cha5.addItem("三月七", 4)
        self.cha5.addItem("姬子", 5)
        self.cha5.addItem("娜塔莎", 6)
        self.cha5.addItem("布洛妮娅", 7)
        self.cha5.addItem("希儿", 8)
        self.cha5.addItem("希露瓦", 9)
        self.cha5.addItem("开拓者·存护", 10)
        self.cha5.addItem("开拓者·毁灭", 11)
        self.cha5.addItem("彦卿", 12)
        self.cha5.addItem("杰帕德", 13)
        self.cha5.addItem("桑博", 14)
        self.cha5.addItem("瓦尔特", 15)
        self.cha5.addItem("白露", 16)
        self.cha5.addItem("素裳", 17)
        self.cha5.addItem("艾丝妲", 18)
        self.cha5.addItem("虎克", 19)
        self.cha5.addItem("阿兰", 20)
        self.cha5.addItem("青雀", 21)
        self.cha5.addItem("黑塔", 22)
        self.cha6 = QComboBox()
        self.cha6.addItem("姬子", 0)
        self.cha6.addItem("丹恒", 1)
        self.cha6.addItem("佩拉", 2)
        self.cha6.addItem("停云", 3)
        self.cha6.addItem("克拉拉", 4)
        self.cha6.addItem("三月七", 5)
        self.cha6.addItem("娜塔莎", 6)
        self.cha6.addItem("布洛妮娅", 7)
        self.cha6.addItem("希儿", 8)
        self.cha6.addItem("希露瓦", 9)
        self.cha6.addItem("开拓者·存护", 10)
        self.cha6.addItem("开拓者·毁灭", 11)
        self.cha6.addItem("彦卿", 12)
        self.cha6.addItem("杰帕德", 13)
        self.cha6.addItem("桑博", 14)
        self.cha6.addItem("瓦尔特", 15)
        self.cha6.addItem("白露", 16)
        self.cha6.addItem("素裳", 17)
        self.cha6.addItem("艾丝妲", 18)
        self.cha6.addItem("虎克", 19)
        self.cha6.addItem("阿兰", 20)
        self.cha6.addItem("青雀", 21)
        self.cha6.addItem("黑塔", 22)
        self.cha7 = QComboBox()
        self.cha7.addItem("娜塔莎", 0)
        self.cha7.addItem("丹恒", 1)
        self.cha7.addItem("佩拉", 2)
        self.cha7.addItem("停云", 3)
        self.cha7.addItem("克拉拉", 4)
        self.cha7.addItem("姬子", 5)
        self.cha7.addItem("三月七", 6)
        self.cha7.addItem("布洛妮娅", 7)
        self.cha7.addItem("希儿", 8)
        self.cha7.addItem("希露瓦", 9)
        self.cha7.addItem("开拓者·存护", 10)
        self.cha7.addItem("开拓者·毁灭", 11)
        self.cha7.addItem("彦卿", 12)
        self.cha7.addItem("杰帕德", 13)
        self.cha7.addItem("桑博", 14)
        self.cha7.addItem("瓦尔特", 15)
        self.cha7.addItem("白露", 16)
        self.cha7.addItem("素裳", 17)
        self.cha7.addItem("艾丝妲", 18)
        self.cha7.addItem("虎克", 19)
        self.cha7.addItem("阿兰", 20)
        self.cha7.addItem("青雀", 21)
        self.cha7.addItem("黑塔", 22)

        self.submit_button = QPushButton("确定")
        self.submit_button.clicked.connect(self.submit_form)

        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.cha1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.cha2)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.cha3)
        self.layout.addWidget(self.label4)
        self.layout.addWidget(self.cha4)
        self.layout.addWidget(self.label5)
        self.layout.addWidget(self.cha5)
        self.layout.addWidget(self.label6)
        self.layout.addWidget(self.cha6)
        self.layout.addWidget(self.label7)
        self.layout.addWidget(self.cha7)
        self.layout.addWidget(self.submit_button)

    def submit_form(self):
        self.heros.append(self.cha1.currentText())
        self.heros.append(self.cha2.currentText())
        self.heros.append(self.cha3.currentText())
        self.heros.append(self.cha4.currentText())
        self.heros.append(self.cha5.currentText())
        self.heros.append(self.cha6.currentText())
        self.heros.append(self.cha7.currentText())
        self.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建对象
    robot = ChatRobot()
    robot.setFixedSize(1408, 875)
    # 加载QSS样式表
    style_file = 'ui.qss'
    style_sheet = QSSLoader.read_qss_file(style_file)
    robot.setStyleSheet(style_sheet)
    # 创建窗口
    robot.show()
    # 进入程序的主循环
    sys.exit(app.exec_())