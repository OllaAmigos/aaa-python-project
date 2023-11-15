from cli import *
from recipes_pizza import *


if __name__ == '__main__':
    print(deliver(Margherita()))
    print(bake(Margherita()))
    print(Hawaiian('XL').abot())
    print(Pepperoni('XL').__eq__(Hawaiian('XL')))
