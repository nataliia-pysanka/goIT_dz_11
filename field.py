"""
Module describes class Field
"""
from abc import ABC, abstractmethod
from re import search as re_search


class Field(ABC):
    """Abstract class for fields in records of adress book"""
    @property
    @abstractmethod
    def value(self):
        raise NotImplementedError

    @value.setter
    @abstractmethod
    def value(self, new_value):
        raise NotImplementedError


class Name(Field):
    """
    Class Name
    """
    def __init__(self, value):
        self._value = None
        try:
            self.value = value
        except ValueError as err:
            print(err)

    @property
    def value(self):
        if self._value:
            return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str) or new_value == '':
            raise ValueError('Name should be a string \n')
        self._value = new_value

    def __str__(self):
        if self.value:
            return self.value
        return 'No value'


class Phone(Field):
    """
    Class Phone
    """
    def __init__(self, number=None):
        self._value = None
        try:
            self.value = number
        except ValueError as err:
            print(err)

    @property
    def value(self):
        if self._value:
            return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise ValueError('Number should be a string \n')

        if 10 <= len(new_value) <= 15 and re_search('\D', new_value) is None:
            self._value = new_value
        raise ValueError('\t Length of number should be 10-15 symbols')

    def __str__(self):
        if self._value:
            return self._value
        return 'No number'

    def edit(self, new_value: str):
        """
        Function for editing value of Phone
        :param new_value: str
        :return: boolean
        """
        try:
            self.value = new_value
        except ValueError as err:
            print(err)
            return False
        return True


n = Phone('')
print(n)