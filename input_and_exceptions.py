'''
Обработка ввода баллов с проверкой на корректность ввода.
Oбработка ошибок ввода баллов
'''

class MyException(Exception):
    def __init__(self, message, original_exception=None):
        super().__init__(message)
        self.original_exception = original_exception

def handle_input():
    try:
        score = None
        while score is None or score < 0 or score > 100:
            try:
                score_input = input("Введите баллы: ")
                if not score_input.isdigit():
                    raise ValueError('Введено некорректное значение. Введите число.')
                score = int(score_input)
                if score < 0:
                    raise ValueError('Значение баллов не может быть меньше 0')
                if score > 100:
                    raise ValueError('Значение баллов не может быть больше 100')
            except ValueError as e:
                raise MyException(str(e))
    except MyException as e:
        print(e)
        # Дополнительная обработка ошибки, если необходимо

handle_input()
