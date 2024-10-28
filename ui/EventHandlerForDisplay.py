from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QRect
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

        self.line_edit_handler_for_display()
        self.animation_buttons()

        # Убедимся, что виджет с кнопками изначально скрыт
        self.Widget_for_maint_button.setVisible(False)

        # Обработка событий для кнопки
        self.pushButton_6.enterEvent = self.show_buttons
        self.pushButton_6.leaveEvent = self.hide_buttons

        self.is_animating = False  # Флаг для отслеживания состояния анимации

    def animation_buttons(self):
        """Настройка анимации для контейнера с кнопками."""
        self.container_animation = QPropertyAnimation(self.Widget_for_maint_button, b'geometry')
        self.container_animation.setDuration(300)  # Длительность анимации
        self.container_animation.setEasingCurve(QEasingCurve.OutCubic)  # Эффект анимации

    def show_buttons(self, event):
        """Плавно показывает контейнер с кнопками при наведении на pushButton_6."""
        if not self.Widget_for_maint_button.isVisible():  # Проверяем, виден ли контейнер
            self.Widget_for_maint_button.setVisible(True)  # Показываем контейнер
            self.container_animation.stop()  # Останавливаем анимацию перед началом
            # Устанавливаем начальную и конечную геометрию для анимации
            self.container_animation.setStartValue(QRect(self.pushButton_6.x() + self.pushButton_6.width(),
                                                         self.pushButton_6.y(),
                                                         0,
                                                         self.Widget_for_maint_button.height()))
            self.container_animation.setEndValue(QRect(self.pushButton_6.x() + self.pushButton_6.width(),
                                                       self.pushButton_6.y(),
                                                       200,  # конечная ширина
                                                       self.Widget_for_maint_button.height()))
            self.container_animation.start()  # Запускаем анимацию
            self.is_animating = True  # Устанавливаем флаг анимации

    def hide_buttons(self, event):
        """Плавно скрывает контейнер с кнопками при уходе курсора с pushButton_6."""
        if self.Widget_for_maint_button.isVisible():  # Проверяем, виден ли контейнер
            self.container_animation.stop()  # Останавливаем предыдущую анимацию, если есть
            # Устанавливаем начальные и конечные значения для анимации скрытия
            self.container_animation.setStartValue(self.Widget_for_maint_button.geometry())
            self.container_animation.setEndValue(QRect(self.pushButton_6.x() + self.pushButton_6.width(),
                                                       self.pushButton_6.y(),
                                                       0,  # конечная ширина для скрытия
                                                       self.Widget_for_maint_button.height()))
            self.container_animation.start()  # Запускаем анимацию
            self.is_animating = True  # Устанавливаем флаг анимации
            self.container_animation.finished.connect(self.hide_widget)  # Скрываем виджет после завершения анимации

    def hide_widget(self):
        """Скрывает виджет после завершения анимации."""
        self.Widget_for_maint_button.setVisible(False)  # Скрываем контейнер
        self.is_animating = False  # Сбрасываем флаг анимации
        self.container_animation.finished.disconnect()  # Отключаем сигн




    def line_edit_handler_for_display(self):
        self.InputTechCard.setValidator(QIntValidator(0, 999))
        self.InputTechCard.editingFinished.connect(self.InputClass.handle_input)

        self.InputWeight.setValidator(QDoubleValidator(0.0, 200.0, 2))
        self.InputWeight.editingFinished.connect(self.line_edit_handler_for_calculate)

    def line_edit_handler_for_calculate(self):
        material_list = self.OutputClass.elements_visible_list
        for material in material_list:
            InputLineEditName = f'LabelSamplesFor{material}'
            initial_line_edit = getattr(self, InputLineEditName, None)
            if initial_line_edit:
                initial_line_edit.setValidator(QDoubleValidator(0.0, 4.0, 3))
                initial_line_edit.editingFinished.connect(
                    lambda line_edit=initial_line_edit, mat=material: self.handle_input(line_edit, mat))
            Material_Box = f'MaterialFor{material}'
            Material_Box_edit = getattr(self, Material_Box, None)
            if Material_Box_edit:
                Material_Box_edit.currentIndexChanged.connect(
                    lambda _, mat=material, box=Material_Box_edit: self.handle_material_change(mat, box)
                )
        self.OutputClass.samples_dict['W'] = self.InputWeight.text()
        self.CalculateClass.Handler_for_calculate(self.OutputClass.samples_dict)

    def handle_input(self, line_edit, material):

        Material_Box = f'MaterialFor{material}'
        Material_Box_edit = getattr(self, Material_Box, None)
        material_box_value = Material_Box_edit.currentText()

        input_value = line_edit.text()
        if input_value:
            self.OutputClass.samples_dict['samples'][material] = input_value
            self.OutputClass.samples_dict['material'][material] = material_box_value
            self.OutputClass.samples_dict['W'] = self.InputWeight.text()
            self.CalculateClass.Handler_for_calculate(self.OutputClass.samples_dict)
            print(self.OutputClass.samples_dict)

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

    def __init__(self, parent):
        self.parent = parent
        self.samples_dict = {
            'W': self.parent.InputWeight.text(),
            'samples': {},
            'material': {},
            'corewire': {
                'C': 0,
                'Al': 0,
                'Ti': 0
            }
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

    main_window = DisplayHandler()
    main_window.show()

    sys.exit(app.exec_())
