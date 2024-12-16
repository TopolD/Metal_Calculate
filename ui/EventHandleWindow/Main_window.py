

from PyQt5.QtCore import QRect, QPropertyAnimation, QEvent, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui.EventHandleWindow.EventHandlerForLrf import DisplayHandlerLrf
from ui.EventHandleWindow.EventHandlerForDilution import DisplayHandlerDilution
from ui.EventHandleWindow.EventHadnlerForFormuls import DisplayHandlerFormuls

from ui.Designe.WindowM import *


class AllWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AllWindow, self).__init__()
        self.setupUi(self)

        self.setStyleSheet(("""
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
                background-color: #A9A9A9; /* Серый цвет при наведении */
                border-color: #808080; /* Более темная граница */
            }
        """))

        self.popup_window = self.WIdget_for_radio_Button
        self.popup_window.setGeometry(0, 0, 0, 0)
        self.popup_window.setStyleSheet("""
            QWidget {
                background-color: white;
                color: black;
                border: 2px ;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
            }""")

        self.animation = QPropertyAnimation(self.popup_window, b"geometry")
        self.animation.setDuration(300)


        self.hide_timer = QTimer(self)
        self.hide_timer.setInterval(200)
        self.hide_timer.setSingleShot(True)
        self.hide_timer.timeout.connect(self.hide_popup)

        self.Main_button_for_RadButton.installEventFilter(self)

        self.popup_window.installEventFilter(self)

        self.popup_x = 65
        self.popup_y = 8
        self.popup_width = 160
        self.popup_height = 35

        self.init_radio_button()
        self.Lrf1_RadButton.setChecked(True)

    def init_radio_button(self):
        self.Lrf1_RadButton.toggled.connect(self.on_radio_toggled)
        self.Lrf2_RadButton.toggled.connect(self.on_radio_toggled)
        self.Buck_RadButton.toggled.connect(self.on_radio_toggled)
        self.Form_RadButton.toggled.connect(self.on_radio_toggled)
        self.Note_RadButton.toggled.connect(self.on_radio_toggled)

    def on_radio_toggled(self, checked):
        sender = self.sender()
        if checked:
            self.show_window(sender.objectName())

    def update_layout(self, name_layout):
        match name_layout:
            case 'Lrf':
                layout_width = DisplayHandlerLrf().AllLrf.sizeHint().width()
                layout_height = DisplayHandlerLrf().AllLrf.sizeHint().height()
                self.widget_For_main_window.resize(layout_width + 90, layout_height + 100)
                self.resize(layout_width + 90, layout_height + 80)
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
                self.resize(layout_width + 250, layout_height + 70)
                self.updateGeometry()
            case _:
                pass


    def show_window(self, name_window):



        match name_window:
            case 'Lrf1_RadButton':
                display_handler_lrf = DisplayHandlerLrf()
                self.update_layout('Lrf')
                self.layout_for_main_window.addWidget(display_handler_lrf)
            case 'Lrf2_RadButton':
                display_handler_lrf = DisplayHandlerLrf()
                self.update_layout('Lrf')
                self.layout_for_main_window.addWidget(display_handler_lrf)
            case 'Buck_RadButton':
                display_handler_Dil = DisplayHandlerDilution()
                self.update_layout('Dil')
                self.layout_for_main_window.addWidget(display_handler_Dil)
            case 'Form_RadButton':
                display_handler_Form = DisplayHandlerFormuls()
                self.update_layout('Form')
                self.layout_for_main_window.addWidget(display_handler_Form)
            case 'Note_RadButton':
                pass


    def eventFilter(self, source, event):
        if source == self.Main_button_for_RadButton:
            if event.type() == QEvent.Enter:
                self.hide_timer.stop()
                self.show_popup()
            elif event.type() == QEvent.Leave:
                self.hide_timer.start()
        elif source == self.popup_window:
            if event.type() == QEvent.Enter:
                self.hide_timer.stop()
            elif event.type() == QEvent.Leave:
                self.hide_timer.start()
        return super().eventFilter(source, event)

    def show_popup(self):

        self.animation.setStartValue(QRect(self.popup_x, self.popup_y, 0, self.popup_height))
        self.animation.setEndValue(QRect(self.popup_x, self.popup_y, self.popup_width, self.popup_height))
        self.animation.start()

    def hide_popup(self):

        self.animation.setStartValue(self.popup_window.geometry())
        self.animation.setEndValue(QRect(self.popup_x, self.popup_y, 0, self.popup_height))
        self.animation.start()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    main_window = AllWindow()
    main_window.show()

    sys.exit(app.exec_())
