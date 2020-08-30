from abc import ABCMeta, abstractmethod

LINES_BEFORE_SECTION = "\n\n"
LINES_AFTER_SECTION = "\n\n"


def formatted_section(func):
    def wrapper(self):
        return LINES_BEFORE_SECTION + func(self) + LINES_AFTER_SECTION
    return wrapper


class BaseClient(metaclass=ABCMeta):

    @abstractmethod
    def generate_report(self):
        pass
