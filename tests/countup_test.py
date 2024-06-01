from PyQt6.QtCore import QEasingCurve
from PyQt6.QtTest import QTest
from PyQt6.QtWidgets import QLabel
from src.pyqtcountup.countup import CountUp


def test_initial_values(qtbot):
    """Test the initial values"""

    label = QLabel()
    countup = CountUp(label)

    assert countup.getLabel() == label
    assert countup.getStartValue() == 0
    assert countup.getEndValue() == 100
    assert countup.getDuration() == 1000
    assert countup.getDecimalPlaces() == 0
    assert countup.getDecimal() == '.'
    assert countup.getThousandsSeparator() == ''
    assert countup.getPrefix() == ''
    assert countup.isPrefixBeforeMinus() == True
    assert countup.getSuffix() == ''
    assert countup.getEasing() is QEasingCurve.Type.OutExpo
    assert countup.isRunning() == False


def test_values_constructor(qtbot):
    """Test setting the values in the constructor"""

    label = QLabel()
    countup = CountUp(label, start_value=-2124.24, end_value=9172.52, duration=2500,
                      decimal_places=2, decimal=',', thousands_separator='.',
                      prefix='€', prefix_before_minus=False, suffix=' EUR', easing=None)

    assert countup.getLabel() == label
    assert countup.getStartValue() == -2124.24
    assert countup.getEndValue() == 9172.52
    assert countup.getDuration() == 2500
    assert countup.getDecimalPlaces() == 2
    assert countup.getDecimal() == ','
    assert countup.getThousandsSeparator() == '.'
    assert countup.getPrefix() == '€'
    assert countup.isPrefixBeforeMinus() == False
    assert countup.getSuffix() == ' EUR'
    assert countup.getEasing() is None
    assert countup.isRunning() == False


def test_set_label(qtbot):
    """Test setting the label"""

    label_1 = QLabel()
    label_2 = QLabel()
    countup = CountUp(label_1)
    countup.setLabel(label_2)
    assert countup.getLabel() == label_2


def test_set_start_end_values(qtbot):
    """Test setting the start and end values"""

    label = QLabel()
    countup = CountUp(label)

    countup.setStartValue(9172.2)
    assert countup.getStartValue() == 9172.2

    countup.setEndValue(9172.2)
    assert countup.getEndValue() == 9172.2

    countup.setStartEndValues(125, 252)
    assert countup.getStartValue() == 125
    assert countup.getEndValue() == 252


def test_set_duration(qtbot):
    """Test setting the duration"""

    label = QLabel()
    countup = CountUp(label)
    countup.setDuration(2500)
    assert countup.getDuration() == 2500


def test_set_decimal_places(qtbot):
    """Test setting the amount of decimal places"""

    label = QLabel()
    countup = CountUp(label)
    countup.setDecimalPlaces(2)
    countup.reset()
    assert countup.getDecimalPlaces() == 2
    assert label.text() == '0.00'


def test_set_decimal(qtbot):
    """Test setting the decimal"""

    label = QLabel()
    countup = CountUp(label)
    countup.setDecimal(',')
    countup.setDecimalPlaces(2)
    countup.reset()
    assert countup.getDecimal() == ','
    assert label.text() == '0,00'


def test_set_thousands_separator(qtbot):
    """Test setting the thousands separator"""

    label = QLabel()
    countup = CountUp(label)
    countup.setThousandsSeparator(',')
    countup.setStartValue(1200)
    countup.reset()
    assert countup.getThousandsSeparator() == ','
    assert label.text() == '1,200'


def test_set_prefix(qtbot):
    """Test setting the prefix"""

    label = QLabel()
    countup = CountUp(label)
    countup.setPrefix('$')
    countup.reset()
    assert countup.getPrefix() == '$'
    assert label.text() == '$0'


def test_set_prefix_before_minus(qtbot):
    """Test setting the prefix placement"""

    label = QLabel()
    countup = CountUp(label)
    countup.setPrefix('$')
    countup.setStartValue(-500)
    countup.reset()
    assert label.text() == '$-500'

    countup.setPrefixBeforeMinus(False)
    countup.reset()
    assert countup.isPrefixBeforeMinus() == False
    assert label.text() == '-$500'


def test_set_suffix(qtbot):
    """Test setting the suffix"""

    label = QLabel()
    countup = CountUp(label)
    countup.setSuffix('€')
    countup.reset()
    assert countup.getSuffix() == '€'
    assert label.text() == '0€'


def test_set_easing(qtbot):
    """Test setting the easing curve"""

    label = QLabel()
    countup = CountUp(label)

    countup.setEasing(QEasingCurve.Type.OutExpo)
    assert countup.getEasing() == QEasingCurve.Type.OutExpo

    countup.setEasing(None)
    assert countup.getEasing() is None


def test_start(qtbot):
    """Test starting the animation"""

    label = QLabel()
    label.setText('Text')
    qtbot.addWidget(label)

    countup = CountUp(label)
    countup.setEndValue(1000)
    countup.setDuration(100)
    countup.start()
    QTest.qWait(500)
    assert label.text() == '1000'


def test_update(qtbot):
    """Test updating the animation"""

    label = QLabel()
    label.setText('Text')
    qtbot.addWidget(label)

    countup = CountUp(label)
    countup.setEndValue(1000)
    countup.setDuration(100)
    countup.start()
    countup.update(-250)
    QTest.qWait(500)
    assert label.text() == '-250'


def test_pause_resume(qtbot):
    """Test pausing and resuming the animation"""

    label = QLabel()
    label.setText('Text')
    qtbot.addWidget(label)

    countup = CountUp(label)
    countup.setDuration(100)
    countup.start()
    countup.pause()
    QTest.qWait(500)
    assert label.text() != '100'
    countup.resume()
    QTest.qWait(500)
    assert label.text() == '100'


def test_stop(qtbot):
    """Test stopping the animation"""

    label = QLabel()
    label.setText('Text')
    qtbot.addWidget(label)

    countup = CountUp(label)
    countup.setDuration(100)
    countup.start()
    countup.stop()
    QTest.qWait(500)
    assert label.text() != '100'


def test_reset(qtbot):
    """Test resetting the animation"""

    label = QLabel()
    label.setText('Text')
    qtbot.addWidget(label)

    countup = CountUp(label)
    countup.start()
    countup.reset()
    QTest.qWait(100)
    assert label.text() == '0'


def test_is_running(qtbot):
    """Test checking if the animation is running"""

    label = QLabel()
    countup = CountUp(label)

    assert countup.isRunning() == False
    countup.start()
    assert countup.isRunning() == True
    countup.pause()
    assert countup.isRunning() == False
    countup.resume()
    assert countup.isRunning() == True
    countup.stop()
    assert countup.isRunning() == False
    countup.resume()
    assert countup.isRunning() == False
    countup.update(50)
    assert countup.isRunning() == True
    countup.reset()
    assert countup.isRunning() == False
