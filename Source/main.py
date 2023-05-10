from ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
import sys


class ChatRobot(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(ChatRobot, self).__init__()
        self.setupUi(self)

    def Query(self):
        """
        此函数用于接收用户的查询内容，即search_text
        传给函数Process进行关键词提取等处理
        """
        search_text = self.lineEdit.text()
        # answer = Process(search_text)
        answer = "回复测试"
        # 创建消息控件，并添加到聊天历史记录控件中
        item = QListWidgetItem(answer)

        # 将消息控件添加到聊天历史记录控件中
        self.listWidget.addItem(item)
        self.listWidget.scrollToBottom()

        # 清空文本框中的消息
        self.lineEdit.setText('')

    def Process(self, search_text):
        """
        此函数用于处理用户的原始查询输入，关键字提取等，可调用其他学生
        """
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建对象
    robot = ChatRobot()
    # 创建窗口
    robot.show()
    # 进入程序的主循环
    sys.exit(app.exec_())
