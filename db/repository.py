import abc
from model.cognate import *

class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_lexicon(self) -> list[LexicalEntry]:
        raise NotImplementedError

    @abc.abstractmethod
    def load_false_friends(self) -> list[LexicalEntry]:
        raise NotImplementedError