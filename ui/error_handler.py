from PyQt5.QtCore import QPropertyAnimation, QRect


class error_handler():

    def update_border_for_error(self, widget, error):
        style = self.get_error_stylesheet(error)
        widget.setStyleSheet(style)

        if error:
            widget.clear()
            self.animate_vibrate(widget)

    def get_error_stylesheet(self, error):
        if isinstance(error, AttributeError):
            return """
                   QLineEdit{
                       background-color: rgb(255, 255, 255);
                       border: none;
                       border-bottom: 2px solid #FFA5A5;
                   }
               """
        return """
               QLineEdit{
                   background-color: rgb(255, 255, 255);
                   border: none;
                   border-bottom: 2px solid #E0E0E0;
               }
           """

    def animate_vibrate(self, widget):
        self.animation = QPropertyAnimation(widget, b"geometry")
        original_geometry = widget.geometry()
        self.animation.setDuration(200)
        self.animation.setKeyValueAt(0, original_geometry)
        self.animation.setKeyValueAt(0.25,
                                     QRect(original_geometry.x() - 10, original_geometry.y(), original_geometry.width(),
                                           original_geometry.height()))
        self.animation.setKeyValueAt(0.5, original_geometry)
        self.animation.setKeyValueAt(0.75,
                                     QRect(original_geometry.x() + 10, original_geometry.y(), original_geometry.width(),
                                           original_geometry.height()))
        self.animation.setKeyValueAt(1, original_geometry)
        self.animation.start()