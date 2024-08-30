from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from Gui import *
from utils_calculate.Formuls_example import *


class DisplayWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(DisplayWindow, self).__init__()
        self.setupUi(self)
        self.DisplayTablesForInputData()

    def DisplayTablesForInputData(self):
        self.DisplayExternalDetailsMaterials()
        self.DisplayExternalDetailsCoreWire()

    def DisplayExternalDetailsMaterials(self):
        self.label_2.setText('C')
        self.label_3.setText('Si')
        self.label_4.setText('Mn')
        self.label_5.setText('Cr')

    def DisplayExternalDetailsCoreWire(self):
        self.label_34.setText('C')
        self.label_35.setText('Al')
        self.label_36.setText('Ti')
        self.label_37.setText('t,°C/S')

    @staticmethod
    def check_for_values(value, constant):
        if value < 0:
            constant.setStyleSheet("background-color: #FFA5A5;")
            constant.setText('ALARM')
        else:
            constant.setStyleSheet("background-color: #C2FFAE;")


class HandlerEvents(DisplayWindow):
    def __init__(self):
        super(HandlerEvents, self).__init__()

    def get_data_for_fuse(self):
        self.lineEdit_67.setValidator(QIntValidator(0, 999))
        self.lineEdit_67.editingFinished.connect(self.update_label)

        self.lineEdit_68.setValidator(QDoubleValidator(0, 200, 1))
        self.lineEdit_68.editingFinished.connect(self.update_label)

    def get_sample_and_set_material(self):
        self.lineEdit_1.setValidator(QDoubleValidator(0, 10, 2))
        self.lineEdit_2.setValidator(QDoubleValidator(0.0, 10, 2))
        self.lineEdit_3.setValidator(QDoubleValidator(0.0, 10, 2))
        self.lineEdit_3.editingFinished.connect(self.set_material_weight)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = DisplayWindow()
    MainWindow.show()
    sys.exit(app.exec_())
