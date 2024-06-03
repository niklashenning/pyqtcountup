from qtpy.QtWidgets import QLabel
from qtpy.QtCore import QTimeLine, QEasingCurve, Signal, QObject
from .utils import Utils


class CountUp(QObject):

    # Signal
    finished = Signal()

    def __init__(self, label: QLabel, start_value: int | float = 0, end_value: int | float = 100,
                 duration: int = 1000, decimal_places: int = 0, decimal: str = '.',
                 thousands_separator: str = '', prefix: str = '', prefix_before_minus: bool = True,
                 suffix: str = '', easing: QEasingCurve.Type | None = QEasingCurve.Type.OutExpo):
        """Create a new CountUp instance

        :param label: label to animate the text of
        :param start_value: start value of the animation
        :param end_value: end value of the animation
        :param duration: duration of the animation
        :param decimal_places: amount of decimal places that will be displayed
        :param decimal: decimal of the number
        :param thousands_separator: thousands separator of the number
        :param prefix: prefix that will be shown before the value
        :param prefix_before_minus: whether to show the prefix before or after the minus for negative values
        :param suffix: suffix that will be shown behind the value
        :param easing: easing curve of the animation
        """

        super(CountUp, self).__init__(None)

        # Init attributes
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
        self.__is_paused = False

        # Init timeline
        self.__timeline = QTimeLine(self.__duration, self.__label)
        self.__timeline.setDuration(duration)

        if easing is None:
            self.__timeline.setEasingCurve(QEasingCurve.Type.Linear)
        else:
            self.__timeline.setEasingCurve(easing)

        self.__timeline.frameChanged.connect(lambda v: self.__frame_changed(v))
        self.__timeline.finished.connect(self.__timeline_finished)

    def start(self):
        """Start the animation"""

        frame_range_start = Utils.get_timeline_value_from_value(self.__start_value, self.__decimal_places)
        frame_range_end = Utils.get_timeline_value_from_value(self.__end_value, self.__decimal_places)
        self.__timeline.setFrameRange(frame_range_start, frame_range_end)
        self.__timeline.setDuration(self.__duration)

        if self.__easing is None:
            self.__timeline.setEasingCurve(QEasingCurve.Type.Linear)
        else:
            self.__timeline.setEasingCurve(self.__easing)

        self.__frame_changed(frame_range_start)
        self.__is_running = True
        self.__is_paused = False
        self.__timeline.start()

    def update(self, new_end_value: int):
        """Update the animation end value while the animation is running"""

        if self.__is_running:
            self.__timeline.stop()
        self.setStartValue(self.__value)
        self.setEndValue(new_end_value)
        self.start()

    def pause(self):
        """Pause the running animation"""

        if not self.__is_paused and self.__is_running:
            self.__timeline.setPaused(True)
            self.__is_running = False
            self.__is_paused = True

    def resume(self):
        """Resume the paused animation"""

        if self.__is_paused:
            self.__is_running = True
            self.__is_paused = False
            self.__timeline.resume()

    def stop(self):
        """Stop the animation"""

        self.__timeline.stop()
        self.__is_running = False
        self.__is_paused = False

    def reset(self):
        """Reset the animation and show the start value"""
        if self.__is_running:
            self.__timeline.stop()
            self.__is_running = False
        self.__frame_changed(Utils.get_timeline_value_from_value(self.__start_value, self.__decimal_places))
        self.__is_paused = False

    def getLabel(self) -> QLabel:
        """Get the label

        :return: label
        """

        return self.__label

    def setLabel(self, label: QLabel):
        """Set the label to animate the text of

        :param label: new label
        """

        self.__label = label

    def getStartValue(self) -> int | float:
        """Get the start value of the animation

        :return: start value
        """

        return self.__start_value

    def setStartValue(self, start_value: int | float):
        """Set the start value of the animation

        :param start_value: new start value
        """

        self.__start_value = start_value

    def getEndValue(self) -> int | float:
        """Get the end value of the animation

        :return: end value
        """

        return self.__end_value

    def setEndValue(self, end_value: int | float):
        """Set the end value of the animation

        :param end_value: new end value
        """

        self.__end_value = end_value

    def setStartEndValues(self, start_value: int | float, end_value: int | float):
        """Set the start and end values of the animation

        :param start_value: new start value
        :param end_value: new end value
        """

        self.__start_value = start_value
        self.__end_value = end_value

    def getDuration(self) -> int:
        """Get the duration of the animation

        :return: duration
        """

        return self.__duration

    def setDuration(self, duration: int):
        """Set the duration of the animation

        :param duration: new duration
        """

        self.__duration = duration

    def getDecimalPlaces(self) -> int:
        """Get the amount of decimal places of the number

        :return: amount of decimal places
        """

        return self.__decimal_places

    def setDecimalPlaces(self, decimal_places: int):
        """Set the amount of decimal places of the number

        :param decimal_places: new amount of decimal places
        """

        self.__decimal_places = decimal_places

    def getDecimal(self) -> str:
        """Get the decimal of the number

        :return: decimal
        """

        return self.__decimal

    def setDecimal(self, decimal: str):
        """Set the decimal of the number

        :param decimal: new decimal
        """

        self.__decimal = decimal

    def getThousandsSeparator(self) -> str:
        """Get the thousands separator of the number

        :return: thousands separator
        """

        return self.__thousands_separator

    def setThousandsSeparator(self, thousands_separator: str):
        """Set the thousands separator of the number

        :param thousands_separator: new thousands separator
        """

        self.__thousands_separator = thousands_separator

    def getPrefix(self) -> str:
        """Get the prefix that will be shown before the number

        :return: prefix
        """

        return self.__prefix

    def setPrefix(self, prefix: str):
        """Set the prefix that will be shown before the number

        :param prefix: new prefix
        """

        self.__prefix = prefix

    def isPrefixBeforeMinus(self) -> bool:
        """Get whether the prefix is shown before or after the minus for negative values

        :return: whether the prefix is shown before the minus for negative values
        """

        return self.__prefix_before_minus

    def setPrefixBeforeMinus(self, enabled: bool):
        """Set whether the prefix is shown before or after the minus for negative values

        :param enabled: whether the prefix should be shown before the minus for negative values
        """

        self.__prefix_before_minus = enabled

    def getSuffix(self) -> str:
        """Get the suffix that will be shown after the number

        :return: suffix
        """

        return self.__suffix

    def setSuffix(self, suffix: str):
        """Set the suffix that will be shown after the number

        :param suffix: new suffix
        """

        self.__suffix = suffix

    def getEasing(self) -> QEasingCurve.Type | None:
        """Get the easing curve of the animation

        :return: easing curve
        """

        return self.__easing

    def setEasing(self, easing: QEasingCurve.Type | None):
        """Set the easing curve of the animation

        :param easing: new easing curve
        """

        self.__easing = easing

    def isRunning(self) -> bool:
        """Get whether the animation is currently running

        :return: whether the animation is running
        """

        return self.__is_running

    def isPaused(self) -> bool:
        """Get whether the animation is currently paused

        :return: whether the animation is paused
        """

        return self.__is_paused

    def __frame_changed(self, timeline_value: int):
        """React to the frameChanged signal of the QTimeLine
        and updates the label with the new value

        :param timeline_value: the current value of the timeline
        """

        # Convert timeline value to real value and format
        value = Utils.get_value_from_timeline_value(timeline_value, self.__decimal_places)
        self.__value = value
        value_string = Utils.format_value(value, self.__decimal_places,
                                          self.__decimal, self.__thousands_separator)

        # Add prefix and suffix
        if not self.__prefix_before_minus and value < 0:
            value_string = value_string[1:]
            full_string = "-" + self.__prefix + value_string + self.__suffix
        else:
            full_string = self.__prefix + value_string + self.__suffix

        # Set label text
        self.__label.setText(full_string)

    def __timeline_finished(self):
        """Handle finished signal of QTimeLine and emit own finished signal"""

        self.__is_running = False
        self.finished.emit()
