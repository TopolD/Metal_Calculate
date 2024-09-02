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
        self.get_weight_and_tech_card()

    def DisplayTablesForInputData(self):
        self.DisplayExternalElementMaterials()
        self.DisplayExternalDetailsCoreWire()

    def DisplayExternalElementMaterials(self):
        self.label_2.setText('C')
        self.label_3.setText('Si')
        self.label_4.setText('Mn')
        self.label_5.setText('Cr')
        self.label_6.setText('Ni')
        self.label_7.setText('Cu')
        self.label_8.setText('Mo')
        self.label_9.setText('V')
        self.label_10.setText('Nb')
        self.label_11.setText('B')
        self.label_12.setText('Другое')

    def DisplayExternalDetailsCoreWire(self):
        self.label_40.setText('C')
        self.label_43.setText('Al')
        self.label_41.setText('Ti')
        self.label_42.setText('t,°C/S')

    def replace_label(self, value):
        self.data_tech_card(value)

        for attr_key, attr_value in value.items():
            if self.label_5.text() != attr_key:
                self.hide_layout(self._Cr)
            if self.label_6.text() != attr_key:
                self.hide_layout(self._Ni)
            if self.label_7.text() != attr_key:
                self.hide_layout(self._Cu)
            if self.label_8.text() != attr_key:
                self.hide_layout(self._Mo)
            if self.label_9.text() != attr_key:
                self.hide_layout(self._V)
            if self.label_10.text() != attr_key:
                self.hide_layout(self._Nb)
            if self.label_11.text() != attr_key:
                self.hide_layout(self._B)

    def hide_layout(self, layout):
        if layout is not None:
            for i in range(layout.count()):
                item = layout.itemAt(i)
                widget = item.widget()
                if widget is not None:
                    widget.hide()
                else:
                    self.hide_layout(item.layout())

    def data_tech_card(self, value):
        self.label_244.setText(value.get('FuseName'))
        self.label_246.setText(value.get('TempVd'))
        self.label_248.setText(value.get('Temp_ccm1'))
        self.label_249.setText(value.get('Temp_ccm2'))

    def get_weight_and_tech_card(self):
        self.lineEdit_67.setValidator(QIntValidator(0, 999))
        self.lineEdit_67.editingFinished.connect(self.update_label)

        self.lineEdit_68.setValidator(QDoubleValidator(0, 200, 1))
        self.lineEdit_68.editingFinished.connect(self.update_label)

    def update_label(self):
        DataHolder.set_data(self.lineEdit_67.text(), None)
        Fuse = GetDataCalculate()
        return self.replace_label(Fuse.get_data_fuse())

    @staticmethod
    def check_for_values(value, constant):
        if value < 0:
            constant.setStyleSheet("background-color: #FFA5A5;")
            constant.setText('ALARM')
        else:
            constant.setStyleSheet("background-color: #C2FFAE;")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = DisplayWindow()
    MainWindow.show()
    sys.exit(app.exec_())
