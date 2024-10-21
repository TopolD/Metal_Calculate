from types import NoneType

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QDoubleValidator, QIntValidator

from ui.Lrf import Ui_LRF1_Widget
from ui.calculate import CalculationHandler
from utils_calculate.formuls_for_calculate import DataHolder, get_data_calculate_with_db


class DisplayHandler(QWidget, Ui_LRF1_Widget):

    def __init__(self):
        super(DisplayHandler, self).__init__()
        self.setupUi(self)

        self.CalculateClass = handler_data(self)
        self.OutputClass = changing_field_values(self)

        self.InputClass = input_data_handler(self)

        self.button_handler_for_display()
        self.line_edit_handler_for_display()
        self.line_edit_initialize_for_calculate()

    def button_handler_for_display(self):
        pass

    def line_edit_handler_for_display(self):
        self.InputTechCard.setValidator(QIntValidator(0, 999))
        self.InputTechCard.editingFinished.connect(self.InputClass.handle_input)

        self.InputWeight.setValidator(QDoubleValidator(0.0, 200.0, 2))
        self.InputWeight.editingFinished.connect(self.CalculateClass.initialize_data_from_Weight)

    def line_edit_initialize_for_calculate(self, Right_Change=False):
        Initialize_Dict = {
            'C': self.LabelTargetForC,
            'Si': self.LabelTargetForSi,
            'Mn': self.LabelTargetForMn,
            'Cr': self.LabelTargetForCr,
            'Ni': self.LabelTargetForNi,
            'Cu': self.LabelTargetForCu,
            'Mo': self.LabelTargetForMo,
            'V': self.LabelTargetForV,
            'Nb': self.LabelTargetForNb,
            'B': self.LabelTargetForB
        }
        if Right_Change == False:
            self.LabelTargetForC.setValidator(QDoubleValidator(0.0, 0, 3))
            self.LabelTargetForSi.setValidator(QDoubleValidator(0.0, 0, 3))
            self.LabelTargetForMn.setValidator(QDoubleValidator(0.0, 0, 3))
            self.LabelTargetForCr.setValidator(QDoubleValidator(0.0, 0, 3))
            self.LabelTargetForNi.setValidator(QDoubleValidator(0.0, 0, 3))
            self.LabelTargetForCu.setValidator(QDoubleValidator(0.0, 0, 3))
            self.LabelTargetForMo.setValidator(QDoubleValidator(0.0, 0, 3))
            self.LabelTargetForV.setValidator(QDoubleValidator(0.0, 0, 3))
            self.LabelTargetForNb.setValidator(QDoubleValidator(0.0, 0, 3))
            self.LabelTargetForB.setValidator(QDoubleValidator(0.0, 0, 3))
        else:
            for attr_key, attr_value in Initialize_Dict.items():
                DataHolder.set_data(self.InputTechCard.text(), None)
                Fuse_Data = get_data_calculate_with_db().get_data_target_for_fuse()
                if attr_key in Fuse_Data:
                    Initialize_Dict[attr_key].setValidator(QDoubleValidator(0.0, Fuse_Data[attr_key], 3))
                    Initialize_Dict[attr_key].editingFinished.connect(
                        self.CalculateClass.InputDataForCalculate(attr_key))
                    self.setFocus(Initialize_Dict[attr_key])
                    break
                else:
                    yield


class input_data_handler:

    def __init__(self, parent):
        self.parent = parent

    def handle_input(self):
        tcn_value = self.parent.InputTechCard.text()

        self.initialize_tech_card(tcn_value)

    def initialize_tech_card(self, tcn_value):
        DataHolder.set_data(tcn_value, None)

        self.parent.OutputClass.output_label_for_fuse()
        self.parent.OutputClass.output_label_for_target_fuse()

    def initialize_samples_for_fuse(self):
        DisplayHandler().line_edit_initialize_for_calculate(Right_Change=True)


class changing_field_values:

    def __init__(self, parent):
        self.parent = parent

    def get_fuse_data(self):
        return input_data_handler(self.parent).handle_input()

    def output_label_for_fuse(self):
        FuseData = self.get_fuse_data_with_db()
        self.parent.SteelName.setText(FuseData['FuseName'])
        self.parent.TempForVd.setText(FuseData['TempVd'])
        self.parent.Mnlz1.setText(FuseData['Temp_ccm1'])
        self.parent.Mnlz2.setText(FuseData['Temp_ccm2'])

    def output_label_for_target_fuse(self):
        FuseData = self.get_fuse_data_target_with_db()

        elements_clean_dict = {
            'C': self.parent.LabelTargetForC,
            'Si': self.parent.LabelTargetForSi,
            'Mn': self.parent.LabelTargetForMn,
            'Cr': self.parent.LabelTargetForCr,
            'Ni': self.parent.LabelTargetForNi,
            'Cu': self.parent.LabelTargetForCu,
            'Mo': self.parent.LabelTargetForMo,
            'V': self.parent.LabelTargetForV,
            'Nb': self.parent.LabelTargetForNb,
            'B': self.parent.LabelTargetForB,
        }

        for AttrKeyDict, AttrValueDict in elements_clean_dict.items():
            if AttrKeyDict in FuseData:
                elements_clean_dict[AttrKeyDict].setText(str(FuseData[AttrKeyDict]))
                self.handler_visible_for_fuse_material_target(AttrKeyDict)
            else:
                self.handler_hiding_for_fuse_material_target(AttrKeyDict)

    def handle_widget_visibility_for_fuse_material_target(self, key, visible):
        layout_name = f'Layout{key}'
        layout = getattr(self.parent, layout_name, None)

        if layout:
            for i in range(layout.count()):
                widget = layout.itemAt(i).widget()
                if widget:
                    widget.setVisible(visible)

    def handler_visible_for_fuse_material_target(self, key):
        self.handle_widget_visibility_for_fuse_material_target(key, visible=True)

    def handler_hiding_for_fuse_material_target(self, key):
        self.handle_widget_visibility_for_fuse_material_target(key, visible=False)

    def get_fuse_data_with_db(self):
        return get_data_calculate_with_db().get_data_fuse()

    def get_fuse_data_target_with_db(self):
        return get_data_calculate_with_db().get_data_target_for_fuse()


class handler_data:
    def __init__(self, parent):
        self.parent = parent
        self.data_for_calculate = {
            'W': self.parent.InputWeight.text(),
            'samples': {},
            'material': {
                'C': self.parent.MaterialForC.currentText(),
                'Si': self.parent.MaterialForSi.currentText(),
                'Mn': self.parent.MaterialForMn.currentText(),
                'Cr': self.parent.MaterialForCr.currentText(),
                'Ni': self.parent.MaterialForNi.currentText(),
                'Cu': self.parent.MaterialForCu.currentText(),
                'Mo': self.parent.MaterialForMo.currentText(),
                'V': self.parent.MaterialForV.currentText(),
                'Nb': self.parent.MaterialForNb.currentText(),
                'B': self.parent.MaterialForB.currentText(),
            },
            'corewire':{}
        }

    def initialize_data_from_Weight(self):
        input_data_handler(self.parent).initialize_samples_for_fuse()
        if self.data_for_calculate is not None:
            self.initialize_data()
        else:
            raise NoneType

    def InputDataForCalculate(self, value):
        input_dict_data = {
            'C': self.parent.LabelTargetForC,
            'Si': self.parent.LabelTargetForSi,
            'Mn': self.parent.LabelTargetForMn,
            'Cr': self.parent.LabelTargetForCr,
            'Ni': self.parent.LabelTargetForNi,
            'Cu': self.parent.LabelTargetForCu,
            'Mo': self.parent.LabelTargetForMo,
            'V': self.parent.LabelTargetForV,
            'Nb': self.parent.LabelTargetForNb,
            'B': self.parent.LabelTargetForB
        }

        for attr_key, attr_value in input_dict_data.items():

            if attr_key == value:
                self.data_for_calculate['samples'].update({attr_key: float(attr_value.text())})

            else:
                yield
        return self.data_for_calculate

    def initialize_data(self):
        DataHolder.set_data(self.parent.InputTechCard.text(), self.data_for_calculate)
        result = CalculationHandler(self.parent.InputTechCard.text())
        if result is not None:
            return result
        else:
            raise NoneType


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main_window = DisplayHandler()
    main_window.show()

    sys.exit(app.exec_())
