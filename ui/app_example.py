from idlelib.autocomplete import TRY_A

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

    def Processor_of_material_data_at_the_time_of_entry(self, DataMaterials: dict):

        self.toggle_all_material_widgets(visible=False)

        for attr_key in DataMaterials.keys():
            self.toggle_specific_material_widget(attr_key, visible=True)

    def toggle_specific_material_widget(self, material, visible=True):
        layout_map = {
            'Cr': self._Cr,
            'Ni': self._Ni,
            'Cu': self._Cu,
            'Mo': self._Mo,
            'V': self._V,
            'Nb': self._Nb,
            'B': self._B
        }

        layout = layout_map.get(material)
        if layout:
            self.toggle_widgets_in_layout(layout, visible)

    def toggle_all_material_widgets(self, visible=False):

        for layout in [self._Cr, self._Ni, self._Cu, self._Mo, self._V, self._Nb, self._B]:
            self.toggle_widgets_in_layout(layout, visible)

    def toggle_widgets_in_layout(self, layout, visible=True):
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget = item.widget()
            if widget is not None:
                widget.setVisible(visible)

    @staticmethod
    def verification_conditions(operator, value):
        if operator:
            value.setVisible(True)
        else:
            value.setVisible(False)

    def update_label(self):
        DataHolder.set_data(self.lineEdit_67.text(), None)
        FuseData = GetDataCalculate()
        Fuse = FuseData.get_data_fuse()
        self.Processor_of_material_data_at_the_time_of_entry(Fuse)
        return self.data_tech_card(Fuse)

    @staticmethod
    def check_for_values(value, constant):
        if value < 0:
            constant.setStyleSheet("border-bottom: 2px solid #FF3B30;")
            constant.setText('ALARM')
        else:
            constant.setStyleSheet("border-bottom: 2px solid #34C759;")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = DisplayWindow()
    MainWindow.show()
    sys.exit(app.exec_())
