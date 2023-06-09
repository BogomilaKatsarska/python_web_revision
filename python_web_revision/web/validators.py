from datetime import date

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_before_today(value):
    if date.today() < value:
        raise ValidationError('The date must be before today')


def validate_priority(value):
    if value < 1 or value > 10:
        raise ValidationError('Priority must be between 1 and 10.')


def validate_text(value):
    if '_' in value:
        raise ValidationError('The value should not contain "_".')


@deconstructible
class ValueInRangeValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if value < self.min_value or self.max_value < value:
            raise ValidationError(f'Value must be between {self.min_value} and {self.max_value}.')

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.min_value == other.min_value
            and self.max_value == other.max_value
        )
