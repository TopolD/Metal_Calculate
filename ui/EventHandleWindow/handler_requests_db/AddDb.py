from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLayout, QMessageBox

from ui.Designe.CreateDb import Ui_DialogCreate_Db
from utils_db.services import get_instance


class Dialog_Add(QDialog, Ui_DialogCreate_Db):

    def __init__(self):
        super(Dialog_Add, self).__init__()
        self.setupUi(self)

        self.ComboBox_For_DbModels.setCurrentText("КоэфУсв")
        self.show_hide_layout('Layout_for_fuse_form', False)
        self.show_hide_layout('chemical_comp_for_fuse', False)

        self.ComboBox_For_DbModels.currentIndexChanged.connect(self.handler_combobox_change)

        self.buttonBox.accepted.disconnect()
        self.buttonBox.accepted.connect(self.add_data_in_db)

        self.process_data = {
            'FuseModel': {
                'Fuse': {'Tcn': self.input_Tcn.text(),
                         'Name': self.Input_FuseName.text(),
                         'TempVd': self.Input_TempVd.text(),
                         'Temp_ccm1': self.Input_Temp_ccm1.text(),
                         'Temp_ccm2': self.Input_Temp_ccm2.text(),
                         },
                'FuseTarget': {
                    'Fuse': None,
                    'Tcn': self.input_Tcn.text(),
                    'C': self.get_float_value(self.Inut_C_for_Fus_db),
                    'Mn': self.get_float_value(self.Inut_Mn_for_Fus_db),
                    'Si': self.get_float_value(self.Inut_Si_for_Fus_db),
                    'Cr': self.get_float_value(self.Inut_Cr_for_Fus_db),
                    'Ti': self.get_float_value(self.Inut_Ti_for_Fus_db),
                    'V': self.get_float_value(self.Inut_V_for_Fus_db),
                    'Mo': self.get_float_value(self.Inut_Mo_for_Fus_db),
                    'B': self.get_float_value(self.Inut_B_for_Fus_db),
                    'Nb': self.get_float_value(self.Inut_Nb_for_Fus_db),
                    'Ni': self.get_float_value(self.Inut_Ni_for_Fus_db),
                    'Cu': self.get_float_value(self.Inut_Cu_for_Fus_db),
                    'Al': self.get_float_value(self.Inut_Al_for_Fus_db),
                    'S': self.get_float_value(self.Inut_S_for_Fus_db),
                    'Ca': self.get_float_value(self.Inut_Ca_for_Fus_db),
                    'Cpr': self.get_float_value(self.Inut_Cpr_for_Fus_db),
                }
            },
            'Chemical': {
                'Name': self.Inut_name_db.text(),
                'C': self.get_float_value(self.Inut_C_db),
                'Mn': self.get_float_value(self.Inut_Mn_db),
                'Si': self.get_float_value(self.Inut_Si_db),
                'Cr': self.get_float_value(self.Inut_Cr_db),
                'Ti': self.get_float_value(self.Inut_Ti_db),
                'V': self.get_float_value(self.Inut_V_db),
                'Mo': self.get_float_value(self.Inut_Mo_db),
                'B': self.get_float_value(self.Inut_B_db),
                'Nb': self.get_float_value(self.Inut_Nb_db),
                'Ni': self.get_float_value(self.Inut_Ni_db),
                'Cu': self.get_float_value(self.Inut_Cu_db),
                'Al': self.get_float_value(self.Inut_Al_db),
                'S': self.get_float_value(self.Inut_S_db),
                'Fe': self.get_float_value(self.Inut_Fe_db),
                'Ca': self.get_float_value(self.Inut_Ca_db),
                'P': self.get_float_value(self.Inut_P_db),
            }

        }

    def handler_combobox_change(self):
        current_box = self.ComboBox_For_DbModels.currentText()

        match current_box:
            case 'КоэфУсв' | 'ХимСостав' | 'Проволока':
                self.show_hide_layout('chemical_comp', True)
                self.show_hide_layout('Layout_for_fuse_form', False)
                self.show_hide_layout('chemical_comp_for_fuse', False)

            case 'Марка':
                self.show_hide_layout('chemical_comp', False)
                self.show_hide_layout('Layout_for_fuse_form', True)
                self.show_hide_layout('chemical_comp_for_fuse', True)

            case _:
                self.show_hide_layout('chemical_comp', False)
                self.show_hide_layout('Layout_for_fuse_form', True)

    def show_hide_layout(self, layout_name, visible):
        layout = getattr(self, layout_name, None)
        if layout:
            self._set_layout_visibility(layout, visible)

    def _set_layout_visibility(self, layout, visible):
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if isinstance(item.widget(), QWidget):
                item.widget().setVisible(visible)
            elif isinstance(item.layout(), QLayout):
                self._set_layout_visibility(item.layout(), visible)

    def get_float_value(self, input_field):
        try:
            return float(input_field.text()) if input_field.text() else 0.0
        except ValueError:
            return 0.0

    def add_data_in_db(self):

        current_box = self.ComboBox_For_DbModels.currentText()
        self.process_data = {
            'FuseModel': {
                'Fuse': {'Tcn': self.input_Tcn.text(),
                         'Name': self.Input_FuseName.text(),
                         'TempVd': self.Input_TempVd.text(),
                         'Temp_ccm1': self.Input_Temp_ccm1.text(),
                         'Temp_ccm2': self.Input_Temp_ccm2.text(),
                         },
                'FuseTarget': {
                    'Fuse': None,
                    'Tcn': self.input_Tcn.text(),
                    'C': self.get_float_value(self.Inut_C_for_Fus_db),
                    'Mn': self.get_float_value(self.Inut_Mn_for_Fus_db),
                    'Si': self.get_float_value(self.Inut_Si_for_Fus_db),
                    'Cr': self.get_float_value(self.Inut_Cr_for_Fus_db),
                    'Ti': self.get_float_value(self.Inut_Ti_for_Fus_db),
                    'V': self.get_float_value(self.Inut_V_for_Fus_db),
                    'Mo': self.get_float_value(self.Inut_Mo_for_Fus_db),
                    'B': self.get_float_value(self.Inut_B_for_Fus_db),
                    'Nb': self.get_float_value(self.Inut_Nb_for_Fus_db),
                    'Ni': self.get_float_value(self.Inut_Ni_for_Fus_db),
                    'Cu': self.get_float_value(self.Inut_Cu_for_Fus_db),
                    'Al': self.get_float_value(self.Inut_Al_for_Fus_db),
                    'S': self.get_float_value(self.Inut_S_for_Fus_db),
                    'Ca': self.get_float_value(self.Inut_Ca_for_Fus_db),
                    'Cpr': self.get_float_value(self.Inut_Cpr_for_Fus_db),
                }
            },
            'Chemical': {
                'Name': self.Inut_name_db.text(),
                'C': self.get_float_value(self.Inut_C_db),
                'Mn': self.get_float_value(self.Inut_Mn_db),
                'Si': self.get_float_value(self.Inut_Si_db),
                'Cr': self.get_float_value(self.Inut_Cr_db),
                'Ti': self.get_float_value(self.Inut_Ti_db),
                'V': self.get_float_value(self.Inut_V_db),
                'Mo': self.get_float_value(self.Inut_Mo_db),
                'B': self.get_float_value(self.Inut_B_db),
                'Nb': self.get_float_value(self.Inut_Nb_db),
                'Ni': self.get_float_value(self.Inut_Ni_db),
                'Cu': self.get_float_value(self.Inut_Cu_db),
                'Al': self.get_float_value(self.Inut_Al_db),
                'S': self.get_float_value(self.Inut_S_db),
                'Fe': self.get_float_value(self.Inut_Fe_db),
                'Ca': self.get_float_value(self.Inut_Ca_db),
                'P': self.get_float_value(self.Inut_P_db),
            }

        }

        self.handler_add_data(current_box)

    def handler_add_data(self, current_box):
        match current_box:
            case 'КоэфУсв':
                data = self.process_data['Chemical']
                instance = get_instance('AbsorptionRate', data)
                self.handle_entity_creation(data, instance)

            case 'ХимСостав':
                data = self.process_data['Chemical']
                instance = get_instance('ChemicalComposition', data)
                self.handle_entity_creation(data, instance)

            case 'Проволока':
                data = self.process_data['Chemical']
                instance = get_instance('CoredWire', data)
                self.handle_entity_creation(data, instance)
            case 'Марка':
                data = self.process_data['FuseModel']
                instance = get_instance('Fuse', data)
                self.handle_entity_creation(data, instance, check=False, )

    def handle_entity_creation(self, data, instance, check=True, ):
        if check is True:
            result = instance._create_entity()
            if result is None:
                QMessageBox.information(self, "Успех", f"Материал: {data['Name']} успешно добавлен!",
                                        QMessageBox.Ok)
                self.accept()
            else:
                QMessageBox.warning(self, 'Ошибка', f'Такие данные: {data['Name']} , уже существуют')
        else:
            result = instance._create_entity()
            if result is None:
                QMessageBox.information(self, "Успех", f"Марка: {data['Fuse']['Tcn']} успешно добавлена!",
                                        QMessageBox.Ok)
                self.accept()
            else:
                QMessageBox.warning(self, 'Ошибка', f'Такая Тех-карта: {data['Fuse']['Tcn']} , уже существует')

    def close(self):
        self.reject()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main_window = Dialog_Add()
    main_window.show()

    sys.exit(app.exec_())
