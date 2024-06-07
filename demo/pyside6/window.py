from PySide6.QtCore import Qt, QEasingCurve
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QMainWindow, QPushButton, QComboBox, QVBoxLayout, QCheckBox, QWidget,
                               QSpinBox, QLineEdit, QHBoxLayout, QLabel, QFormLayout, QDoubleSpinBox)
from pyqtcountup import CountUp


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        # Window settings
        self.setWindowTitle('PyQt CountUp Demo')

        # Create map for easing curves
        self.easing_curve_ignore_list = ['Custom', 'TCBSpline', 'BezierSpline', 'NCurveTypes',
                                         'InCurve', 'OutCurve', 'SineCurve', 'CosineCurve']
        self.easing_curve_map = {}
        for key, value in vars(QEasingCurve.Type).items():
            if isinstance(value, QEasingCurve.Type) and key not in self.easing_curve_ignore_list:
                self.easing_curve_map[key] = value

        # Create label
        self.countup_label = QLabel()
        self.countup_label.setText('0')
        self.countup_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.countup_label.setFont(QFont('System Regular', 30))
        self.countup_label.setContentsMargins(0, 0, 0, 25)

        # Init CountUp
        self.countup = CountUp(self.countup_label)
        self.countup.finished.connect(lambda: print('finished'))

        # Create layouts
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.countup_label)
        main_layout.addLayout(self.create_settings_layout())
        main_layout.addLayout(self.create_button_layout())
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.setContentsMargins(25, 25, 25, 25)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.setFocus()

    def start_animation(self):
        self.countup.setStartValue(self.start_value_input.value())
        self.countup.setEndValue(self.end_value_input.value())
        self.update_settings()
        self.countup.start()

    def pause_animation(self):
        self.countup.pause()

    def resume_animation(self):
        self.update_settings()
        self.countup.resume()

    def stop_animation(self):
        self.countup.stop()

    def reset_animation(self):
        self.update_settings()
        self.countup.reset()

    def update_animation(self):
        self.update_settings()
        self.countup.update(self.update_value_input.value())

    def update_settings(self):
        self.countup.setDuration(self.duration_input.value())
        self.countup.setDecimalPlaces(self.decimal_places_input.value())
        self.countup.setDecimal(self.decimal_input.text())
        self.countup.setSeparator(self.separator_input.text())
        self.countup.setPrefix(self.prefix_input.text())
        self.countup.setPrefixBeforeMinus(self.prefix_before_minus_checkbox.isChecked())
        self.countup.setSuffix(self.suffix_input.text())
        self.countup.setEasing(self.easing_curve_map[self.easing_combobox.currentText()])

    def create_settings_layout(self):
        self.start_value_input = QDoubleSpinBox()
        self.start_value_input.setRange(-10000000, 10000000)

        self.end_value_input = QDoubleSpinBox()
        self.end_value_input.setRange(-10000000, 10000000)
        self.end_value_input.setValue(7924)

        self.duration_input = QSpinBox()
        self.duration_input.setRange(0, 10000000)
        self.duration_input.setValue(2000)

        self.decimal_places_input = QSpinBox()
        self.decimal_places_input.setMinimum(0)

        self.decimal_input = QLineEdit('.')

        self.separator_input = QLineEdit()

        self.prefix_input = QLineEdit()

        self.prefix_before_minus_checkbox = QCheckBox('Prefix before minus')
        self.prefix_before_minus_checkbox.setChecked(True)

        self.suffix_input = QLineEdit()

        self.easing_combobox = QComboBox()

        for key, value in self.easing_curve_map.items():
            self.easing_combobox.addItem(key)
            if value == self.countup.getEasing():
                self.easing_combobox.setCurrentText(key)

        form_layout_1 = QFormLayout()
        form_layout_1.addRow('Start value:', self.start_value_input)
        form_layout_1.addRow('Duration:', self.duration_input)
        form_layout_1.addRow('Decimal:', self.decimal_input)
        form_layout_1.addRow('Prefix:', self.prefix_input)
        form_layout_1.addWidget(self.prefix_before_minus_checkbox)
        form_layout_1.setContentsMargins(0, 0, 35, 0)

        form_layout_2 = QFormLayout()
        form_layout_2.addRow('End value:', self.end_value_input)
        form_layout_2.addRow('Decimal places:', self.decimal_places_input)
        form_layout_2.addRow('Separator:', self.separator_input)
        form_layout_2.addRow('Suffix:', self.suffix_input)
        form_layout_2.addRow('Easing: ', self.easing_combobox)

        settings_layout = QHBoxLayout()
        settings_layout.addLayout(form_layout_1)
        settings_layout.addLayout(form_layout_2)
        settings_layout.setContentsMargins(0, 0, 0, 15)

        return settings_layout

    def create_button_layout(self):
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_animation)

        self.pause_button = QPushButton('Pause')
        self.pause_button.clicked.connect(self.pause_animation)

        self.resume_button = QPushButton('Resume')
        self.resume_button.clicked.connect(self.resume_animation)

        self.stop_button = QPushButton('Stop')
        self.stop_button.clicked.connect(self.stop_animation)

        self.reset_button = QPushButton('Reset')
        self.reset_button.clicked.connect(self.reset_animation)

        self.update_button = QPushButton('Update')
        self.update_button.clicked.connect(self.update_animation)

        self.update_value_input = QDoubleSpinBox()
        self.update_value_input.setRange(-10000000, 10000000)
        self.update_value_input.setValue(6789)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.resume_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.reset_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.update_value_input)

        return button_layout
