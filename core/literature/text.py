import re
import sys

is_python3 = sys.version_info >= (3, 0)


class Text:

    @staticmethod
    def isstring(value):
        if is_python3:
            return isinstance(value, str)
        return isinstance(value, basestring)

    @staticmethod
    def condensate(txt):
        """
            Returns a condensed version of the given string, trimming, removing line breaks and multiple spaces
        """
        s = txt.strip()
        s = Text.remove_line_breaks(s)
        s = Text.remove_multiple_spaces(s)
        return s


    @staticmethod
    def remove_line_breaks(txt):
        return txt.replace('\n', ' ').replace('\r', '')


    @staticmethod
    def remove_multiple_spaces(txt):
        return re.sub("[\s]+", " ", txt)


    @staticmethod
    def repeat(txt, times):
        return "".join(txt for a in range(times))
