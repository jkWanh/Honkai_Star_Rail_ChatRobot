from PyQt5.QtWidgets import QApplication
import sys
from Robot import ChatRobot
from Tools import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建对象
    robot = ChatRobot()
    robot.setFixedSize(1408, 875)
    # 加载QSS样式表
    style_file = './Qss/ui.qss'
    style_sheet = QSSLoader.read_qss_file(style_file)
    robot.setStyleSheet(style_sheet)
    # 创建窗口
    robot.show()
    # 进入程序的主循环
    sys.exit(app.exec_())
