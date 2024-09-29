from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from Lrf1 import *
from utils_calculate.Formuls_example import *


class DisplayWindow(QWidget, Ui_LRF1_Widget):
    def __init__(self):
        super(DisplayWindow, self).__init__()

        self.setupUi(self)
        self.get_func()
        self.widget_2.setVisible(False)

        self.hidden_widget = self.findChild(QWidget, 'widget_2')
        self.show_button = self.findChild(QPushButton, 'pushButton_9')
        self.hide_button = self.findChild(QPushButton, 'pushButton_10')

        self.original_size = self.size()

        self.show_button.clicked.connect(self.show_widget)
        self.hide_button.clicked.connect(self.hide_widget)

    def show_widget(self):
        self.hidden_widget.show()
        self.adjustSize()

    def hide_widget(self):
        self.hidden_widget.hide()
        self.resize(self.original_size)

    def get_func(self):
        self.get_weight_and_tech_card()
        self.get_clear_data_for_button()

    def data_tech_card(self, value):
        self.label_82.setText(value.get('FuseName'))
        self.label_83.setText(value.get('TempVd'))
        self.label_84.setText(value.get('Temp_ccm1'))
        self.label_85.setText(value.get('Temp_ccm2'))
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
        self.pushButton_9.clicked.connect(self.clear_data_for_button)

    def clear_data_for_button(self):
        button = {
            'W': self.lineEdit_21,
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
        self.lineEdit.setValidator(QIntValidator(0, 999))
        self.lineEdit.editingFinished.connect(self.update_label)

        self.lineEdit_21.setValidator(QDoubleValidator(0.0, 200.0, 1))
        self.lineEdit_21.editingFinished.connect(self.update_label_wight)

    def update_label(self):
        try:
            DataHolder.set_data(self.lineEdit.text(), None)
            Fuse = GetDataCalculate().get_data_fuse()
            self.Processor_of_material_data_at_the_time_of_entry(Fuse)
            self.update_border_for_error(self.lineEdit, None)

            return self.data_tech_card(Fuse)
        except AttributeError as e:
            self.update_border_for_error(self.lineEdit, e)
        finally:
            self.lineEdit.setFocus()

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
