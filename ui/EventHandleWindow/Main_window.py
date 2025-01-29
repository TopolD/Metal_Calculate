from PyQt5.QtCore import QRect, QPropertyAnimation, QEvent, QTimer

from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

from ui.Designe.WindowM import Ui_Calculate
from ui.EventHandleWindow.EventHandlerForLrf import DisplayHandlerLrf
from ui.EventHandleWindow.EventHandlerForDilution import DisplayHandlerDilution
from ui.EventHandleWindow.EventHadnlerForFormuls import DisplayHandlerFormuls
from ui.EventHandleWindow.handler_requests_db.AddDb import Dialog_Add
from ui.EventHandleWindow.handler_requests_db.DelDb import Dialog_Del
from ui.EventHandleWindow.handler_requests_db.UpdDb import Dialog_Upd


class AllWindow(QMainWindow, Ui_Calculate):
    def __init__(self):
        super(AllWindow, self).__init__()
        self.setupUi(self)

        self.Lrf_1 = DisplayHandlerLrf()
        self.Lrf_2 = DisplayHandlerLrf()

        self.Dil = DisplayHandlerDilution()
        self.Form = DisplayHandlerFormuls()

        self.Mech = WindowMechanics(self)

        StyleForButton(self)

        self.init_radio_button()
        self.Lrf1_RadButton.setChecked(True)

        self.dialog_handler = DialogHandler(self)
        self.initial_button_for_db()




    def initial_button_for_db(self):

        self.Button_For_add_in_Db.clicked.connect(self.dialog_handler.button_called_methods)
        self.Button_For_update_in_Db.clicked.connect(self.dialog_handler.button_called_methods)
        self.Button_For_del_in_Db.clicked.connect(self.dialog_handler.button_called_methods)

    def eventFilter(self, source, event):
        if source == self.Main_button_for_RadButton:
            if event.type() == QEvent.Enter:
                self.Mech.hide_timer_radio.stop()
                self.Mech.show_popup()
            elif event.type() == QEvent.Leave:
                self.Mech.hide_timer_radio.start()
        elif source == self.Mech.radio_button_window:
            if event.type() == QEvent.Enter:
                self.Mech.hide_timer_radio.stop()
            elif event.type() == QEvent.Leave:
                self.Mech.hide_timer_radio.start()
        elif source == self.History_Button:
            if event.type() == QEvent.Enter:
                self.Mech.hide_timer_db.stop()
                self.Mech.show_db()
            elif event.type() == QEvent.Leave:
                self.Mech.hide_timer_db.start()
        elif source == self.Mech.button_for_db:
            if event.type() == QEvent.Enter:
                self.Mech.hide_timer_db.stop()
            elif event.type() == QEvent.Leave:
                self.Mech.hide_timer_db.start()
        return super().eventFilter(source, event)

    def init_radio_button(self):

        for radio_button in [
            self.Lrf1_RadButton,
            self.Lrf2_RadButton,
            self.Buck_RadButton,
            self.Form_RadButton,
            self.Note_RadButton,
        ]:
            radio_button.toggled.connect(self.on_radio_toggled)

    def on_radio_toggled(self, checked):
        sender = self.sender()
        if checked:
            self.show_window(sender.objectName())

    def show_window(self, name_window):
        match name_window:
            case 'Lrf1_RadButton':
                self.initial_display_handler(self.Lrf_1)
                self.Lrf_1.label.setText('LRF-1')
                self.History_Button.setHidden(False)
                self.update_layout('Lrf')

            case 'Lrf2_RadButton':
                self.initial_display_handler(self.Lrf_2)
                self.Lrf_2.label.setText('LRF-2')
                self.History_Button.setHidden(False)
                self.update_layout('Lrf')

            case 'Buck_RadButton':
                self.initial_display_handler(self.Dil)
                self.History_Button.setHidden(True)
                self.update_layout('Dil')

            case 'Form_RadButton':
                self.initial_display_handler(self.Form)
                self.History_Button.setHidden(True)
                self.update_layout('Form')
            case 'Note_RadButton':
                self.History_Button.setHidden(True)
                pass

    def update_layout(self, name_layout):
        match name_layout:
            case 'Lrf':
                layout_width = DisplayHandlerLrf().AllLrf.sizeHint().width()
                layout_height = DisplayHandlerLrf().AllLrf.sizeHint().height()
                self.widget_For_main_window.resize(layout_width + 90, layout_height + 100)
                self.resize(layout_width + 110, layout_height + 80)
                self.updateGeometry()
            case 'Dil':
                layout_width = DisplayHandlerFormuls().FormulsLayout.sizeHint().width()
                layout_height = DisplayHandlerFormuls().FormulsLayout.sizeHint().height()
                self.widget_For_main_window.resize(layout_width + 230, layout_height + 60)
                self.resize(layout_width + 250, layout_height + 70)
                self.updateGeometry()
            case 'Form':
                layout_width = DisplayHandlerFormuls().FormulsLayout.sizeHint().width()
                layout_height = DisplayHandlerFormuls().FormulsLayout.sizeHint().height()
                self.widget_For_main_window.resize(layout_width + 230, layout_height + 60)
                self.resize(layout_width + 250, layout_height + 80)
                self.updateGeometry()
            case _:
                pass

    def initial_display_handler(self, widget_name=None):
        display_handler_list = [
            self.Lrf_1,
            self.Lrf_2,
            self.Dil,
            self.Form
        ]

        for widget in display_handler_list:
            widget.setVisible(False)

            if not self.is_widget_in_layout(widget):
                self.layout_for_main_window.addWidget(widget)

        if widget_name in display_handler_list:
            widget_name.setVisible(True)

    def is_widget_in_layout(self, widget):

        for i in range(self.layout_for_main_window.count()):
            layout_widget = self.layout_for_main_window.itemAt(i).widget()
            if layout_widget == widget:
                return True
        return False


class WindowMechanics:

    def __init__(self, parent):
        self.parent = parent

        self.animation_for_db()
        self.animation_for_rd()

    def animation_for_db(self):
        self.button_for_db = self.parent.Widget_For_Db
        self.button_for_db.setGeometry(0, 0, 0, 0)
        self.animation_db = QPropertyAnimation(self.button_for_db, b"geometry")
        self.animation_db.setDuration(300)

        self.hide_timer_db = QTimer(self.parent)
        self.hide_timer_db.setInterval(200)
        self.hide_timer_db.setSingleShot(True)
        self.hide_timer_db.timeout.connect(self.hide_db)

        self.parent.History_Button.installEventFilter(self.parent)
        self.button_for_db.installEventFilter(self.parent)

        self.popup_x_db = self.parent.History_Button.geometry().x() + 520
        self.popup_y_db = 8
        self.popup_width_db = 100
        self.popup_height_db = 35

    def animation_for_rd(self):
        self.radio_button_window = self.parent.WIdget_for_radio_Button
        self.radio_button_window.setGeometry(0, 0, 0, 0)
        self.radio_button_window.setStyleSheet("""
                    QWidget {
                        background-color: white;
                        color: black;
                        border: 2px;
                        border-radius: 10px;
                        font-size: 14px;
                        font-weight: bold;
                    }""")

        self.animation_radio = QPropertyAnimation(self.radio_button_window, b"geometry")
        self.animation_radio.setDuration(300)

        self.hide_timer_radio = QTimer(self.parent)
        self.hide_timer_radio.setInterval(200)
        self.hide_timer_radio.setSingleShot(True)
        self.hide_timer_radio.timeout.connect(self.hide_popup)

        self.parent.Main_button_for_RadButton.installEventFilter(self.parent)
        self.radio_button_window.installEventFilter(self.parent)

        self.popup_x_radio = 65
        self.popup_y_radio = 8
        self.popup_width_radio = 160
        self.popup_height_radio = 35

    def show_db(self):
        self.animation_db.setStartValue(
            QRect(self.popup_x_db + self.popup_width_db, self.popup_y_db, 0, self.popup_height_db))
        self.animation_db.setEndValue(
            QRect(self.popup_x_db, self.popup_y_db, self.popup_width_db, self.popup_height_db))
        self.animation_db.start()

    def hide_db(self):
        current_geometry = self.button_for_db.geometry()
        self.animation_db.setStartValue(current_geometry)
        self.animation_db.setEndValue(
            QRect(self.popup_x_db + self.popup_width_db, self.popup_y_db, 0, self.popup_height_db))
        self.animation_db.start()

    def show_popup(self):
        self.animation_radio.setStartValue(QRect(self.popup_x_radio, self.popup_y_radio, 0, self.popup_height_radio))
        self.animation_radio.setEndValue(
            QRect(self.popup_x_radio, self.popup_y_radio, self.popup_width_radio, self.popup_height_radio))
        self.animation_radio.start()

    def hide_popup(self):
        self.animation_radio.setStartValue(self.radio_button_window.geometry())
        self.animation_radio.setEndValue(QRect(self.popup_x_radio, self.popup_y_radio, 0, self.popup_height_radio))
        self.animation_radio.start()


class StyleForButton:

    def __init__(self, parent):
        self.parent = parent

        self.parent.Lrf1_RadButton.setStyleSheet("""
                QRadioButton::indicator {
                    width: 30px;
                    height: 30px;
                    background-image: url('../icons/fire/fire.svg');
                    background-size: 10px 10px; 
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
                }
                 QRadioButton::indicator:hover {
                    width: 30px;
                    height: 30px;
                    background-image: url('../icons/fire/fire_hover.svg');
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
    
                }
                 QRadioButton::indicator:checked  {
                    width: 30px;
                    height: 30px;
                    background-image: url('../icons/fire/fire_checked.svg');
                    background-size: 10px 10px; 
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
    
                }
            """)
        self.parent.Lrf2_RadButton.setStyleSheet("""
                QRadioButton::indicator {
                    width: 30px;
                    height: 30px;
                    background-image: url('../icons/fire/fire.svg');
                    background-size: 10px 10px; 
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
                }
                 QRadioButton::indicator:hover {
                    width: 30px;
                    height: 30px;
                    background-image: url('../icons/fire/fire_hover.svg');
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
    
                }
                 QRadioButton::indicator:checked  {
                    width: 30px;
                    height: 30px;
                    background-image: url('../icons/fire/fire_checked.svg');
                    background-size: 10px 10px; 
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
    
                }
            """)
        self.parent.Widget_For_Db.setStyleSheet("""
            QWidget {
                background-color: white;
                color: black; 
                border: 2px;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            
            QPushButton:hover {
                background-color: #A9A9A9; 
                border-color: #808080; 
            }
            QPushButton:pressed {
                background-color: #696969; 
                border-color: #808080; 
            }
            
        """)

        self.parent.setStyleSheet(("""
                QPushButton {
                    background-color: white;
                    color: black;
                    border: 2px ;
                    border-radius: 10px;
                    padding: 8px 16px;
                    font-size: 14px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #A9A9A9; 
                    border-color: #808080; 
                }
    
    
            """))

        self.parent.Buck_RadButton.setStyleSheet("""
                QRadioButton::indicator {
                    width: 30px;
                    height: 30px;
                    background-image: url('../icons/bucket/bucket.svg');
                    background-size: 10px 10px; 
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
                }
                 QRadioButton::indicator:hover {
                    width: 30px;
                    height: 30px;
                    background-image: url('../icons/bucket/bucket_hover.svg');
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
    
                }
                 QRadioButton::indicator:checked  {
                    width: 30px;
                    height: 30px;
                    background-image: url('../icons/bucket/bucket_checked.svg');
                    background-size: 10px 10px; 
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
    
                }
            """)

        self.parent.Form_RadButton.setStyleSheet("""
                QRadioButton::indicator {
                    width: 30px;
                    height: 30px;
                    background-image: url('../icons/atom/atom.svg');
                    background-size: 10px 10px; 
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
                }
                 QRadioButton::indicator:hover {
                    width: 30px;
                    height: 30px;
                    background-image: url('../icons/atom/atom_hover.svg');
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
    
                }
                 QRadioButton::indicator:checked  {
                    width: 30px;
                    height: 30px;
                    background-image: url('../icons/atom/atom_checked.svg');
                    background-size: 10px 10px; 
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
    
                }
            """)

        self.parent.Note_RadButton.setStyleSheet("""
                QRadioButton::indicator {
                    width: 30px;
                    height: 30px;
                    background-image: url('../icons/note/note.svg');
                    background-size: 10px 10px; 
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
                }
                 QRadioButton::indicator:hover {
                    width: 30px;
                    height: 30px;
                    background-image: url('../icons/note/note_hover.svg');
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
    
                }
                 QRadioButton::indicator:checked  {
                    width: 30px;
                    height: 30px;
                    background-image: url('../icons/note/note_checked.svg');
                    background-size: 10px 10px; 
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
    
                }
            """)


class DialogHandler(QDialog):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def button_called_methods(self,checked):
        button = self.sender()
        if button:
            self.show_dialog_window(button.objectName())
    def show_dialog_window(self, dialog_name):
        match dialog_name:
            case 'Button_For_add_in_Db':
                dialog = Dialog_Add()
                dialog.exec_()
            case 'Button_For_update_in_Db':
                dialog = Dialog_Upd()
                dialog.exec_()
            case 'Button_For_del_in_Db':
                dialog = Dialog_Del()
                dialog.exec_()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main_window = AllWindow()
    main_window.show()

    sys.exit(app.exec_())
