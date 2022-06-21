from collections import UserDict
from record import Record


class RecIterator:
    """
    Class-iterator
    """
    def __init__(self, records):
        self.records = records

    def _gen_record(self):
        if self.records:
            return self.records.pop(0)
        raise StopIteration

    def __next__(self):
        return self._gen_record()

    def __iter__(self):
        return self


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, rec: Record):
        key = rec.name.value
        self[key] = rec

    def __str__(self):
        res = ''
        for key in self.data:
            res += f'{key}\n'
            for number in self[key].numbers:
                res += f'\t{number}\n'
        return res

    def _records(self):
        return (record for record in self.data.values())

    def __iter__(self):
        return RecIterator(self._records)

    def print(self):
        for rec, data in self.data.items():
            print(data)


