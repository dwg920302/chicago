from abc import *


class ReaderBase(metaclass=ABCMeta):
    @abstractmethod
    def set_url(self):
        pass

    def to_dframe(self):
        pass


class PrinterBase(metaclass=ABCMeta):
    @abstractmethod
    def from_csv(self):
        pass

    @abstractmethod
    def from_xls(self):
        pass

    @abstractmethod
    def from_json(self):
        pass


class ScraperBase(metaclass=ABCMeta):
    @abstractmethod
    def scrap_it(self):
        pass

    @abstractmethod
    def driver(self):
        pass
