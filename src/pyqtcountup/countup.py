from qtpy.QtWidgets import QLabel
from qtpy.QtCore import QTimeLine, QEasingCurve, Signal, QObject
from .utils import Utils


class CountUp(QObject):

    finished = Signal()

    def __init__(self, label: QLabel, start_value: int | float = 0, end_value: int | float = 100,
                 duration: int = 1000, decimal_places: int = 0, decimal: str = '.',
                 thousands_separator: str = '', prefix: str = '', prefix_before_minus: bool = True,
                 suffix: str = '', easing: QEasingCurve.Type | None = QEasingCurve.Type.OutCubic):
        super(CountUp, self).__init__(None)

        self.label = label
        self.start_value = start_value
        self.end_value = end_value
        self.duration = duration
        self.decimal_places = decimal_places
        self.decimal = decimal
        self.thousands_separator = thousands_separator
        self.prefix = prefix
        self.prefix_before_minus = prefix_before_minus
        self.suffix = suffix
        self.easing = easing

        self.value = 0
        self.is_running = False
        self.timeline = QTimeLine(self.duration, self.label)
        self.timeline.setDuration(duration)

        if easing is None:
            self.timeline.setEasingCurve(QEasingCurve.Type.Linear)
        else:
            self.timeline.setEasingCurve(easing)

        self.timeline.frameChanged.connect(lambda v: self.__frame_changed(v))
        self.timeline.finished.connect(self.__timeline_finished)

    def start(self):
        frame_range_start = Utils.get_timeline_value_from_value(self.start_value, self.decimal_places)
        frame_range_end = Utils.get_timeline_value_from_value(self.end_value, self.decimal_places)
        self.timeline.setFrameRange(frame_range_start, frame_range_end)
        self.__frame_changed(frame_range_start)
        self.is_running = True
        self.timeline.start()

    def update(self, new_end_value: int):
        self.timeline.stop()
        self.setStartValue(self.value)
        self.setEndValue(new_end_value)
        self.start()

    def pause(self):
        self.timeline.setPaused(True)
        self.is_running = False

    def resume(self):
        self.is_running = True
        self.timeline.resume()

    def stop(self):
        self.timeline.stop()
        self.is_running = False

    def reset(self):
        self.timeline.stop()
        self.is_running = False
        self.__frame_changed(Utils.get_timeline_value_from_value(self.start_value, self.decimal_places))

    def getLabel(self) -> QLabel:
        return self.label

    def setLabel(self, label: QLabel):
        self.label = label

    def getStartValue(self) -> int | float:
        return self.start_value

    def setStartValue(self, start_value: int | float):
        self.start_value = start_value

    def getEndValue(self) -> int | float:
        return self.end_value

    def setEndValue(self, end_value: int | float):
        self.end_value = end_value

    def setStartEndValues(self, start_value: int | float, end_value: int | float):
        self.start_value = start_value
        self.end_value = end_value

    def getDuration(self) -> int:
        return self.duration

    def setDuration(self, duration: int):
        self.duration = duration
        self.timeline.setDuration(duration)

    def getDecimalPlaces(self) -> int:
        return self.decimal_places

    def setDecimalPlaces(self, decimal_places: int):
        self.decimal_places = decimal_places

    def getDecimal(self) -> str:
        return self.decimal

    def setDecimal(self, decimal: str):
        self.decimal = decimal

    def getThousandsSeparator(self) -> str:
        return self.thousands_separator

    def setThousandsSeparator(self, thousands_separator: str):
        self.thousands_separator = thousands_separator

    def getPrefix(self) -> str:
        return self.prefix

    def setPrefix(self, prefix: str):
        self.prefix = prefix

    def isPrefixBeforeMinus(self) -> bool:
        return self.prefix_before_minus

    def setPrefixBeforeMinus(self, enabled: bool):
        self.prefix_before_minus = enabled

    def getSuffix(self) -> str:
        return self.suffix

    def setSuffix(self, suffix: str):
        self.suffix = suffix

    def getEasing(self) -> QEasingCurve.Type | None:
        return self.easing

    def setEasing(self, easing: QEasingCurve.Type | None):
        self.easing = easing
        if easing is None:
            self.timeline.setEasingCurve(QEasingCurve.Type.Linear)
        else:
            self.timeline.setEasingCurve(easing)

    def isRunning(self) -> bool:
        return self.is_running

    def __frame_changed(self, timeline_value: int):
        value = Utils.get_value_from_timeline_value(timeline_value, self.decimal_places)
        self.value = value
        value_string = Utils.format_value(value, self.decimal_places,
                                          self.decimal, self.thousands_separator)

        if not self.prefix_before_minus and value < 0:
            value_string = value_string[1:]
            full_string = "-" + self.prefix + value_string + self.suffix
        else:
            full_string = self.prefix + value_string + self.suffix

        self.label.setText(full_string)

    def __timeline_finished(self):
        self.is_running = False
        self.finished.emit()
