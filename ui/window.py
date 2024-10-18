from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from ui.EventHandlerForDisplay import DisplayHandler


class Window1(DisplayHandler):
    def __init__(self, main_window):
        super(Window1, self).__init__()
        self.setWindowTitle('Calculate - Lrf1')
        self.main_window = main_window
        self.pushButton_2.clicked.connect(self.switch_to_window_2)

    def switch_to_window_2(self):
        self.hide()
        self.main_window.show_window_2()

#
# class Window2(DisplayWindow):
#     def __init__(self, main_window):
#         super(Window2, self).__init__()
#         self.setWindowTitle('Calculate - Lrf2')
#         self.main_window = main_window
#         self.pushButton.clicked.connect(self.switch_to_window_1)
#
#     def switch_to_window_1(self):
#         self.hide()
#         self.main_window.show_window_1()
#
#
# class Window3(DisplayWindow):
#     def __init__(self, main_window):
#         super(Window3, self).__init__()
#         self.setWindowTitle('Calculate - Разбавление')
#         self.main_window = main_window
#         self.pushButton_3.clicked.connect(self.switch_to_window_3)
#
#     def switch_to_window_3(self):
#         self.hide()
#         self.main_window.show_window_3()
#
#
# class Window4(DisplayWindow):
#     def __init__(self, main_window):
#         super(Window4, self).__init__()
#         self.setWindowTitle('Calculate - Формулы')
#         self.main_window = main_window
#         self.pushButton_4.clicked.connect(self.switch_to_window_4)
#
#     def switch_to_window_4(self):
#         self.hide()
#         self.main_window.show_window_4()
#
#
# class Window5(DisplayWindow):
#     def __init__(self, main_window):
#         super(Window5, self).__init__()
#         self.setWindowTitle('Calculate - Заметки')
#         self.main_window = main_window
#         self.pushButton_5.clicked.connect(self.switch_to_window_5)
#
#     def switch_to_window_5(self):
#         self.hide()
#         self.main_window.show_window_5()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Main Window')

        self.lrf1 = Window1(self)
        self.lrf2 = Window2(self)
        self.lrf3 = Window3(self)
        self.lrf4 = Window4(self)
        self.lrf5 = Window5(self)

    def show_window_1(self):
        self.lrf1.show()

    def show_window_2(self):
        self.lrf2.show()

    def show_window_3(self):
        self.lrf3.show()

    def show_window_4(self):
        self.lrf4.show()

    def show_window_5(self):
        self.lrf5.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow()

    main_window.show_window_1()

    sys.exit(app.exec_())
