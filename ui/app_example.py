from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from Lrf1 import *
from utils_calculate.Formuls_example import *
from Gui import *


class DisplayWindow(QWidget, Ui_LRF1_Widget):
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
        self.label_14.setText(str(value.get('C', 'N/A')))
        self.label_15.setText(str(value.get('Si', 'N/A')))
        self.label_16.setText(str(value.get('Mn', 'N/A')))
        self.label_17.setText(str(value.get('Cr', 'N/A')))
        self.label_18.setText(str(value.get('Ni', 'N/A')))
        self.label_19.setText(str(value.get('Cu', 'N/A')))
        self.label_20.setText(str(value.get('Mo', 'N/A')))
        self.label_21.setText(str(value.get('V', 'N/A')))
        self.label_22.setText(str(value.get('Nb', 'N/A')))
        self.label_23.setText(str(value.get('B', 'N/A')))
        self.label_24.setText('-')

        self.label_45.setText(str(value.get('Cpr', 'N/A')))
        self.label_48.setText(str(value.get('Al', 'N/A')))
        self.label_46.setText(str(value.get('Ti', 'N/A')))

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


# переделать под чистый код
class Window1(DisplayWindow):
    def __init__(self, main_window):
        super(Window1, self).__init__()
        self.setWindowTitle('Calculate - Lrf1')
        self.main_window = main_window
        self.pushButton_2.clicked.connect(self.switch_to_window_2)

    def switch_to_window_2(self):
        self.hide()
        self.main_window.show_window_2()


class Window2(DisplayWindow):
    def __init__(self, main_window):
        super(Window2, self).__init__()
        self.setWindowTitle('Calculate - Lrf2')
        self.main_window = main_window
        self.pushButton.clicked.connect(self.switch_to_window_1)

    def switch_to_window_1(self):
        self.hide()
        self.main_window.show_window_1()


class Window3(DisplayWindow):
    def __init__(self, main_window):
        super(Window3, self).__init__()
        self.setWindowTitle('Calculate - Разбавление')
        self.main_window = main_window
        self.pushButton_3.clicked.connect(self.switch_to_window_3)

    def switch_to_window_3(self):
        self.hide()
        self.main_window.show_window_3()


class Window4(DisplayWindow):
    def __init__(self, main_window):
        super(Window4, self).__init__()
        self.setWindowTitle('Calculate - Формулы')
        self.main_window = main_window
        self.pushButton_4.clicked.connect(self.switch_to_window_4)

    def switch_to_window_4(self):
        self.hide()
        self.main_window.show_window_4()


class Window5(DisplayWindow):
    def __init__(self, main_window):
        super(Window5, self).__init__()
        self.setWindowTitle('Calculate - Заметки')
        self.main_window = main_window
        self.pushButton_5.clicked.connect(self.switch_to_window_5)

    def switch_to_window_5(self):
        self.hide()
        self.main_window.show_window_5()


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
