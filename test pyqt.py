from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Test')
        self.setGeometry(100, 100, 350, 200)

        # ___________Текст______________________________
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Тест текста")
        self.main_text.move(120, 100)
        self.main_text.adjustSize()
        # _______________________________________________

        # ________Кнопка_________________________________
        self.butten1 = QtWidgets.QPushButton(self)
        self.butten1.move(70, 150)
        self.butten1.setText('Я кнопка')
        self.butten1.setFixedWidth(200)
        self.butten1.clicked.connect(self.KcikButten)
        # ________________________________________________

        #____Новый_обект__________________________________
        self.new_text = QtWidgets.QLabel(self)
        #_________________________________________________

        #новый метод
    def KcikButten(self):
        self.new_text.setText("Привет я новый текст")
        self.new_text.move(120,90)
        self.new_text.adjustSize() #нормальный размер текста

#основное окно
def application():
    app = QApplication(sys.argv)
    Win = Window()


    Win.show()
    sys.exit(app.exec_())





if __name__=="__main__":
    application()