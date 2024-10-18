from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5 import QtWidgets

from ui.Lrf import Ui_LRF1_Widget
from utils_calculate.formuls_for_calculate import DataHolder, GetDataCalculateWithDb


class DisplayHandler(QWidget, Ui_LRF1_Widget):

    def __init__(self):
        super(DisplayHandler, self).__init__()
        self.setupUi(self)

        self.CalculateClass = HandlerData()
        self.OutputClass = ChangingFieldValues(self)

        self.InputClass = InputDataHandler(self)

        self.ButtonHandlerForDisplay()
        self.LineEditHandlerForDisplay()

    def ButtonHandlerForDisplay(self):
        pass

    def LineEditHandlerForDisplay(self):
        self.InputTechCard.setValidator(QIntValidator(0, 999))
        self.InputTechCard.editingFinished.connect(self.InputClass.handle_input)

        self.InputWeight.setValidator(QDoubleValidator(0.0, 200.0, 2))
        self.InputWeight.editingFinished.connect(self.CalculateClass.InputDataForCalculate)


class InputDataHandler:

    def __init__(self, parent):
        self.parent = parent

    def handle_input(self):
        tcn_value = self.parent.InputTechCard.text()

        self.initialize_tech_card(tcn_value)

    def initialize_tech_card(self, tcn_value):
        DataHolder.set_data(tcn_value, None)

        self.parent.OutputClass.OutputLabelForFuse()
        self.parent.OutputClass.OutputLabelForTargetFuse()


class ChangingFieldValues:

    def __init__(self, parent):
        self.parent = parent

    def GetFuseData(self):
        return InputDataHandler(self.parent).handle_input()

    def OutputLabelForFuse(self):
        FuseData = self.get_fuse_data()
        self.parent.SteelName.setText(FuseData['FuseName'])
        self.parent.TempForVd.setText(FuseData['TempVd'])
        self.parent.Mnlz1.setText(FuseData['Temp_ccm1'])
        self.parent.Mnlz2.setText(FuseData['Temp_ccm2'])

    def OutputLabelForTargetFuse(self):
        FuseData = self.get_fuse_data()

        ElementsCleanDict = {
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

        for AttrKeyFuse, AttrValueFuse in FuseData.items():
            for AttrKeyDict, AttrValueDict in ElementsCleanDict.items():
                if AttrKeyFuse == AttrKeyDict:
                    ElementsCleanDict[AttrKeyFuse].setText(str(FuseData[AttrKeyFuse]))
                else:
                        self.handler_hidding_for_fuse_material_target(AttrKeyDict)

    def handler_hidding_for_fuse_material_target(self, value):
        layout_name = f'Layout{value}'
        layout = getattr(self.parent, layout_name, None)

        if layout:
            for i in range(layout.count()):
                widget = layout.itemAt(i).widget()
                if widget:
                    widget.setVisible(False)

    def get_fuse_data(self):
        return GetDataCalculateWithDb().get_data_fuse()


class HandlerData:
    def __init__(self):
        pass

    def InputDataForCalculate(self):
        # Логика для обработки данных
        pass


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main_window = DisplayHandler()
    main_window.show()

    sys.exit(app.exec_())
