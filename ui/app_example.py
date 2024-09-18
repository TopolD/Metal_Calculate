from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from Lrf1 import *
from utils_calculate.Formuls_example import *


class DisplayWindow(QWidget, Ui_LRF1_Widget):
    def __init__(self):
        super(DisplayWindow, self).__init__()

        self.setupUi(self)
        self.DisplayTablesForInputData()
        self.get_func()

    def get_func(self):
        self.get_weight_and_tech_card()
        self.get_clear_data_for_button()
        self.get_data_with_line_edit()

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

    def get_clear_data_for_button(self):
        self.pushButton_11.clicked.connect(self.clear_data_for_button)

    def clear_data_for_button(self):
        button = {
            'W': self.lineEdit_68,
            'C': self.lineEdit_1,
            'Si': self.lineEdit_2,
            'Mn': self.lineEdit_3,
            'Cr': self.lineEdit_4,
            'Ni': self.lineEdit_5,
            'Cu': self.lineEdit_6,
            'Mo': self.lineEdit_7,
            'V': self.lineEdit_8,
            'Nb': self.lineEdit_9,
            'B': self.lineEdit_10,

        }

        for key, value in button.items():
            value.clear()

    def get_weight_and_tech_card(self):
        self.lineEdit_67.setValidator(QIntValidator(0, 999))
        self.lineEdit_67.editingFinished.connect(self.update_label)

    def update_label(self):
        try:
            DataHolder.set_data(self.lineEdit_67.text(), None)
            FuseData = GetDataCalculate()
            Fuse = FuseData.get_data_fuse()
            self.Processor_of_material_data_at_the_time_of_entry(Fuse)
            self.update_border_for_error(self.lineEdit_67, None)
            self.clear_data_for_button()
            return self.data_tech_card(Fuse)
        except AttributeError as e:
            self.update_border_for_error(self.lineEdit_67, e)
        finally:
            self.lineEdit_67.setFocus()

    def update_border_for_error(self, widget, error):
        style = self.get_error_stylesheet(error)
        widget.setStyleSheet(style)

        if error:
            widget.clear()
            self.animate_vibrate(widget)

    def get_error_stylesheet(self, error):
        if isinstance(error, AttributeError):
            return """
                QLineEdit{
                    background-color: rgb(255, 255, 255);
                    border: none;
                    border-bottom: 2px solid #FFA5A5;
                }
            """
        return """
            QLineEdit{
                background-color: rgb(255, 255, 255);
                border: none;
                border-bottom: 2px solid #E0E0E0;
            }
        """

    def animate_vibrate(self, widget):
        self.animation = QPropertyAnimation(widget, b"geometry")
        original_geometry = widget.geometry()
        self.animation.setDuration(200)
        self.animation.setKeyValueAt(0, original_geometry)
        self.animation.setKeyValueAt(0.25,
                                     QRect(original_geometry.x() - 10, original_geometry.y(), original_geometry.width(),
                                           original_geometry.height()))
        self.animation.setKeyValueAt(0.5, original_geometry)
        self.animation.setKeyValueAt(0.75,
                                     QRect(original_geometry.x() + 10, original_geometry.y(), original_geometry.width(),
                                           original_geometry.height()))
        self.animation.setKeyValueAt(1, original_geometry)
        self.animation.start()

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
    def check_for_values(value, constant):
        if value < 0:
            constant.setStyleSheet("border-bottom: 2px solid #FF3B30;")
            constant.setText('ALARM')
        else:
            constant.setStyleSheet("border-bottom: 2px solid #34C759;")
