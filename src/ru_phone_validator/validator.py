

class PhoneNumber:

    def __init__(self, full_number: str):
        self._full_number = full_number

    @property
    def full_number(self):
        return self._full_number

    @full_number.setter
    def full_number(self, value: str):
        # validation here
        self._full_number = value

    @property
    def number(self) -> str:
        return self.full_number.replace('+', '')

    @property
    def _number(self) -> int:
        return int(self.number)

    @property
    def country_code(self):
        return self.number[:-10]

    @property
    def _country_code(self) -> int:
        return int(self.country_code)

    @property
    def area_code(self) -> str:
        return self.full_number[len(self.country_code):-len(self.last_digits)]

    @property
    def _area_code(self) -> int:
        return int(self.area_code)

    @property
    def prefix(self) -> str:
        return self.last_digits[:-len(self.line_number)]

    @property
    def _prefix(self) -> int:
        return int(self.prefix)

    @property
    def line_number(self) -> str:
        return self.last_digits[3:]

    @property
    def _line_numbers(self) -> int:
        return int(self.line_number)

    @property
    def last_digits(self) -> str:
        return self.full_number[len(self.full_number) - 7:]

    @property
    def _last_digits(self) -> int:
        return int(self.last_digits)

    @property
    def country(self) -> str:
        ...

    @property
    def region(self) -> str:
        ...
