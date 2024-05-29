from src.pyqtcountup.utils import Utils


def test_format_value():
    assert Utils.format_value(1201.24, 3, '.', ',') == '1,201.240'
    assert Utils.format_value(-14212.88, 2, ',', ' ') == '-14 212,88'
    assert Utils.format_value(7846.4231, 2, '.', '') == '7846.42'
    assert Utils.format_value(823.72, 0, '.', ',') == '824'


def test_get_timeline_value_from_value():
    assert Utils.get_timeline_value_from_value(124.78, 2) == 12478
    assert Utils.get_timeline_value_from_value(-2832.63, 2) == -283263


def test_get_value_from_timeline_value():
    assert Utils.get_value_from_timeline_value(12478, 2) == 124.78
    assert Utils.get_value_from_timeline_value(-283263, 2) == -2832.63
