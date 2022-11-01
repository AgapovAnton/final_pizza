import click
from random import randint

# from pizza import Pizza, Margarita, Pepperoni, Hawaiian # вот это не работает

# Сделал отдельный файл pizza.py, но как его импортнуть сюда
# не понял, поэтому скопировал классы пицц


class Pizza:
    def __init__(self, size: str = 'L'):
        self._size = size

    @property
    def size(self):
        if hasattr(self, '_size'):
            return self._size
        else:
            self._size = 'L'
            return self._size

    # Проверяем, что размер L или XL
    @size.setter
    def size(self, value: str):
        if (value == 'L') or (value == 'XL'):
            self._size = value
        else:
            raise ValueError('Wrong size. Input L or XL')


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
    """Готовит пиццу"""
    print(f'Приготовили {pizza} за {randint(1, 5)}с!')


@log
def delivery_(pizza):
    """Доставляет пиццу"""
    print(f'🛵 Доставили за {randint(1, 5)}с!')


@log
def pickup(pizza):
    """Самовывоз"""
    print(f'🏠 Забрали за {randint(1, 5)}с!')


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('class_pizza', nargs=1)
def order(class_pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""

    # Так почему то неработает
    # pizza = type(f'{class_pizza}', (Pizza,), {})
    # print(f'Приготовили {pizza.__class__.__name__} за {randint(1, 5)}с!')

    print(f'Приготовили {class_pizza} за {randint(1, 5)}с!')
    if delivery:
        print(f'🛵 Доставили за {randint(1, 5)}с!')


@cli.command()
def menu():
    """Выводит меню"""
    Margarita().dict()
    Pepperoni().dict()
    Hawaiian().dict()


if __name__ == '__main__':
    cli()
