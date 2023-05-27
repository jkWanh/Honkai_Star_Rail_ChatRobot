from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtWidgets import QDialog, QLineEdit, QFileDialog, QComboBox, QLabel, QVBoxLayout, QPushButton
from diversion import *


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
        self.setFixedSize(500, 600)
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
