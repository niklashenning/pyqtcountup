from qtpy.QtWidgets import QLabel
from qtpy.QtCore import QTimeLine, QEasingCurve
from .utils import Utils


class CountUp:

    def __init__(self, label: QLabel, from_value: int | float = 0, to_value: int | float = 100,
                 duration: int = 1000, decimals: int = 0, decimal_point: str = '.',
                 thousands_separator: str = '', prefix: str = '',
                 prefix_before_minus: bool = True, suffix: str = ''):
        self.label = label
        self.from_value = from_value
        self.to_value = to_value
        self.duration = duration
        self.decimals = decimals
        self.decimal_point = decimal_point
        self.thousands_separator = thousands_separator
        self.prefix = prefix
        self.prefix_before_minus = prefix_before_minus
        self.suffix = suffix

    def start(self):
        def frame_changed(timeline_value):
            value = Utils.get_value_from_timeline_value(timeline_value, self.decimals)
            value_string = Utils.format_value(value, self.decimals,
                                              self.decimal_point, self.thousands_separator)

            if not self.prefix_before_minus and value < 0:
                value_string = value_string[1:]
                full_string = "-" + self.prefix + value_string + self.suffix
            else:
                full_string = self.prefix + value_string + self.suffix

            self.label.setText(full_string)

        frame_range_start = Utils.get_timeline_value_from_value(self.from_value, self.decimals)
        frame_range_end = Utils.get_timeline_value_from_value(self.to_value, self.decimals)

        timeline = QTimeLine(self.duration, self.label)
        timeline.setFrameRange(frame_range_start, frame_range_end)
        timeline.setEasingCurve(QEasingCurve.Type.OutCubic)
        timeline.frameChanged.connect(frame_changed)
        timeline.start()

    def pause(self):
        pass

    def resume(self):
        pass

    def stop(self):
        pass

    def reset(self):
        pass

    def setLabel(self, label: QLabel):
        self.label = label

    def setFromValue(self, from_value: int | float):
        self.from_value = from_value

    def setToValue(self, to_value: int | float):
        self.to_value = to_value

    def setDuration(self, duration: int):
        self.duration = duration

    def setDecimals(self, decimals: int):
        self.decimals = decimals

    def setDecimalPoint(self, decimal_point: str):
        self.decimal_point = decimal_point

    def setThousandsSeparator(self, thousands_separator: str):
        self.thousands_separator = thousands_separator

    def setPrefix(self, prefix: str):
        self.prefix = prefix

    def setPrefixBeforeMinus(self, enabled: bool):
        self.prefix_before_minus = enabled

    def setSuffix(self, suffix: str):
        self.suffix = suffix
