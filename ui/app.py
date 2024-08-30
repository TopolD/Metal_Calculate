from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from Gui import *
from utils_calculate.Formuls_example import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.get_weight_and_tech_card()
        self.get_sample_and_set_material()
        self.material()
        self.CoreWire()

    def DisplayExternalDetailsCoreWire(self):
        self.label_34.setText('C')
        self.label_35.setText('Al')
        self.label_36.setText('Ti')
        self.label_37.setText('t,°C/S ')

    def DisplayExternalDetailsMaterials(self):
        self.label_2.setText('C')
        self.label_3.setText('Si')
        self.label_4.setText('Mn')
        self.label_5.setText('Cr')

    def get_weight_and_tech_card(self):
        self.lineEdit_67.setValidator(QIntValidator(0, 999))
        self.lineEdit_67.editingFinished.connect(self.update_label)

        self.lineEdit_68.setValidator(QDoubleValidator(0, 200, 1))
        self.lineEdit_68.editingFinished.connect(self.update_label)

    def get_sample_and_set_material(self):
        self.lineEdit_1.setValidator(QDoubleValidator(0, 10, 2))
        self.lineEdit_2.setValidator(QDoubleValidator(0.0, 10, 2))
        self.lineEdit_3.setValidator(QDoubleValidator(0.0, 10, 2))
        self.lineEdit_3.editingFinished.connect(self.set_material_weight)

    def get_replace_material_weight(self):

        Data = {
            'Tcn': self.lineEdit_67.text(),
            'W': self.lineEdit_68.text().replace(',', '.'),
            'samples': {
                'C': self.lineEdit_1.text().replace(',', '.'),
                'Si': self.lineEdit_2.text().replace(',', '.'),
                'Mn': self.lineEdit_3.text().replace(',', '.'),
            },
            'material': {
                'C': self.comboBox.currentText(),
                'Si': self.comboBox_5.currentText(),
                'Mn': self.comboBox_3.currentText()
            }

        }
        DataMaterial = DataHolder.set_data(self.lineEdit_67.text(), Data)
        CalculateMaterial = DataMaterial.gather_materials()
        return CalculateMaterial

    @staticmethod
    def check_for_values(value, constant):
        if value < 0:
            constant.setStyleSheet("background-color: #FFA5A5;")
            constant.setText('ALARM')
        else:
            constant.setStyleSheet("background-color: #C2FFAE;")

    @QtCore.pyqtSlot()
    def set_material_weight(self):

        DataMaterials = self.get_replace_material_weight()
        self.label_24.setText(str(DataMaterials.get('C')))
        self.label_25.setText(str(DataMaterials.get('Si')))
        self.label_26.setText(str(DataMaterials.get('Mn')))

        self.check_for_values(int(self.label_24.text()), self.label_24)
        self.check_for_values(int(self.label_25.text()), self.label_25)
        self.check_for_values(int(self.label_26.text()), self.label_26)

    def show_notification(self, message):
        self.notification_label = QLabel(message, self)
        self.notification_label.setStyleSheet("background-color: #FFA5A5; ;border-radius: 5%")

        self.notification_label.setGeometry(60, 60, 232, 20)
        self.notification_label.show()

        QTimer.singleShot(5000, self.notification_label.hide)

    @QtCore.pyqtSlot()
    def update_label(self):
        try:
            value = GetDataCalculate(self.lineEdit_67.text(), None)
            Fuse = value.get_data_fuse()
            self.label_244.setText(Fuse.get('FuseName'))
            self.label_246.setText(Fuse.get('TempVd'))
            self.label_248.setText(Fuse.get('Temp_ccm1'))
            self.label_249.setText(Fuse.get('Temp_ccm2'))

            self.label_254.setText(Fuse.get('C', 'N/A'))
            self.label_255.setText(Fuse.get('Al', 'N/A'))
            self.label_256.setText(Fuse.get('Ti', 'N/A'))

            self.label_269.setText(Fuse.get('C', 'N/A'))
            self.label_270.setText(Fuse.get('Si', 'N/A'))
            self.label_271.setText(Fuse.get('Mn', 'N/A'))
            self.label_272.setText(Fuse.get('Cr', 'N/A'))
        except Exception:
            self.show_notification(f'Ошибка: не существует такая тех карта {self.lineEdit_67.text()}')
        finally:
            self.lineEdit_67.setFocus()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
