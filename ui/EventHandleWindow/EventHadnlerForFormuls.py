
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit

from ui.Designe.Converter.Formuls import Ui_FormulsDesigner


class DisplayHandlerFormuls(QWidget, Ui_FormulsDesigner):
    def __init__(self):
        super(DisplayHandlerFormuls, self).__init__()
        self.setupUi(self)
        self.setStyleSheet("""
            QRadioButton#Cekv::indicator{
                background-color: red;
                border-radius: 6px;
            }
            QRadioButton#Ct::indicator{
                background-color: orange;
                border-radius: 6px;
            }
            QRadioButton#Pcm::indicator{
                background-color: yellow;
                border-radius: 6px;
            }
            QRadioButton#J_Factor::indicator{
                background-color: green;
                border-radius: 6px;
            }
            QRadioButton#Cu_8_Sn::indicator{
                background-color: Cyan;
                border-radius: 6px;
            }
            QRadioButton#Cr_Ni_Mo_V::indicator{
                background-color: blue;
                border-radius: 6px;
            }
            QRadioButton#Cr_Ni_Cu::indicator{
                background-color: purple;
                border-radius: 6px;
            }
            QRadioButton::indicator:checked{
                border: 2px solid black;
            }
            QRadioButton::indicator:hover{
                border: 2px solid black;
            }
        """)
        self.Cekv.toggled.connect(self.on_radio_toggled)
        self.Ct.toggled.connect(self.on_radio_toggled)
        self.Pcm.toggled.connect(self.on_radio_toggled)
        self.J_Factor.toggled.connect(self.on_radio_toggled)
        self.Cu_8_Sn.toggled.connect(self.on_radio_toggled)
        self.Cr_Ni_Mo_V.toggled.connect(self.on_radio_toggled)
        self.Cr_Ni_Cu.toggled.connect(self.on_radio_toggled)
        self.handler_input_data_dict = {
            'Cekv': {},
            'Ct': {},
            'Pcm': {},
            'J_Factor': {},
            'Cu_8_Sn': {},
            'Cr_Ni_Mo_V': {},
            'Cr_Ni_Cu': {},
        }
        self.formuls_dict = {
            'Cekv': {
                'C': {},
                'Mn': {},
                'Cr': {},
                'Ni': {},
                'Cu': {},
                'Mo': {},
                'V': {}
            },
            'Ct': {
                'C': {},
                'Mn': {},
                'Cr': {},
                'Ni': {},
                'Cu': {},
                'Mo': {},
            },
            'Pcm': {
                'C': {},
                'Si': {},
                'Mn': {},
                'Cr': {},
                'Ni': {},
                'Cu': {},
                'Mo': {},
                'V': {},
                'B': {}
            },
            'J_Factor': {
                'Si': {},
                'Mn': {},
                'P': {},
                'Sn': {}
            },
            'Cu_8_Sn': {
                'Cu': {},
                'Sn': {}
            },
            'Cr_Ni_Mo_V': {
                'Ni': {},
                'Cr': {},
                'Mo': {},
                'V': {}

            },
            'Cr_Ni_Cu': {
                'Cr': {},
                'Ni': {},
                'Cu': {}
            },
        }

        self.formuls_handlers = {
            'Cekv': self.Calc_Cekv,
            'Ct': self.Calc_Ct,
            'Pcm': self.Calc_Pcm,
            'J_Factor': self.Calc_J_Factor,
            'Cu_8_Sn': self.Calc_Cu_8_Sn,
            'Cr_Ni_Mo_V': self.Calc_Cr_Ni_Mo_V,
            'Cr_Ni_Cu': self.Calc_Cr_Ni_Cu,
        }

    def reset_formuls_dict(self):
        self.handler_input_data_dict = {
            'Cekv': {},
            'Ct': {},
            'Pcm': {},
            'J_Factor': {},
            'Cu_8_Sn': {},
            'Cr_Ni_Mo_V': {},
            'Cr_Ni_Cu': {},
        }

    def on_radio_toggled(self, checked):
        sender = self.sender()
        if checked:
            self.reset_formuls_dict()
            self.initial_formuls_label(sender.objectName())

    def initial_formuls_label(self, radio_button_name):
        list_material = ['C', 'Si', 'Mn', 'P', 'Cr', 'Ni', 'Cu', 'Mo', 'V', 'B', 'Sn']
        formuls_dict = self.formuls_dict

        if radio_button_name in formuls_dict:
            formula_data = formuls_dict[radio_button_name]

            for material in list_material:
                if material not in formula_data:

                    self.disable_unused_buttons(material, False)

                else:
                    self.disable_unused_buttons(material, True)
                    Layout_name = f'InputFor{material}'
                    Layout_init = getattr(self, Layout_name, None)
                    if Layout_init:
                        Layout_init.setValidator(QDoubleValidator(0.0, 4.0, 3))
                        Layout_init.editingFinished.connect(
                            lambda line_edit=Layout_init, mat=material: self.handler_input(line_edit, mat,
                                                                                           radio_button_name)
                        )

    def handler_input(self, line_edit, mat, radio_button_name):
        input_value = line_edit.text()
        if input_value:
            self.handler_input_data_dict[radio_button_name][mat] = input_value
            self.formuls_handlers.get(radio_button_name)()

    def disable_unused_buttons(self, material, solition):
        Layout_name = f'LayoutFor{material}'
        Layout_init = getattr(self, Layout_name, None)
        for i in range(Layout_init.count()):
            widget = Layout_init.itemAt(i).widget()
            if solition == True:
                if isinstance(widget, QLineEdit):
                    widget.clear()
                widget.setStyleSheet("""
                                    border-bottom: 2px solid #BCFBA7;
                                """)
                widget.setEnabled(solition)
            else:
                if isinstance(widget, QLineEdit):
                    widget.clear()
                widget.setStyleSheet("""
                                    border-bottom: 2px solid #E0E0E0;
                                """)
                widget.setEnabled(solition)

    def Calc_Cekv(self):
        C = self.handler_input_data_dict['Cekv'].get('C')
        Mn = self.handler_input_data_dict['Cekv'].get('Mn')
        Cr = self.handler_input_data_dict['Cekv'].get('Cr')
        Ni = self.handler_input_data_dict['Cekv'].get('Ni')
        Mo = self.handler_input_data_dict['Cekv'].get('Mo')
        Cu = self.handler_input_data_dict['Cekv'].get('Cu')
        V = self.handler_input_data_dict['Cekv'].get('V')
        if C and Mn and Cr and Ni and Mo and Cu and V:
            C_Mn = float(C.replace(',', '.')) + (float(Mn.replace(',', '.')) / 6)

            Cr_Mo_V = (float(Cr.replace(',', '.')) + float(Mo.replace(',', '.')) + float(V.replace(',', '.'))) / 5
            Ni_Cu = (float(Ni.replace(',', '.')) + float(Cu.replace(',', '.'))) / 15
            result = round(C_Mn + Cr_Mo_V + Ni_Cu, 3)
            self.LabelCekv.clear()
            self.LabelCekv.setText(str(result))

    def Calc_Ct(self):
        C = self.handler_input_data_dict['Ct'].get('C')
        Mn = self.handler_input_data_dict['Ct'].get('Mn')
        Cr = self.handler_input_data_dict['Ct'].get('Cr')
        Ni = self.handler_input_data_dict['Ct'].get('Ni')
        Cu = self.handler_input_data_dict['Ct'].get('Cu')
        Mo = self.handler_input_data_dict['Ct'].get('Mo')

        if C and Mn and Cr and Ni and Cu and Mo:
            Mn_Mo = ((float(Mn.replace(',', '.')) + float(Mo.replace(',', '.'))) / 10) + float(C.replace(',', '.'))
            Cr_Cu = ((float(Cr.replace(',', '.')) + float(Cu.replace(',', '.'))) / 20) + (
                float(Ni.replace(',', '.'))) / 40
            result = round(Mn_Mo + Cr_Cu, 3)
            self.LabelCt.clear()
            self.LabelCt.setText(str(result))

    def Calc_Pcm(self):
        C = self.handler_input_data_dict['Pcm'].get('C')
        Si = self.handler_input_data_dict['Pcm'].get('Si')
        Mn = self.handler_input_data_dict['Pcm'].get('Mn')
        Cr = self.handler_input_data_dict['Pcm'].get('Cr')
        Ni = self.handler_input_data_dict['Pcm'].get('Ni')
        Mo = self.handler_input_data_dict['Pcm'].get('Mo')
        Cu = self.handler_input_data_dict['Pcm'].get('Cu')
        V = self.handler_input_data_dict['Pcm'].get('V')
        B = self.handler_input_data_dict['Pcm'].get('B')

        if C and Mn and Cr and Ni and Mo and Cu and B:
            C_Mn_Si_Cu=float(C.replace(',', '.'))+(float(Si.replace(',','.'))/30)+(float(Mn.replace(',', '.'))/20)+(float(Cu.replace(',', '.'))/20)
            Ni_Cr_Mo_V= (float(Ni.replace(',','.'))/60)+(float(Cr.replace(',','.'))/20)+(float(Mo.replace(',','.'))/15)+(float(V.replace(',','.'))/10)
            result = round((C_Mn_Si_Cu+Ni_Cr_Mo_V)+(float(B.replace(',','.'))*5),3)
            self.LabelPcm.clear()
            self.LabelPcm.setText(str(result))

    def Calc_J_Factor(self):
        Si = self.handler_input_data_dict['J_Factor'].get('Si')
        Mn = self.handler_input_data_dict['J_Factor'].get('Mn')
        Sn = self.handler_input_data_dict['J_Factor'].get('Sn')
        P = self.handler_input_data_dict['J_Factor'].get('P')

        if Si and Mn and Sn and P:
            result = round(
                (float(Si.replace(',', '.')) + float(Mn.replace(',', '.'))) * (
                        (float(Sn.replace(',', '.'))) + (float(P.replace(',', '.')))) * 10000, 3)
            self.LabelJ_Factor.clear()
            self.LabelCr_Ni_Mo_V.setText(str(result))

    def Calc_Cu_8_Sn(self):
        Cu = self.handler_input_data_dict['Cu_8_Sn'].get('Cu')
        Sn = self.handler_input_data_dict['Cu_8_Sn'].get('Sn')
        if Cu and Sn:
            result = round(
                float(Cu.replace(',', '.')) + float(Sn.replace(',', '.')) * 8, 3)
            self.LabelCr_Ni_Mo_V.clear()
            self.LabelCr_Ni_Mo_V.setText(str(result))

    def Calc_Cr_Ni_Mo_V(self):
        Cr = self.handler_input_data_dict['Cr_Ni_Mo_V'].get('Cr')
        Ni = self.handler_input_data_dict['Cr_Ni_Mo_V'].get('Ni')
        Mo = self.handler_input_data_dict['Cr_Ni_Mo_V'].get('Mo')
        V = self.handler_input_data_dict['Cr_Ni_Mo_V'].get('V')

        if Cr and Ni and Mo and V:
            result = round(
                float(Cr.replace(',', '.')) + float(Ni.replace(',', '.')) + float(Mo.replace(',', '.')) + float(
                    V.replace(',', '.')), 3)
            self.LabelCr_Ni_Mo_V.clear()
            self.LabelCr_Ni_Mo_V.setText(str(result))

    def Calc_Cr_Ni_Cu(self):
        print(self.handler_input_data_dict)
        self.LabelCr_Ni_Cu.clear()
        Cr = self.handler_input_data_dict['Cr_Ni_Cu'].get('Cr')
        Ni = self.handler_input_data_dict['Cr_Ni_Cu'].get('Ni')
        Cu = self.handler_input_data_dict['Cr_Ni_Cu'].get('Cu')

        if Cr and Ni and Cu:
            result = round(float(Cr.replace(',', '.')) + float(Ni.replace(',', '.')) + float(Cu.replace(',', '.')), 3)
            self.LabelCr_Ni_Cu.setText(str(result))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main_window = DisplayHandlerFormuls()
    main_window.show()

    sys.exit(app.exec_())
