import pyperclip
import requests
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QIcon, QPainter, QBrush, QPixmap
from ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QVBoxLayout, QLabel, QPushButton, \
    QHBoxLayout, QSpacerItem, QFrame, QMessageBox, QDialog, QLineEdit
import sys
from ChatGPT import *
from diversion import  *
class ChatRobot(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(ChatRobot, self).__init__()
        self.setupUi(self)
        # 记录每次的问题和回答内容，增加聊天导出功能
        self.Questions = []
        self.Questions2 = []
        self.Answers = []
        self.Answers2 = []
        # 调用圆形图片控件
        self.label = CircleImage(self, 200, 200)
        self.label.set_image(QPixmap('./static/avatar.png'))
        self.label.move(40, 60)

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
            self.add_record("我", search_text, False, 0)
            # 清空文本框中的消息
            self.lineEdit.setText('')

            # 生成回答
            answer = self.Process(search_text)
            #answer = [['Character', '毁灭', '雅利洛-VI', '/', '克拉拉', 'https://uploadstatic.mihoyo.com/sr-wiki/2023/03/09/187636729/6b0b412b079a5610d34c2d87a9faf665_5273843714696308389.png', '四星', '物理']]
            # 记录回答内容
            self.Answers.append(answer)
            self.add_record("Robot", answer, True, 0)
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
            self.add_record("我", search_text, False, 1)
            # 清空文本框中的消息
            self.lineEdit.setText('')
            # 生成回答
            answer = GPT(search_text)
            # 记录回答内容
            self.Answers2.append(answer)
            self.add_record("GPT", answer, True, 1)
        else:
            QMessageBox.information(self, "提示", "不能发送空消息！", QMessageBox.Ok)

    def add_record(self, character, content, ans, mode):
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
                spacer = QSpacerItem(50, 30)
                displayLayout.addItem(spacer)
                displayLayout.addWidget(answerLabel)

                itemLayout.addLayout(displayLayout)
                itemWidget.setStyleSheet('background-color: #afdfe4; border-radius: 10px; margin: 5px;')
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
                text += "角色：" + mess_list[4]+"\n\n"
                text += "属性：" + mess_list[7] + "\n\n品质：" + mess_list[6] + "\n\n"
                text += "命途：" + mess_list[1] + "\n\n"
                text += "职业：" + mess_list[2] + "\n\n"
                text += "派别：" + mess_list[3]
                url = mess_list[5]
                print(url)
                return text, url
            case "Monster":
                text += "怪物名：" + mess_list[2] + "\n\n"
                text += "地域：" + mess_list[1] + "\n\n"
                text += "发现地：" + mess_list[4] + "\n\n"
                text += "类型：" + mess_list[5] + "\n\n"
                text += "抵抗：" + mess_list[7] + "\n\n"
                text += "描述：" + mess_list[8]
                url = mess_list[6]
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

        flag,ans = diversion(search_text)
        print(flag)
        print(ans)
        return flag,ans
        pass

    def EditInfo(self):
        """
        切换账户信息，需要爬虫实现
        """
        dialog = FormDialog()
        if dialog.exec_() == QDialog.Accepted:
            print("Form submitted successfully")
            print("%s\n%s" % (dialog.UID, dialog.Password))
            """
            登录过程
            """

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
        self.setWindowTitle("输入信息以登录账户")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("UID：")
        self.line_edit = QLineEdit()
        self.label2 = QLabel("Password：")
        self.line_edit2 = QLineEdit()
        self.line_edit2.setEchoMode(QLineEdit.Password)
        self.submit_button = QPushButton("确定")
        self.submit_button.clicked.connect(self.submit_form)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.line_edit2)
        self.layout.addWidget(self.submit_button)

    def submit_form(self):
        self.UID = self.line_edit.text()
        self.Password = self.line_edit2.text()
        # 在这里执行提交表单的逻辑，可以将数据发送到后端或执行其他操作
        self.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建对象
    robot = ChatRobot()
    robot.setFixedSize(1207, 792)
    # 加载QSS样式表
    style_file = 'ui.qss'
    style_sheet = QSSLoader.read_qss_file(style_file)
    robot.setStyleSheet(style_sheet)
    # 创建窗口
    robot.show()
    # 进入程序的主循环
    sys.exit(app.exec_())