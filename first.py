import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import uic
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        uic.loadUi('UI.ui', self)

        self.btn.clicked.connect(self.paint)

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(70, 150)
        self.do_paint = False


    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.x = random.randrange(0, 100)
        self.y = random.randrange(0, 100)
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        qp.setPen(QColor(255, 255, 0))
        qp.drawEllipse(30, 30, self.x, self.x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())