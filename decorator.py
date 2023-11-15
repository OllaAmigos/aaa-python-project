from random import randint


def log(template):
    """
    Регестрирует время выполнения функции по указанному шаблону.
    Аргументы:
        - шаблон -- строка; c описанием, ЧТО выполнилось за
            указанное время; включает '{}', куда функция вставит
            время выполнения.
    Вывод:
        функция декоратора.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(template.format(randint(1, 36)))
            return result
        return wrapper
    return decorator
