# PyQt CountUp

[![PyPI](https://img.shields.io/badge/pypi-v1.0.0-blue)](https://pypi.org/project/pyqtcountup/)
[![Python](https://img.shields.io/badge/python-3.7+-blue)](https://github.com/niklashenning/pyqtcountup)
[![Build](https://img.shields.io/badge/build-passing-neon)](https://github.com/niklashenning/pyqtcountup)
[![Coverage](https://img.shields.io/badge/coverage-100%25-green)](https://github.com/niklashenning/pyqtcountup)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/niklashenning/pyqtcountup/blob/master/LICENSE)

A simple numerical data animation library for PyQt and PySide labels inspired by [countUp.js](https://github.com/inorganik/CountUp.js)

![pyqtcountup](https://github.com/niklashenning/pyqtcountup/assets/58544929/0e6a2b8b-e4c6-493c-a007-86c5be3011d3)

## Features
* Customizable decimal places
* Customizable decimal separator and thousands separator
* Customizable prefix and suffix
* Supports 41 different easing curves
* Works with `PyQt5`, `PyQt6`, `PySide2`, and `PySide6`

## Installation
```
pip install pyqtcountup
```

## Usage
Import the `CountUp` class, instantiate it with a label, and start the animation by calling the `start()` method:

```python
from PyQt6.QtWidgets import QMainWindow, QLabel
from pyqtcountup import CountUp


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        
        # Create label to show the animation on
        countup_label = QLabel(self)
        
        # Init and start animation with duration of 2.5 seconds
        countup = CountUp(countup_label)
        countup.setStartValue(1000)
        countup.setEndValue(7241)
        countup.setDuration(2500)
        countup.start()
```

Use the `update()` method to update the end value of a running animation (can also be used if the animation is already finished):
```python
# Start animation with 2500 as end value
countup.setEndValue(2500)
countup.start()

# Update end value of the animation to be 1500
countup.update(1500)
```

To pause and resume an animation, use the `pause()` and `resume()` methods:
```python
# Temporarily stop the animation with the option to resume it
countup.pause()

# Resume the animation at the point where it was stopped
countup.resume()
```

> **NOTE:** <br>Only paused animations can be resumed, so calling `resume()` after using the `stop()` method will not work.


If you want to stop an animation completely, you can use the `stop()` method:
```python
countup.stop()
```

If you want to stop the animation and also reset the label to the start value, you can use the `reset()` method:
```python
countup.reset()
```

To check if the animation is currently running or paused, use the `isRunning()` and `isPaused()` methods: 
```python
# True if the animation is currently running, otherwise False
is_running = countup.isRunning()

# True if the animation is currently paused and can be resumed, otherwise False
is_paused = countup.isPaused()
```

## Customization
* **Setting the start and end values of the animation:**
```python
countup.setStartValue(-1000)
countup.setEndValue(2500)

# Alternatively
countup.setStartEndValues(-1000, 2500)
```

* **Setting the duration of the animation:**
```python
countup.setDuration(2500)  # 2500 milliseconds = 2.5 seconds
```

* **Customizing the formatting of the number:**
```python
countup.setDecimalPlaces(2)  # Default: 0
countup.setDecimal(',')      # Default: '.'
countup.setSeparator('.')    # Default: ''
```
> **EXAMPLE:** <br>The value `1052` formatted with two decimal places, `,` as the decimal, and `.` as the separator would be `1.052,00`

* **Adding a prefix and a suffix:**
```python
countup.setPrefix('~')   # Default: ''
countup.setSuffix('€')  # Default: ''
```
> **EXAMPLE:** <br>The value `100` formatted with `~` as the prefix and `€` as the suffix would be shown as `~100€`

* **Making the prefix show between the minus and the number for negative values:**
```python
countup.setPrefixBeforeMinus(False)  # Default: True
```
> **EXAMPLE:** <br>The value `100` formatted with `$` as the prefix and `setPrefixBeforeMinus(False)` would be shown as `-$100` instead of `$-100`

* **Customizing the easing of the animation:**
```python
countup.setEasing(QEasingCurve.Type.OutCubic)  # Default: QEasingCurve.Type.OutExpo

# Using no easing (same as QEasingCurve.Type.Linear)
countup.setEasing(None)
```
> **AVAILABLE EASING CURVES:** <br> `Linear`, `InQuad`, `OutQuad`, `InOutQuad`, `OutInQuad`, `InCubic`, `OutCubic`,
> `InOutCubic`, `OutInCubic`, `InQuart`, `OutQuart`, `InOutQuart`, `OutInQuart`, `InQuint`, `OutQuint`, `InOutQuint`,
> `OutInQuint`, `InSine`, `OutSine`, `InOutSine`, `OutInSine`, `InExpo`, `OutExpo`, `InOutExpo`, `OutInExpo`,
> `InCirc`, `OutCirc`, `InOutCirc`, `OutInCirc`, `InElastic`, `OutElastic`, `InOutElastic`, `OutInElastic`,
> `InBack`, `OutBack`, `InOutBack`, `OutInBack`, `InBounce`, `OutBounce`, `InOutBounce`, `OutInBounce`
> <br>You can find visualizations of these easing curves in the [PyQt documentation](https://doc.qt.io/qtforpython-5/PySide2/QtCore/QEasingCurve.html).

Examples for PyQt5, PyQt6, and PySide6 can be found in the [demo](https://github.com/niklashenning/pyqtcountup/blob/master/demo) folder.

## Tests
Installing the required test dependencies [PyQt6](https://pypi.org/project/PyQt6/), [pytest](https://github.com/pytest-dev/pytest), and [coveragepy](https://github.com/nedbat/coveragepy):
```
pip install PyQt6 pytest coverage
```

To run the tests with coverage, clone this repository, go into the main directory and run:
```
coverage run -m pytest
coverage report --ignore-errors -m
```

## License
This software is licensed under the [MIT license](https://github.com/niklashenning/pyqtcountup/blob/master/LICENSE).
