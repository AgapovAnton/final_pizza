class Pizza:
    def __init__(self, size: str):
        self._size = size

    @property
    def size(self):
        if hasattr(self, '_size'):
            return self._size
        else:
            self._size = 'L'
            return self._size

    @size.setter
    def size(self, value: str):
        if (value == 'L') or (value == 'XL'):
            self._size = value
        else:
            raise ValueError('Wrong size. Input L or XL')


class Margarita(Pizza):
    def __init__(self, _size: str):
        super().__init__(_size)

    def dict(self):
        print(f'{self.__class__.__name__} 🧀: \
            tomato sauce, mozzarella, tomatoes')


class Pepperoni(Pizza):
    def __init__(self, _size: str):
        super().__init__(_size)

    def dict(self):
        print(self.__dict__)
        print(f'{self.__class__.__name__} 🍕: \
            tomato sauce, mozzarella, pepperoni')


class Hawaiian(Pizza):
    def __init__(self, _size: str):
        super().__init__(_size)

    def dict(self):
        print(f'{self.__class__.__name__} 🍍: \
            tomato sauce, mozzarella, chicken, pineapples')


if __name__ == '__main__':
    my_pizza = Margarita('XL')
    my_pizza.dict()
