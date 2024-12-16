from PyQt5.QtCore import  QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QComboBox
from PyQt5.QtGui import QDoubleValidator, QIntValidator

from ui.Designe.Lrf import Ui_LRF1_Widget
from ui.calculate import CalculationHandler
from utils_calculate.formuls_for_calculate import DataHolder, get_data_calculate_with_db


class DisplayHandlerLrf(QWidget, Ui_LRF1_Widget):

    def __init__(self):
        super(DisplayHandlerLrf, self).__init__()
        self.setupUi(self)

        self.CalculateClass = handler_data(self)
        self.OutputClass = changing_field_values(self)
        self.InputClass = input_data_handler(self)

        self.line_edit_handler_for_display()


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_layout)
        self.timer.start(100)



    def update_layout(self):
        layout_width = self.AllLrf.sizeHint().width()
        layout_height = self.AllLrf.sizeHint().height()
        self.resize(layout_width + 90, layout_height + 10)
        self.updateGeometry()



    def line_edit_handler_for_display(self):
        self.InputTechCard.setValidator(QIntValidator(0, 999))
        self.InputTechCard.editingFinished.connect(self.InputClass.handle_input)

        self.InputWeight.setValidator(QDoubleValidator(0.0, 200.0, 2))
        self.InputWeight.editingFinished.connect(self.line_edit_handler_for_calculate_material)




    def line_edit_handler_for_calculate_material(self):
        self.reset_samples_dict()
        self.setup_handlers(self.OutputClass.elements_visible_list)

    def setup_material_handlers(self, material_list, prefix_input, prefix_box):
        for material in material_list:
            input_name = f'{prefix_input}{material}'
            input_field = getattr(self, input_name, None)
            if input_field:
                input_field.setValidator(QDoubleValidator(0.0, 4.0, 3))
                input_field.editingFinished.connect(
                    lambda line_edit=input_field, mat=material: self.handler_input(line_edit, mat)
                )

            box_name = f'{prefix_box}{material}'
            material_box = getattr(self, box_name, None)
            if isinstance(material_box, QComboBox):
                material_box.currentIndexChanged.connect(
                    lambda _, mat=material, box=material_box: self.handle_material_change(mat, box)
                )

    def setup_handlers(self, material_list):

        self.setup_material_handlers(material_list, 'LabelSamplesFor', 'MaterialFor')

    def handler_input(self, line_edit, material):

        Material_Box = f'MaterialFor{material}'
        Material_Box_edit = getattr(self, Material_Box, None)
        if isinstance(Material_Box_edit, QComboBox):
            material_box_value = Material_Box_edit.currentText()
        else:
            material_box_value = Material_Box_edit.text()

        input_value = line_edit.text()
        if input_value:
            if material in ['Cpr', 'Al', 'Ti', 'Ca']:
                self.OutputClass.samples_dict['corewire'][material] = input_value
                self.OutputClass.samples_dict['material'][material] = material_box_value
            else:
                self.OutputClass.samples_dict['samples'][material] = input_value
                self.OutputClass.samples_dict['material'][material] = material_box_value

            self.OutputClass.samples_dict['W'] = self.InputWeight.text()
            self.OutputClass.samples_dict['temp'] = self.LabelTargetCoreForCa.text()
            self.CalculateClass.Handler_for_calculate(self.OutputClass.samples_dict)
            # print(self.OutputClass.samples_dict)

    def reset_samples_dict(self):
        self.OutputClass.samples_dict = {
            'W': self.InputWeight.text(),
            'samples': {},
            'material': {},
            'corewire': {},
            'temp':self.LabelTargetCoreForCa.text()
        }

    def handle_material_change(self, material, material_box):
        self.OutputClass.samples_dict['material'][material] = material_box.currentText()
        self.CalculateClass.Handler_for_calculate(self.OutputClass.samples_dict)


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


class changing_field_values:
    elements_visible_list = None

    def __init__(self, parent):
        self.parent = parent
        self.samples_dict = {
            'W': self.parent.InputWeight.text(),
            'samples': {},
            'material': {},
            'corewire': {},
            'temp':{}
        }

        self.elements_visible_list = []

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

            'Cpr': self.parent.LabelTargetCoreForC,
            'Al': self.parent.LabelTargetCoreForAl,
            'Ti': self.parent.LabelTargetCoreForTi,
            'Ca': self.parent.LabelTargetCoreForCa,
        }
        self.elements_visible_list.clear()
        for AttrKeyDict, AttrValueDict in elements_clean_dict.items():
            if AttrKeyDict in FuseData:
                elements_clean_dict[AttrKeyDict].setText(str(FuseData[AttrKeyDict]))
                self.elements_visible_list.append(AttrKeyDict)
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

    def Handler_for_calculate(self, Data):

        DataHolder.set_data(self.parent.InputTechCard.text(),
                            Data)
        result = CalculationHandler(self.parent.InputTechCard.text(), Data).HandlerSamples()
        for attr_key, attr_value in result.items():
            if attr_key in ['Cpr', 'Al', 'Ti','Ca']:
                LabelMetersCoreInit = f'LabelMetersCoreFor{attr_key}'
                LabelMetersCoreName = getattr(self.parent, LabelMetersCoreInit, None)
                if LabelMetersCoreName:
                    self.flight_check_materials(LabelMetersCoreName, attr_value)

            LabelKiloInit = f'LabelKiloFor{attr_key}'
            LabelKiloName = getattr(self.parent, LabelKiloInit, None)
            if LabelKiloName:
                self.flight_check_materials(LabelKiloName, attr_value)

    def flight_check_materials(self, handler, value):
        if value < 0:
            handler.setStyleSheet("""
                     border-bottom: 2px solid #FFA5A5;
    
                 """)
        else:
            handler.setText(str(value))
            handler.setStyleSheet("""
                     border-bottom: 2px solid #BCFBA7;
                 """)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main_window = DisplayHandlerLrf()
    main_window.show()

    sys.exit(app.exec_())
