from django.forms import ValidationError

class ProductSizeValidator:
    def __init__(self, acceptable_sizes: list) -> None:
        # Приведение всех размеров в списке к верхнему регистру
        for index, size in enumerate(acceptable_sizes):
            acceptable_sizes[index] = size.upper()
        self.ACCEPTABLE_SIZES = acceptable_sizes  # Сохранение допустимых размеров в атрибуте класса

    def check_size(self, value: str) -> None:
        # Проверка, что размер есть в списке допустимых размеров
        if value not in self.ACCEPTABLE_SIZES:
            raise ValidationError(f"{value} is not an available size")  # Если нет, поднимаем исключение

    def validate_size(self, values: str | list) -> None:
        # Если values - это строка (один размер)
        if isinstance(values, str):
            return self.check_size(values)  # Проверяем один размер

        # Если values - это список размеров
        for value in values:
            value = value.upper()  # Приведение размера к верхнему регистру
            return self.check_size(value)  # Проверка каждого размера в списке