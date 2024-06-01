

class Utils:

    @staticmethod
    def format_value(value: int | float, decimal_places: int,
                     decimal: str, thousands_separator: str) -> str:
        """Format a value to a string with given decimal places,
         decimal and thousands separator

        :param value: value to be formatted
        :param decimal_places: amount of decimal places
        :param decimal: decimal of the number
        :param thousands_separator: thousands separator of the number
        :return: formatted value as string
        """

        string_format = '{:,.' + str(decimal_places) + 'f}'
        temp_thousands_separator = '0888019ca0faa9774a728c864e248749'
        temp_decimal_separator = 'f6e9eccf7256112eccd52f41f1fded3f'

        return (string_format.format(value)
                             .replace(',', temp_thousands_separator)
                             .replace('.', temp_decimal_separator)
                             .replace(temp_thousands_separator, thousands_separator)
                             .replace(temp_decimal_separator, decimal))

    @staticmethod
    def get_timeline_value_from_value(value: int | float, decimal_places: int) -> int:
        """Get the timeline value from a real value

        :param value: real value to convert to timeline value
        :param decimal_places: amount of decimal places
        :return: timeline value
        """

        if decimal_places <= 0:
            return int(value)

        return int(value * 10 ** decimal_places)

    @staticmethod
    def get_value_from_timeline_value(timeline_value: int, decimal_places: int) -> int | float:
        """Get the real value from a timeline value

        :param timeline_value: timeline value to convert to value
        :param decimal_places: amount of decimal places
        :return: real value
        """

        if decimal_places <= 0:
            return timeline_value

        return timeline_value / 10 ** decimal_places
