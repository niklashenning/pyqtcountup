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

        self.__label = label
        self.__start_value = start_value
        self.__end_value = end_value
        self.__duration = duration
        self.__decimal_places = decimal_places
        self.__decimal = decimal
        self.__thousands_separator = thousands_separator
        self.__prefix = prefix
        self.__prefix_before_minus = prefix_before_minus
        self.__suffix = suffix
        self.__easing = easing

        self.__value = 0
        self.__is_running = False
        self.__timeline = QTimeLine(self.__duration, self.__label)
        self.__timeline.setDuration(duration)

        if easing is None:
            self.__timeline.setEasingCurve(QEasingCurve.Type.Linear)
        else:
            self.__timeline.setEasingCurve(easing)

        self.__timeline.frameChanged.connect(lambda v: self.__frame_changed(v))
        self.__timeline.finished.connect(self.__timeline_finished)

    def start(self):
        frame_range_start = Utils.get_timeline_value_from_value(self.__start_value, self.__decimal_places)
        frame_range_end = Utils.get_timeline_value_from_value(self.__end_value, self.__decimal_places)
        self.__timeline.setFrameRange(frame_range_start, frame_range_end)
        self.__frame_changed(frame_range_start)
        self.__is_running = True
        self.__timeline.start()

    def update(self, new_end_value: int):
        self.__timeline.stop()
        self.setStartValue(self.__value)
        self.setEndValue(new_end_value)
        self.start()

    def pause(self):
        self.__timeline.setPaused(True)
        self.__is_running = False

    def resume(self):
        self.__is_running = True
        self.__timeline.resume()

    def stop(self):
        self.__timeline.stop()
        self.__is_running = False

    def reset(self):
        self.__timeline.stop()
        self.__is_running = False
        self.__frame_changed(Utils.get_timeline_value_from_value(self.__start_value, self.__decimal_places))

    def getLabel(self) -> QLabel:
        return self.__label

    def setLabel(self, label: QLabel):
        self.__label = label

    def getStartValue(self) -> int | float:
        return self.__start_value

    def setStartValue(self, start_value: int | float):
        self.__start_value = start_value

    def getEndValue(self) -> int | float:
        return self.__end_value

    def setEndValue(self, end_value: int | float):
        self.__end_value = end_value

    def setStartEndValues(self, start_value: int | float, end_value: int | float):
        self.__start_value = start_value
        self.__end_value = end_value

    def getDuration(self) -> int:
        return self.__duration

    def setDuration(self, duration: int):
        self.__duration = duration
        self.__timeline.setDuration(duration)

    def getDecimalPlaces(self) -> int:
        return self.__decimal_places

    def setDecimalPlaces(self, decimal_places: int):
        self.__decimal_places = decimal_places

    def getDecimal(self) -> str:
        return self.__decimal

    def setDecimal(self, decimal: str):
        self.__decimal = decimal

    def getThousandsSeparator(self) -> str:
        return self.__thousands_separator

    def setThousandsSeparator(self, thousands_separator: str):
        self.__thousands_separator = thousands_separator

    def getPrefix(self) -> str:
        return self.__prefix

    def setPrefix(self, prefix: str):
        self.__prefix = prefix

    def isPrefixBeforeMinus(self) -> bool:
        return self.__prefix_before_minus

    def setPrefixBeforeMinus(self, enabled: bool):
        self.__prefix_before_minus = enabled

    def getSuffix(self) -> str:
        return self.__suffix

    def setSuffix(self, suffix: str):
        self.__suffix = suffix

    def getEasing(self) -> QEasingCurve.Type | None:
        return self.__easing

    def setEasing(self, easing: QEasingCurve.Type | None):
        self.__easing = easing
        if easing is None:
            self.__timeline.setEasingCurve(QEasingCurve.Type.Linear)
        else:
            self.__timeline.setEasingCurve(easing)

    def isRunning(self) -> bool:
        return self.__is_running

    def __frame_changed(self, timeline_value: int):
        value = Utils.get_value_from_timeline_value(timeline_value, self.__decimal_places)
        self.__value = value
        value_string = Utils.format_value(value, self.__decimal_places,
                                          self.__decimal, self.__thousands_separator)

        if not self.__prefix_before_minus and value < 0:
            value_string = value_string[1:]
            full_string = "-" + self.__prefix + value_string + self.__suffix
        else:
            full_string = self.__prefix + value_string + self.__suffix

        self.__label.setText(full_string)

    def __timeline_finished(self):
        self.__is_running = False
        self.finished.emit()
