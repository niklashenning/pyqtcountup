
class Utils:

    @staticmethod
    def format_value(value, decimals, decimal_point, thousands_separator):
        string_format = '{:,.' + str(decimals) + 'f}'
        temp_thousands_separator = '0888019ca0faa9774a728c864e248749'
        temp_decimal_separator = 'f6e9eccf7256112eccd52f41f1fded3f'

        return (string_format.format(value)
                             .replace(',', temp_thousands_separator)
                             .replace('.', temp_decimal_separator)
                             .replace(temp_thousands_separator, thousands_separator)
                             .replace(temp_decimal_separator, decimal_point))

    @staticmethod
    def get_timeline_value_from_value(timeline_value, decimals):
        if decimals <= 0:
            return int(timeline_value)

        return int(timeline_value * 10 ** decimals)

    @staticmethod
    def get_value_from_timeline_value(value, decimals):
        if decimals <= 0:
            return value

        return value / 10 ** decimals
