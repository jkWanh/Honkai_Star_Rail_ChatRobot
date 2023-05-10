from ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
import sys
import time
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QMovie, QPixmap
from PyQt5.QtWidgets import QMainWindow, QSplashScreen

class MySplashScreen(QSplashScreen):
    def __init__(self):
        super(MySplashScreen, self).__init__()

        # 新建动画
        self.movie = QMovie(r'pictures/qi.gif')
        self.movie.frameChanged.connect(lambda: self.setPixmap(self.movie.currentPixmap()))
        self.movie.start()

    def mousePressEvent(self, QMouseEvent):
        pass


class LoadDataWorker(QObject):
    finished = pyqtSignal()
    message_signal = pyqtSignal(str)

    def __init__(self):
        super(LoadDataWorker, self).__init__()

    def run(self):
        for i in range(10):
            time.sleep(0.40)
        self.finished.emit()


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self, splash):
        super(Form, self).__init__()
        self.resize(800, 600)

        self.splash = splash

        self.load_thread = QThread()
        self.load_worker = LoadDataWorker()
        self.load_worker.moveToThread(self.load_thread)
        self.load_thread.started.connect(self.load_worker.run)
        self.load_worker.message_signal.connect(self.set_message)
        self.load_worker.finished.connect(self.load_worker_finished)
        self.load_thread.start()

        while self.load_thread.isRunning():
            QtWidgets.qApp.processEvents()  # 不断刷新，保证动画流畅

        self.load_thread.deleteLater()
        self.setupUi(self)
    def load_worker_finished(self):
        self.load_thread.quit()
        self.load_thread.wait()

    def set_message(self, message):
        self.splash.showMessage(message, Qt.AlignLeft | Qt.AlignBottom, Qt.white)

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
    splash = MySplashScreen()
    splash.setPixmap(QPixmap(r'pictures/qi.gif'))  # 设置背景图片
    splash.show()
    app.processEvents()  # 处理主进程，不卡顿
    form = Form(splash)
    form.show()
    splash.finish(form)  # 主界面加载完成后隐藏
    splash.movie.stop()  # 停止动画
    splash.deleteLater()
    app.exec_()
    # 进入程序的主循环
    sys.exit(app.exec_())
