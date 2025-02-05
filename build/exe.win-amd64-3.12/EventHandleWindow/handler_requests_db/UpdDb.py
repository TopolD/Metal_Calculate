from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QCheckBox, QHBoxLayout, QLineEdit, QMessageBox

from ui.Designe.UpdateDb import Ui_DialogUpdate_db
from utils_db.services import get_instance


class Dialog_Upd(QDialog, Ui_DialogUpdate_db):

    def __init__(self):
        super(Dialog_Upd, self).__init__()
        self.setupUi(self)

        self.ComboBox_For_DbModels.setCurrentText("КоэфУсв")
        self.methods_for_add_checkbox_in_sroll('КоэфУсв')
        self.ComboBox_For_DbModels.currentIndexChanged.connect(self.handler_combobox_change)

        self.hbox_list = []

        self.buttonBox.accepted.disconnect()
        self.buttonBox.accepted.connect(self.get_checked_inputs)

    def handler_combobox_change(self):
        current_box = self.ComboBox_For_DbModels.currentText()
        self.methods_for_add_checkbox_in_sroll(current_box)

    def methods_for_add_checkbox_in_sroll(self, current_box):
        list_for_material = ['Name', 'C', 'Mn', 'Si', 'Cr', 'Ti', 'V', 'Mo', 'B', 'Nb', 'Ni', 'Cu', 'Al', 'S', 'Fe',
                             'Ca', 'P']
        list_for_fuse = ['Tcn', 'Name', 'TempVd', 'Temp_ccm1', 'Temp_ccm2', 'C', 'Mn', 'Si', 'Cr', 'Ti', 'V', 'Mo', 'B',
                         'Nb', 'Ni', 'Cu', 'Al', 'S', 'Ca', 'Cpr']

        match current_box:

            case 'КоэфУсв':
                self.mechanic_hide_or_show_list(list_for_material)
            case 'ХимСостав':
                self.mechanic_hide_or_show_list(list_for_material)
            case 'Проволока':
                self.mechanic_hide_or_show_list(list_for_material)
            case 'Марка':
                self.mechanic_hide_or_show_list(list_for_fuse)
            case 'Целевые':
                self.mechanic_hide_or_show_list(list_for_fuse)

    def mechanic_hide_or_show_list(self, material_list):

        if hasattr(self, 'checkbox_lineedit_map'):
            for hbox, (checkbox, line_edit) in self.checkbox_lineedit_map.items():
                self.layout_for_all_checkbox.removeItem(hbox)
                checkbox.deleteLater()
                line_edit.deleteLater()
            self.checkbox_lineedit_map.clear()
        else:
            self.checkbox_lineedit_map = {}

        for name in material_list:
            hbox = QHBoxLayout()
            checkbox = QCheckBox(name)
            line_edit = QLineEdit()
            line_edit.setEnabled(False)

            checkbox.stateChanged.connect(lambda state, le=line_edit: le.setEnabled(state == Qt.Checked))

            hbox.addWidget(checkbox)
            hbox.addWidget(line_edit)

            self.checkbox_lineedit_map[hbox] = (checkbox, line_edit)

            self.layout_for_all_checkbox.addLayout(hbox)

    def get_checked_inputs(self):
        data = {'search_criteria': {},
                'update_data': {}
                }
        for hbox, (checkbox, line_edit) in self.checkbox_lineedit_map.items():
            if checkbox.isChecked():
                data['update_data'][checkbox.text()] = line_edit.text()
                data['search_criteria']['Name'] = data['update_data']['Name']
        self.update_data_in_db(data)

    def update_data_in_db(self, data):
        current_box = self.ComboBox_For_DbModels.currentText()
        current_data = data.copy()
        print(current_data, '1')
        match current_box:
            case 'КоэфУсв':

                self.handle_entity_creation(current_data, get_instance('AbsorptionRate', value_for_update=current_data))
            case 'ХимСостав':
                self.handle_entity_creation(current_data, get_instance('ChemicalComposition', value_for_update=current_data))

            case 'Проволока':

                self.handle_entity_creation(current_data, get_instance('CoredWire', value_for_update=current_data))

            case 'Марка':

                self.handle_entity_creation(current_data, get_instance('Fuse', value_for_update=current_data))

            case 'Целевые':

                self.handle_entity_creation(current_data, get_instance('FuseTarget', value_for_update=current_data))

    def handle_entity_creation(self, data, instance, check=True, ):
        if check is True:
            result = instance._update_entity()
            if result is None:
                QMessageBox.information(self, "Успех", f"Материал: {data['update_data'].get('Name')} успешно обновлен!",
                                        QMessageBox.Ok)
                self.accept()

        else:
            result = instance._update_entity()
            if result is None:
                QMessageBox.information(self, "Успех", f"Марка: {data['update_data'].get('Name')} успешно обновлена!",
                                        QMessageBox.Ok)
                self.accept()

    def close(self):
        self.reject()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main_window = Dialog_Upd()
    main_window.show()

    sys.exit(app.exec_())
