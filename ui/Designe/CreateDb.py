# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateDbDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogCreate_Db(object):
    def setupUi(self, DialogCreate_Db):
        DialogCreate_Db.setObjectName("DialogCreate_Db")
        DialogCreate_Db.resize(678, 280)
        self.widget = QtWidgets.QWidget(DialogCreate_Db)
        self.widget.setGeometry(QtCore.QRect(11, 13, 651, 258))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ComboBox_For_DbModels = QtWidgets.QComboBox(self.widget)
        self.ComboBox_For_DbModels.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.ComboBox_For_DbModels.setObjectName("ComboBox_For_DbModels")
        self.ComboBox_For_DbModels.addItem("")
        self.ComboBox_For_DbModels.addItem("")
        self.ComboBox_For_DbModels.addItem("")
        self.ComboBox_For_DbModels.addItem("")
        self.gridLayout.addWidget(self.ComboBox_For_DbModels, 0, 0, 1, 1)
        self.Layout_for_forms = QtWidgets.QVBoxLayout()
        self.Layout_for_forms.setSpacing(0)
        self.Layout_for_forms.setObjectName("Layout_for_forms")
        self.Layout_for_chemicalcomp = QtWidgets.QVBoxLayout()
        self.Layout_for_chemicalcomp.setSpacing(0)
        self.Layout_for_chemicalcomp.setObjectName("Layout_for_chemicalcomp")
        self.Layout_for_forms.addLayout(self.Layout_for_chemicalcomp)
        self.chemical_comp = QtWidgets.QVBoxLayout()
        self.chemical_comp.setObjectName("chemical_comp")
        self.one = QtWidgets.QHBoxLayout()
        self.one.setSpacing(3)
        self.one.setObjectName("one")
        self.Layout_Inut_name_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_name_db.setObjectName("Layout_Inut_name_db")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.LabelName = QtWidgets.QLabel(self.widget)
        self.LabelName.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelName.setObjectName("LabelName")
        self.verticalLayout.addWidget(self.LabelName)
        self.Inut_name_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_name_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_name_db.setAlignment(QtCore.Qt.AlignCenter)
        self.Inut_name_db.setObjectName("Inut_name_db")
        self.verticalLayout.addWidget(self.Inut_name_db)
        self.Layout_Inut_name_db.addLayout(self.verticalLayout)
        self.one.addLayout(self.Layout_Inut_name_db)
        self.Layout_Inut_C_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_C_db.setObjectName("Layout_Inut_C_db")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_C = QtWidgets.QLabel(self.widget)
        self.label_C.setObjectName("label_C")
        self.verticalLayout_2.addWidget(self.label_C)
        self.Inut_C_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_C_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_C_db.setObjectName("Inut_C_db")
        self.verticalLayout_2.addWidget(self.Inut_C_db)
        self.Layout_Inut_C_db.addLayout(self.verticalLayout_2)
        self.one.addLayout(self.Layout_Inut_C_db)
        self.Layout_Inut_Mn_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Mn_db.setObjectName("Layout_Inut_Mn_db")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_Mn = QtWidgets.QLabel(self.widget)
        self.label_Mn.setObjectName("label_Mn")
        self.verticalLayout_3.addWidget(self.label_Mn)
        self.Inut_Mn_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Mn_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Mn_db.setObjectName("Inut_Mn_db")
        self.verticalLayout_3.addWidget(self.Inut_Mn_db)
        self.Layout_Inut_Mn_db.addLayout(self.verticalLayout_3)
        self.one.addLayout(self.Layout_Inut_Mn_db)
        self.Layout_Inut_Si_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Si_db.setObjectName("Layout_Inut_Si_db")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_Si = QtWidgets.QLabel(self.widget)
        self.label_Si.setObjectName("label_Si")
        self.verticalLayout_5.addWidget(self.label_Si)
        self.Inut_Si_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Si_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Si_db.setObjectName("Inut_Si_db")
        self.verticalLayout_5.addWidget(self.Inut_Si_db)
        self.Layout_Inut_Si_db.addLayout(self.verticalLayout_5)
        self.one.addLayout(self.Layout_Inut_Si_db)
        self.Layout_Inut_Cr_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Cr_db.setObjectName("Layout_Inut_Cr_db")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_Cr = QtWidgets.QLabel(self.widget)
        self.label_Cr.setObjectName("label_Cr")
        self.verticalLayout_4.addWidget(self.label_Cr)
        self.Inut_Cr_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Cr_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Cr_db.setObjectName("Inut_Cr_db")
        self.verticalLayout_4.addWidget(self.Inut_Cr_db)
        self.Layout_Inut_Cr_db.addLayout(self.verticalLayout_4)
        self.one.addLayout(self.Layout_Inut_Cr_db)
        self.Layout_Inut_Ti_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Ti_db.setObjectName("Layout_Inut_Ti_db")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_Ti = QtWidgets.QLabel(self.widget)
        self.label_Ti.setObjectName("label_Ti")
        self.verticalLayout_6.addWidget(self.label_Ti)
        self.Inut_Ti_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Ti_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Ti_db.setObjectName("Inut_Ti_db")
        self.verticalLayout_6.addWidget(self.Inut_Ti_db)
        self.Layout_Inut_Ti_db.addLayout(self.verticalLayout_6)
        self.one.addLayout(self.Layout_Inut_Ti_db)
        self.Layout_Inut_V_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_V_db.setObjectName("Layout_Inut_V_db")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_V = QtWidgets.QLabel(self.widget)
        self.label_V.setObjectName("label_V")
        self.verticalLayout_12.addWidget(self.label_V)
        self.Inut_V_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_V_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_V_db.setObjectName("Inut_V_db")
        self.verticalLayout_12.addWidget(self.Inut_V_db)
        self.Layout_Inut_V_db.addLayout(self.verticalLayout_12)
        self.one.addLayout(self.Layout_Inut_V_db)
        self.chemical_comp.addLayout(self.one)
        self.two = QtWidgets.QHBoxLayout()
        self.two.setSpacing(6)
        self.two.setObjectName("two")
        self.Layout_Inut_Mo_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Mo_db.setObjectName("Layout_Inut_Mo_db")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_Mo = QtWidgets.QLabel(self.widget)
        self.label_Mo.setObjectName("label_Mo")
        self.verticalLayout_11.addWidget(self.label_Mo)
        self.Inut_Mo_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Mo_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Mo_db.setObjectName("Inut_Mo_db")
        self.verticalLayout_11.addWidget(self.Inut_Mo_db)
        self.Layout_Inut_Mo_db.addLayout(self.verticalLayout_11)
        self.two.addLayout(self.Layout_Inut_Mo_db)
        self.Layout_Inut_B_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_B_db.setObjectName("Layout_Inut_B_db")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_B = QtWidgets.QLabel(self.widget)
        self.label_B.setObjectName("label_B")
        self.verticalLayout_8.addWidget(self.label_B)
        self.Inut_B_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_B_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_B_db.setObjectName("Inut_B_db")
        self.verticalLayout_8.addWidget(self.Inut_B_db)
        self.Layout_Inut_B_db.addLayout(self.verticalLayout_8)
        self.two.addLayout(self.Layout_Inut_B_db)
        self.Layout_Inut_Nb_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Nb_db.setObjectName("Layout_Inut_Nb_db")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_Nb = QtWidgets.QLabel(self.widget)
        self.label_Nb.setObjectName("label_Nb")
        self.verticalLayout_7.addWidget(self.label_Nb)
        self.Inut_Nb_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Nb_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Nb_db.setObjectName("Inut_Nb_db")
        self.verticalLayout_7.addWidget(self.Inut_Nb_db)
        self.Layout_Inut_Nb_db.addLayout(self.verticalLayout_7)
        self.two.addLayout(self.Layout_Inut_Nb_db)
        self.Layout_Inut_Ni_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Ni_db.setObjectName("Layout_Inut_Ni_db")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_Ni = QtWidgets.QLabel(self.widget)
        self.label_Ni.setObjectName("label_Ni")
        self.verticalLayout_10.addWidget(self.label_Ni)
        self.Inut_Ni_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Ni_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Ni_db.setObjectName("Inut_Ni_db")
        self.verticalLayout_10.addWidget(self.Inut_Ni_db)
        self.Layout_Inut_Ni_db.addLayout(self.verticalLayout_10)
        self.two.addLayout(self.Layout_Inut_Ni_db)
        self.Layout_Inut_Cu_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Cu_db.setObjectName("Layout_Inut_Cu_db")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_Cu = QtWidgets.QLabel(self.widget)
        self.label_Cu.setObjectName("label_Cu")
        self.verticalLayout_9.addWidget(self.label_Cu)
        self.Inut_Cu_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Cu_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Cu_db.setObjectName("Inut_Cu_db")
        self.verticalLayout_9.addWidget(self.Inut_Cu_db)
        self.Layout_Inut_Cu_db.addLayout(self.verticalLayout_9)
        self.two.addLayout(self.Layout_Inut_Cu_db)
        self.Layout_Inut_Al_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Al_db.setObjectName("Layout_Inut_Al_db")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_Al = QtWidgets.QLabel(self.widget)
        self.label_Al.setObjectName("label_Al")
        self.verticalLayout_13.addWidget(self.label_Al)
        self.Inut_Al_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Al_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Al_db.setObjectName("Inut_Al_db")
        self.verticalLayout_13.addWidget(self.Inut_Al_db)
        self.Layout_Inut_Al_db.addLayout(self.verticalLayout_13)
        self.two.addLayout(self.Layout_Inut_Al_db)
        self.Layout_Inut_S_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_S_db.setObjectName("Layout_Inut_S_db")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_S = QtWidgets.QLabel(self.widget)
        self.label_S.setObjectName("label_S")
        self.verticalLayout_14.addWidget(self.label_S)
        self.Inut_S_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_S_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_S_db.setObjectName("Inut_S_db")
        self.verticalLayout_14.addWidget(self.Inut_S_db)
        self.Layout_Inut_S_db.addLayout(self.verticalLayout_14)
        self.two.addLayout(self.Layout_Inut_S_db)
        self.Layout_Inut_Fe_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Fe_db.setObjectName("Layout_Inut_Fe_db")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_Fe = QtWidgets.QLabel(self.widget)
        self.label_Fe.setObjectName("label_Fe")
        self.verticalLayout_15.addWidget(self.label_Fe)
        self.Inut_Fe_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Fe_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Fe_db.setObjectName("Inut_Fe_db")
        self.verticalLayout_15.addWidget(self.Inut_Fe_db)
        self.Layout_Inut_Fe_db.addLayout(self.verticalLayout_15)
        self.two.addLayout(self.Layout_Inut_Fe_db)
        self.Layout_Inut_Ca_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Ca_db.setObjectName("Layout_Inut_Ca_db")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_Ca = QtWidgets.QLabel(self.widget)
        self.label_Ca.setObjectName("label_Ca")
        self.verticalLayout_16.addWidget(self.label_Ca)
        self.Inut_Ca_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Ca_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Ca_db.setObjectName("Inut_Ca_db")
        self.verticalLayout_16.addWidget(self.Inut_Ca_db)
        self.Layout_Inut_Ca_db.addLayout(self.verticalLayout_16)
        self.two.addLayout(self.Layout_Inut_Ca_db)
        self.Layout_Inut_P_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_P_db.setObjectName("Layout_Inut_P_db")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_P = QtWidgets.QLabel(self.widget)
        self.label_P.setObjectName("label_P")
        self.verticalLayout_17.addWidget(self.label_P)
        self.Inut_P_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_P_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_P_db.setObjectName("Inut_P_db")
        self.verticalLayout_17.addWidget(self.Inut_P_db)
        self.Layout_Inut_P_db.addLayout(self.verticalLayout_17)
        self.two.addLayout(self.Layout_Inut_P_db)
        self.chemical_comp.addLayout(self.two)
        self.Layout_for_forms.addLayout(self.chemical_comp)
        self.Layout_for_fuse_form = QtWidgets.QHBoxLayout()
        self.Layout_for_fuse_form.setSpacing(6)
        self.Layout_for_fuse_form.setObjectName("Layout_for_fuse_form")
        self.Fuse_Tcn = QtWidgets.QVBoxLayout()
        self.Fuse_Tcn.setSpacing(0)
        self.Fuse_Tcn.setObjectName("Fuse_Tcn")
        self.label_tcn = QtWidgets.QLabel(self.widget)
        self.label_tcn.setObjectName("label_tcn")
        self.Fuse_Tcn.addWidget(self.label_tcn)
        self.input_Tcn = QtWidgets.QLineEdit(self.widget)
        self.input_Tcn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.input_Tcn.setObjectName("input_Tcn")
        self.Fuse_Tcn.addWidget(self.input_Tcn)
        self.Layout_for_fuse_form.addLayout(self.Fuse_Tcn)
        self.Fuse_Name = QtWidgets.QVBoxLayout()
        self.Fuse_Name.setSpacing(0)
        self.Fuse_Name.setObjectName("Fuse_Name")
        self.label_FuseName = QtWidgets.QLabel(self.widget)
        self.label_FuseName.setObjectName("label_FuseName")
        self.Fuse_Name.addWidget(self.label_FuseName)
        self.Input_FuseName = QtWidgets.QLineEdit(self.widget)
        self.Input_FuseName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Input_FuseName.setObjectName("Input_FuseName")
        self.Fuse_Name.addWidget(self.Input_FuseName)
        self.Layout_for_fuse_form.addLayout(self.Fuse_Name)
        self.TempVd = QtWidgets.QVBoxLayout()
        self.TempVd.setSpacing(0)
        self.TempVd.setObjectName("TempVd")
        self.label_TempVd = QtWidgets.QLabel(self.widget)
        self.label_TempVd.setObjectName("label_TempVd")
        self.TempVd.addWidget(self.label_TempVd)
        self.Input_TempVd = QtWidgets.QLineEdit(self.widget)
        self.Input_TempVd.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Input_TempVd.setObjectName("Input_TempVd")
        self.TempVd.addWidget(self.Input_TempVd)
        self.Layout_for_fuse_form.addLayout(self.TempVd)
        self.Temp_ccm1 = QtWidgets.QVBoxLayout()
        self.Temp_ccm1.setSpacing(0)
        self.Temp_ccm1.setObjectName("Temp_ccm1")
        self.label_Temp_ccm1 = QtWidgets.QLabel(self.widget)
        self.label_Temp_ccm1.setObjectName("label_Temp_ccm1")
        self.Temp_ccm1.addWidget(self.label_Temp_ccm1)
        self.Input_Temp_ccm1 = QtWidgets.QLineEdit(self.widget)
        self.Input_Temp_ccm1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Input_Temp_ccm1.setObjectName("Input_Temp_ccm1")
        self.Temp_ccm1.addWidget(self.Input_Temp_ccm1)
        self.Layout_for_fuse_form.addLayout(self.Temp_ccm1)
        self.Temp_ccm2 = QtWidgets.QVBoxLayout()
        self.Temp_ccm2.setSpacing(0)
        self.Temp_ccm2.setObjectName("Temp_ccm2")
        self.label_Temp_ccm2 = QtWidgets.QLabel(self.widget)
        self.label_Temp_ccm2.setObjectName("label_Temp_ccm2")
        self.Temp_ccm2.addWidget(self.label_Temp_ccm2)
        self.Input_Temp_ccm2 = QtWidgets.QLineEdit(self.widget)
        self.Input_Temp_ccm2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Input_Temp_ccm2.setObjectName("Input_Temp_ccm2")
        self.Temp_ccm2.addWidget(self.Input_Temp_ccm2)
        self.Layout_for_fuse_form.addLayout(self.Temp_ccm2)
        self.Layout_for_forms.addLayout(self.Layout_for_fuse_form)
        self.chemical_comp_for_fuse = QtWidgets.QVBoxLayout()
        self.chemical_comp_for_fuse.setObjectName("chemical_comp_for_fuse")
        self.Fuse_one = QtWidgets.QHBoxLayout()
        self.Fuse_one.setSpacing(3)
        self.Fuse_one.setObjectName("Fuse_one")
        self.Layout_Inut_C_for_Fuse_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_C_for_Fuse_db.setObjectName("Layout_Inut_C_for_Fuse_db")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_C_2 = QtWidgets.QLabel(self.widget)
        self.label_C_2.setObjectName("label_C_2")
        self.verticalLayout_19.addWidget(self.label_C_2)
        self.Inut_C_for_Fus_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_C_for_Fus_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_C_for_Fus_db.setObjectName("Inut_C_for_Fus_db")
        self.verticalLayout_19.addWidget(self.Inut_C_for_Fus_db)
        self.Layout_Inut_C_for_Fuse_db.addLayout(self.verticalLayout_19)
        self.Fuse_one.addLayout(self.Layout_Inut_C_for_Fuse_db)
        self.Layout_Inut_Mn_for_Fuse_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Mn_for_Fuse_db.setObjectName("Layout_Inut_Mn_for_Fuse_db")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_Mn_2 = QtWidgets.QLabel(self.widget)
        self.label_Mn_2.setObjectName("label_Mn_2")
        self.verticalLayout_20.addWidget(self.label_Mn_2)
        self.Inut_Mn_for_Fus_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Mn_for_Fus_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Mn_for_Fus_db.setObjectName("Inut_Mn_for_Fus_db")
        self.verticalLayout_20.addWidget(self.Inut_Mn_for_Fus_db)
        self.Layout_Inut_Mn_for_Fuse_db.addLayout(self.verticalLayout_20)
        self.Fuse_one.addLayout(self.Layout_Inut_Mn_for_Fuse_db)
        self.Layout_Inut_Si_for_Fuse_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Si_for_Fuse_db.setObjectName("Layout_Inut_Si_for_Fuse_db")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_Si_2 = QtWidgets.QLabel(self.widget)
        self.label_Si_2.setObjectName("label_Si_2")
        self.verticalLayout_21.addWidget(self.label_Si_2)
        self.Inut_Si_for_Fus_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Si_for_Fus_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Si_for_Fus_db.setObjectName("Inut_Si_for_Fus_db")
        self.verticalLayout_21.addWidget(self.Inut_Si_for_Fus_db)
        self.Layout_Inut_Si_for_Fuse_db.addLayout(self.verticalLayout_21)
        self.Fuse_one.addLayout(self.Layout_Inut_Si_for_Fuse_db)
        self.Layout_Inut_Cr_for_Fuse_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Cr_for_Fuse_db.setObjectName("Layout_Inut_Cr_for_Fuse_db")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_Cr_2 = QtWidgets.QLabel(self.widget)
        self.label_Cr_2.setObjectName("label_Cr_2")
        self.verticalLayout_22.addWidget(self.label_Cr_2)
        self.Inut_Cr_for_Fus_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Cr_for_Fus_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Cr_for_Fus_db.setObjectName("Inut_Cr_for_Fus_db")
        self.verticalLayout_22.addWidget(self.Inut_Cr_for_Fus_db)
        self.Layout_Inut_Cr_for_Fuse_db.addLayout(self.verticalLayout_22)
        self.Fuse_one.addLayout(self.Layout_Inut_Cr_for_Fuse_db)
        self.Layout_Inut_Ti_for_Fuse_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Ti_for_Fuse_db.setObjectName("Layout_Inut_Ti_for_Fuse_db")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_Ti_2 = QtWidgets.QLabel(self.widget)
        self.label_Ti_2.setObjectName("label_Ti_2")
        self.verticalLayout_23.addWidget(self.label_Ti_2)
        self.Inut_Ti_for_Fus_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Ti_for_Fus_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Ti_for_Fus_db.setObjectName("Inut_Ti_for_Fus_db")
        self.verticalLayout_23.addWidget(self.Inut_Ti_for_Fus_db)
        self.Layout_Inut_Ti_for_Fuse_db.addLayout(self.verticalLayout_23)
        self.Fuse_one.addLayout(self.Layout_Inut_Ti_for_Fuse_db)
        self.Layout_Inut_V_for_Fuse_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_V_for_Fuse_db.setObjectName("Layout_Inut_V_for_Fuse_db")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_V_2 = QtWidgets.QLabel(self.widget)
        self.label_V_2.setObjectName("label_V_2")
        self.verticalLayout_24.addWidget(self.label_V_2)
        self.Inut_V_for_Fus_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_V_for_Fus_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_V_for_Fus_db.setObjectName("Inut_V_for_Fus_db")
        self.verticalLayout_24.addWidget(self.Inut_V_for_Fus_db)
        self.Layout_Inut_V_for_Fuse_db.addLayout(self.verticalLayout_24)
        self.Fuse_one.addLayout(self.Layout_Inut_V_for_Fuse_db)
        self.chemical_comp_for_fuse.addLayout(self.Fuse_one)
        self.Fuse_two = QtWidgets.QHBoxLayout()
        self.Fuse_two.setSpacing(6)
        self.Fuse_two.setObjectName("Fuse_two")
        self.Layout_Inut_Mo_for_Fuse_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Mo_for_Fuse_db.setObjectName("Layout_Inut_Mo_for_Fuse_db")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_Mo_2 = QtWidgets.QLabel(self.widget)
        self.label_Mo_2.setObjectName("label_Mo_2")
        self.verticalLayout_25.addWidget(self.label_Mo_2)
        self.Inut_Mo_for_Fus_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Mo_for_Fus_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Mo_for_Fus_db.setObjectName("Inut_Mo_for_Fus_db")
        self.verticalLayout_25.addWidget(self.Inut_Mo_for_Fus_db)
        self.Layout_Inut_Mo_for_Fuse_db.addLayout(self.verticalLayout_25)
        self.Fuse_two.addLayout(self.Layout_Inut_Mo_for_Fuse_db)
        self.Layout_Inut_B_for_Fuse_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_B_for_Fuse_db.setObjectName("Layout_Inut_B_for_Fuse_db")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_B_2 = QtWidgets.QLabel(self.widget)
        self.label_B_2.setObjectName("label_B_2")
        self.verticalLayout_26.addWidget(self.label_B_2)
        self.Inut_B_for_Fus_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_B_for_Fus_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_B_for_Fus_db.setObjectName("Inut_B_for_Fus_db")
        self.verticalLayout_26.addWidget(self.Inut_B_for_Fus_db)
        self.Layout_Inut_B_for_Fuse_db.addLayout(self.verticalLayout_26)
        self.Fuse_two.addLayout(self.Layout_Inut_B_for_Fuse_db)
        self.Layout_Inut_Nb_for_Fuse_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Nb_for_Fuse_db.setObjectName("Layout_Inut_Nb_for_Fuse_db")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_Nb_2 = QtWidgets.QLabel(self.widget)
        self.label_Nb_2.setObjectName("label_Nb_2")
        self.verticalLayout_27.addWidget(self.label_Nb_2)
        self.Inut_Nb_for_Fus_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Nb_for_Fus_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Nb_for_Fus_db.setObjectName("Inut_Nb_for_Fus_db")
        self.verticalLayout_27.addWidget(self.Inut_Nb_for_Fus_db)
        self.Layout_Inut_Nb_for_Fuse_db.addLayout(self.verticalLayout_27)
        self.Fuse_two.addLayout(self.Layout_Inut_Nb_for_Fuse_db)
        self.Layout_Inut_Ni_for_Fuse_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Ni_for_Fuse_db.setObjectName("Layout_Inut_Ni_for_Fuse_db")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_Ni_2 = QtWidgets.QLabel(self.widget)
        self.label_Ni_2.setObjectName("label_Ni_2")
        self.verticalLayout_28.addWidget(self.label_Ni_2)
        self.Inut_Ni_for_Fus_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Ni_for_Fus_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Ni_for_Fus_db.setObjectName("Inut_Ni_for_Fus_db")
        self.verticalLayout_28.addWidget(self.Inut_Ni_for_Fus_db)
        self.Layout_Inut_Ni_for_Fuse_db.addLayout(self.verticalLayout_28)
        self.Fuse_two.addLayout(self.Layout_Inut_Ni_for_Fuse_db)
        self.Layout_Inut_Cu_for_Fuse_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Cu_for_Fuse_db.setObjectName("Layout_Inut_Cu_for_Fuse_db")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.label_Cu_2 = QtWidgets.QLabel(self.widget)
        self.label_Cu_2.setObjectName("label_Cu_2")
        self.verticalLayout_29.addWidget(self.label_Cu_2)
        self.Inut_Cu_for_Fus_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Cu_for_Fus_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Cu_for_Fus_db.setObjectName("Inut_Cu_for_Fus_db")
        self.verticalLayout_29.addWidget(self.Inut_Cu_for_Fus_db)
        self.Layout_Inut_Cu_for_Fuse_db.addLayout(self.verticalLayout_29)
        self.Fuse_two.addLayout(self.Layout_Inut_Cu_for_Fuse_db)
        self.Layout_Inut_Al_for_Fuse_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Al_for_Fuse_db.setObjectName("Layout_Inut_Al_for_Fuse_db")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.label_Al_2 = QtWidgets.QLabel(self.widget)
        self.label_Al_2.setObjectName("label_Al_2")
        self.verticalLayout_30.addWidget(self.label_Al_2)
        self.Inut_Al_for_Fus_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Al_for_Fus_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Al_for_Fus_db.setObjectName("Inut_Al_for_Fus_db")
        self.verticalLayout_30.addWidget(self.Inut_Al_for_Fus_db)
        self.Layout_Inut_Al_for_Fuse_db.addLayout(self.verticalLayout_30)
        self.Fuse_two.addLayout(self.Layout_Inut_Al_for_Fuse_db)
        self.Layout_Inut_S_for_Fuse_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_S_for_Fuse_db.setObjectName("Layout_Inut_S_for_Fuse_db")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label_S_2 = QtWidgets.QLabel(self.widget)
        self.label_S_2.setObjectName("label_S_2")
        self.verticalLayout_31.addWidget(self.label_S_2)
        self.Inut_S_for_Fus_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_S_for_Fus_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_S_for_Fus_db.setObjectName("Inut_S_for_Fus_db")
        self.verticalLayout_31.addWidget(self.Inut_S_for_Fus_db)
        self.Layout_Inut_S_for_Fuse_db.addLayout(self.verticalLayout_31)
        self.Fuse_two.addLayout(self.Layout_Inut_S_for_Fuse_db)
        self.Layout_Inut_Ca_for_Fuse_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Ca_for_Fuse_db.setObjectName("Layout_Inut_Ca_for_Fuse_db")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_Ca_2 = QtWidgets.QLabel(self.widget)
        self.label_Ca_2.setObjectName("label_Ca_2")
        self.verticalLayout_33.addWidget(self.label_Ca_2)
        self.Inut_Ca_for_Fus_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Ca_for_Fus_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Ca_for_Fus_db.setObjectName("Inut_Ca_for_Fus_db")
        self.verticalLayout_33.addWidget(self.Inut_Ca_for_Fus_db)
        self.Layout_Inut_Ca_for_Fuse_db.addLayout(self.verticalLayout_33)
        self.Fuse_two.addLayout(self.Layout_Inut_Ca_for_Fuse_db)
        self.Layout_Inut_Cpr_for_Fuse_db = QtWidgets.QHBoxLayout()
        self.Layout_Inut_Cpr_for_Fuse_db.setObjectName("Layout_Inut_Cpr_for_Fuse_db")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout()
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.label_P_2 = QtWidgets.QLabel(self.widget)
        self.label_P_2.setObjectName("label_P_2")
        self.verticalLayout_34.addWidget(self.label_P_2)
        self.Inut_Cpr_for_Fus_db = QtWidgets.QLineEdit(self.widget)
        self.Inut_Cpr_for_Fus_db.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border: none;\n"
"border-bottom: 2px solid #E0E0E0;\n"
"")
        self.Inut_Cpr_for_Fus_db.setObjectName("Inut_Cpr_for_Fus_db")
        self.verticalLayout_34.addWidget(self.Inut_Cpr_for_Fus_db)
        self.Layout_Inut_Cpr_for_Fuse_db.addLayout(self.verticalLayout_34)
        self.Fuse_two.addLayout(self.Layout_Inut_Cpr_for_Fuse_db)
        self.chemical_comp_for_fuse.addLayout(self.Fuse_two)
        self.Layout_for_forms.addLayout(self.chemical_comp_for_fuse)
        self.gridLayout.addLayout(self.Layout_for_forms, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.retranslateUi(DialogCreate_Db)
        self.buttonBox.accepted.connect(DialogCreate_Db.accept) # type: ignore
        self.buttonBox.rejected.connect(DialogCreate_Db.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogCreate_Db)

    def retranslateUi(self, DialogCreate_Db):
        _translate = QtCore.QCoreApplication.translate
        DialogCreate_Db.setWindowTitle(_translate("DialogCreate_Db", "Dialog"))
        self.ComboBox_For_DbModels.setItemText(0, _translate("DialogCreate_Db", "КоэфУсв"))
        self.ComboBox_For_DbModels.setItemText(1, _translate("DialogCreate_Db", "ХимСостав"))
        self.ComboBox_For_DbModels.setItemText(2, _translate("DialogCreate_Db", "Проволока"))
        self.ComboBox_For_DbModels.setItemText(3, _translate("DialogCreate_Db", "Марка"))
        self.LabelName.setText(_translate("DialogCreate_Db", "Name"))
        self.label_C.setText(_translate("DialogCreate_Db", "C"))
        self.label_Mn.setText(_translate("DialogCreate_Db", "Mn"))
        self.label_Si.setText(_translate("DialogCreate_Db", "Si"))
        self.label_Cr.setText(_translate("DialogCreate_Db", "Cr"))
        self.label_Ti.setText(_translate("DialogCreate_Db", "Ti"))
        self.label_V.setText(_translate("DialogCreate_Db", "V"))
        self.label_Mo.setText(_translate("DialogCreate_Db", "Mo"))
        self.label_B.setText(_translate("DialogCreate_Db", "B"))
        self.label_Nb.setText(_translate("DialogCreate_Db", "Nb"))
        self.label_Ni.setText(_translate("DialogCreate_Db", "Ni"))
        self.label_Cu.setText(_translate("DialogCreate_Db", "Cu"))
        self.label_Al.setText(_translate("DialogCreate_Db", "Al"))
        self.label_S.setText(_translate("DialogCreate_Db", "S"))
        self.label_Fe.setText(_translate("DialogCreate_Db", "Fe"))
        self.label_Ca.setText(_translate("DialogCreate_Db", "Ca"))
        self.label_P.setText(_translate("DialogCreate_Db", "P"))
        self.label_tcn.setText(_translate("DialogCreate_Db", "Тех-карта"))
        self.label_FuseName.setText(_translate("DialogCreate_Db", "Марка"))
        self.label_TempVd.setText(_translate("DialogCreate_Db", "Вд"))
        self.label_Temp_ccm1.setText(_translate("DialogCreate_Db", "Мнлз-1"))
        self.label_Temp_ccm2.setText(_translate("DialogCreate_Db", "Мнлз-2"))
        self.label_C_2.setText(_translate("DialogCreate_Db", "C"))
        self.label_Mn_2.setText(_translate("DialogCreate_Db", "Mn"))
        self.label_Si_2.setText(_translate("DialogCreate_Db", "Si"))
        self.label_Cr_2.setText(_translate("DialogCreate_Db", "Cr"))
        self.label_Ti_2.setText(_translate("DialogCreate_Db", "Ti"))
        self.label_V_2.setText(_translate("DialogCreate_Db", "V"))
        self.label_Mo_2.setText(_translate("DialogCreate_Db", "Mo"))
        self.label_B_2.setText(_translate("DialogCreate_Db", "B"))
        self.label_Nb_2.setText(_translate("DialogCreate_Db", "Nb"))
        self.label_Ni_2.setText(_translate("DialogCreate_Db", "Ni"))
        self.label_Cu_2.setText(_translate("DialogCreate_Db", "Cu"))
        self.label_Al_2.setText(_translate("DialogCreate_Db", "Al"))
        self.label_S_2.setText(_translate("DialogCreate_Db", "S"))
        self.label_Ca_2.setText(_translate("DialogCreate_Db", "Ca"))
        self.label_P_2.setText(_translate("DialogCreate_Db", "Cpr"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogCreate_Db = QtWidgets.QDialog()
    ui = Ui_DialogCreate_Db()
    ui.setupUi(DialogCreate_Db)
    DialogCreate_Db.show()
    sys.exit(app.exec_())
