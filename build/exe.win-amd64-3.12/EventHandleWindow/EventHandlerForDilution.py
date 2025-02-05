
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QWidget, QApplication

from ui.Designe.Dilution import Ui_Dilution_Widget


class DisplayHandlerDilution(QWidget, Ui_Dilution_Widget):
    def __init__(self):
        super(DisplayHandlerDilution, self).__init__()
        self.setupUi(self)

        self.dilution_dict = self.initial_dict()
        self.line_edit_handler()


    def initial_dict(self):
        dilution_dict = {
            'Ladles': {
                'Ladle_1': {},
                'Ladle_2': {},
                'Ladle_3': {},
            }
        }
        return dilution_dict

    def line_edit_handler(self):
        self.Input_Weight_Ladle_1.setValidator(QDoubleValidator(0.0, 200, 1))
        self.Input_Weight_Ladle_2.setValidator(QDoubleValidator(0.0, 200, 1))
        self.Input_Weight_Ladle_3.setValidator(QDoubleValidator(0.0, 200, 1))
        self.Input_Weight_Ladle_1.editingFinished.connect(self.initial_label_for_dilution)

    def initial_label_for_dilution(self):
        Dilution_material_list = ['C', 'Si', 'Mn', 'Cu', 'Cr', 'Ti', 'Ni', 'P', 'V', 'Mo', 'Nb', 'Al', 'P']

        for list_value in Dilution_material_list:
            for value in range(1, 4):
                dilution_name = f'Ladel_{list_value}_N{value}'

                dilution_label = getattr(self, dilution_name, None)
                if dilution_label:
                    dilution_label.setValidator(QDoubleValidator(0.0, 4.0, 3))
                    dilution_label.editingFinished.connect(
                        lambda line_edit=dilution_label, mat=list_value: self.handler_input_dilution(line_edit,
                                                                                                     mat))

    def handler_input_dilution(self, line_edit, mat):
        input_value = line_edit.text()

        if input_value:
            ladle_index = int(line_edit.objectName().split('_')[-1].lstrip('N'))
            ladle_name = f'Ladle_{ladle_index}'

            self.dilution_dict['Ladles'][ladle_name][mat] = float(input_value.replace(',', '.'))
            weight_line_edit = getattr(self, f'Input_Weight_Ladle_{ladle_index}', None)
            self.dilution_dict['Ladles'][ladle_name]['W'] = float(weight_line_edit.text()) if weight_line_edit else 0.0
        self.calculate_weight()
        self.calculate_dilution_material(mat)

    def calculate_weight(self):
        weight = 0
        for ladle_key, ladle_data in self.dilution_dict.get('Ladles', {}).items():
            weight += ladle_data.get('W', 0)
        self.label.setText(str(weight))
        self.label.setStyleSheet(("""
                     border-bottom: 2px solid #BCFBA7;
                 """)
                                 )
        return weight

    def calculate_dilution_material(self, mat):
        total_dilution = 0
        total_weight = self.calculate_weight()

        for ladle_key, ladle_data in self.dilution_dict.get('Ladles', {}).items():
            material_concentration = ladle_data.get(mat, 0)
            weight = ladle_data.get('W', 0)
            total_dilution += material_concentration * weight
            total_dilution / total_weight

            Dil_name = f'Dil_{mat}_Label_Calc'
            Dil_label = getattr(self, Dil_name, None)
            result = round(total_dilution / total_weight, 3)
            Dil_label.setText(str(result))
            Dil_label.setStyleSheet(("""
                     border-bottom: 2px solid #BCFBA7;
                 """)
                                    )


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main_window = DisplayHandlerDilution()
    main_window.show()

    sys.exit(app.exec_())
