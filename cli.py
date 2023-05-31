import click
from random import randint


class Pizza:
    def __init__(self, size: str = 'L'):
        self._size = size

    @property
    def size(self):
        if hasattr(self, '_size') is False:
            self._size = 'L'
        return self._size

    # Проверяем, что размер L или XL
    @size.setter
    def size(self, value: str):
        assert value in ('L', 'XL'), 'Wrong size. Input L or XL'
        self._size = value


class Margarita(Pizza):
    def __init__(self, size: str = 'L'):
        super().__init__(size)

    def dict(self):
        print(f'{self.__class__.__name__} 🧀: \
            tomato sauce, mozzarella, tomatoes')


class Pepperoni(Pizza):
    def __init__(self, size: str = 'L'):
        super().__init__(size)

    def dict(self):
        print(f'{self.__class__.__name__} 🍕: \
            tomato sauce, mozzarella, pepperoni')


class Hawaiian(Pizza):
    def __init__(self, size: str = 'L'):
        super().__init__(size)

    def dict(self):
        print(f'{self.__class__.__name__} 🍍: \
            tomato sauce, mozzarella, chicken, pineapples')


def log(function):
    def wrapper(*args):
        res = function.__name__ + f' - {randint(1, 5)}c!'
        print(res)

        return res

    return wrapper


@log
def bake(pizza):
    """Готовит пиццу

    >>> bake('margarita')
    ... 'Приготовили margarita за 2с!'
    """
    print(f'Приготовили {pizza} за {randint(1, 5)}с!')


@log
def delivery_(pizza):
    """Доставляет пиццу

    >>> delivery_('pepperoni')
    ... '🛵 Доставили за 3с!'
    """
    print(f'🛵 Доставили за {randint(1, 5)}с!')


@log
def pickup(pizza):
    """Самовывоз

    >>> pickup('pepperoni')
    ... '🏠 Забрали за 3с!'
    """
    print(f'🏠 Забрали за {randint(1, 5)}с!')


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('class_pizza', nargs=1)
def order(class_pizza: str, delivery: bool):
    """Готовит и доставляет пиццу

    >>> python cli.py order pepperoni --delivery
    ... 'Приготовили pepperoni за 4с!
    ... 🛵 Доставили за 3с!'
    >>> python cli.py order hawaiian
    ... 'Приготовили hawaiian за 4с!'
    """

    pizza = type(f'{class_pizza}', (Pizza,), {})
    print(f'Приготовили {pizza.__name__} за {randint(1, 5)}с!')

    if delivery:
        print(f'🛵 Доставили за {randint(1, 5)}с!')


@cli.command()
def menu():
    """Выводит меню

    >>> python cli.py menu
    ... 'Margarita 🧀:             tomato sauce, mozzarella, tomatoes
    ... Pepperoni 🍕:             tomato sauce, mozzarella, pepperoni
    ... Hawaiian 🍍:             tomato sauce, mozzarella, chicken, pineapples'
    """

    Margarita().dict()
    Pepperoni().dict()
    Hawaiian().dict()


if __name__ == '__main__':
    cli()
