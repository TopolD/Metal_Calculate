from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox

from ui.Designe.DeleteDb import Ui_DialogDelete_Db
from utils_db.services import get_instance


class Dialog_Del(QDialog, Ui_DialogDelete_Db):

    def __init__(self):
        super(Dialog_Del, self).__init__()
        self.setupUi(self)

        self.ComboBox_For_DbModels.setCurrentText("КоэфУсв")

        self.buttonBox.accepted.disconnect()
        self.buttonBox.accepted.connect(self.handler_del_data)

    def handler_del_data(self):
        current_box = self.ComboBox_For_DbModels.currentText()

        data = {'search_criteria': {'Name': self.lineEdit_for_delete.text()}}
        match current_box:

            case 'КоэфУсв':
                instance = get_instance('AbsorptionRate', value_for_update=data)
                self.handle_entity_creation(data, instance)

            case 'ХимСостав':

                instance = get_instance('ChemicalComposition', value_for_update=data)
                self.handle_entity_creation(data, instance)

            case 'Проволока':

                instance = get_instance('CoredWire', value_for_update=data)
                self.handle_entity_creation(data, instance)
            case 'Марка':
                instance = get_instance('Fuse', value_for_update=data)
                self.handle_entity_creation(data, instance, check=False)

    def handle_entity_creation(self, data, instance, check=True):
        if check is True:
            if instance._delete_entity() is None:
                QMessageBox.information(self, "Успех", f"Материал: {data['search_criteria']['Name']} успешно удален!",
                                        QMessageBox.Ok)
                self.accept()
            else:
                QMessageBox.warning(self, 'Ошибка', f'Такие данные: {data['search_criteria']['Name']} , не существуют')
        else:
            if instance._delete_entity() is None:
                QMessageBox.information(self, "Успех", f"Марка: {data['search_criteria']['Name']} успешно удалена!",
                                        QMessageBox.Ok)
                self.accept()
            else:
                QMessageBox.warning(self, 'Ошибка', f'Такая Марка: {data['search_criteria']['Name']} , не существует')

    def close(self):
        self.reject()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main_window = Dialog_Del()
    main_window.show()

    sys.exit(app.exec_())
