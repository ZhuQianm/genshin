# 制 作 人：祝金宝
# 制作时间：2022/7/3 9:48
# 制作用途：仅学习（不负任何责任）

import pyautogui
import time
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("轩专用")
        self.resize(500, 500)
        self.MyTextA()

    def MyTextA(self):
        label1 = QLabel(self)
        label1.move(5, 5)
        label1.resize(100, 15)
        label1.setText("—这里是坐标点——")

        label2 = QLabel(self)
        label2.move(200, 140)
        label2.resize(100, 15)
        label2.setText("这里是运行次数")

        label3 = QLabel(self)
        label3.move(200, 200)
        label3.resize(100, 15)
        label3.setText("这里是睡眠时间(s)")

        test1 = QTextEdit(self)
        test1.resize(100, 300)
        test1.move(5, 20)

        test2 = QTextEdit(self)
        test2.resize(70, 50)
        test2.move(120, 140)

        test3 = QTextEdit(self)
        test3.resize(70, 50)
        test3.move(120, 200)

        button1 = QPushButton(self)
        button1.resize(70, 50)
        button1.setText("记录坐标")
        button1.move(120, 20)

        button2 = QPushButton(self)
        button2.resize(70, 50)
        button2.setText("开始强化")
        button2.move(120, 80)

        def clickbuttion1():
            a = 2
            list1 = []
            time.sleep(int(a))
            list1 = pyautogui.position()
            str1 = str(list1[0]) + ',' + str(list1[1])
            test1.append(str1)

        button1.clicked.connect(clickbuttion1)

        def clickbuttion2():
            a = test1.toPlainText()
            numb = test2.toPlainText()
            if numb is None:
                numb = 200
            else:
                numb = int(numb)
            num2 = test3.toPlainText()
            if num2 is None:
                num2 = 2
            else:
                num2 = int(num2)
            a = a.split('\n')
            i = 0
            while i < numb:
                i = i + 1
                for item in a:
                    b = item.split(',')
                    pyautogui.click(int(b[0]), int(b[1]), 1)
                    time.sleep(num2)
        button2.clicked.connect(clickbuttion2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())
