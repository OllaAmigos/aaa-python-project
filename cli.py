import click
from decorator import log
from recipes_pizza import Pizza, Margherita, Pepperoni, Hawaiian

PIZZA_NAMES_DICT = {
    'margherita': Margherita(),
    'pepperoni': Pepperoni(),
    'hawaiian': Hawaiian()
}
MAX_PIZZA_NAME_LENGTH = max([len(key) for key in PIZZA_NAMES_DICT.keys()])

MENU = [f'{i} - {type(pizza).__name__:{MAX_PIZZA_NAME_LENGTH}} '
        f'{pizza.emoji:1}: {", ".join(pizza.ingredients)}'
        for i, pizza in enumerate(PIZZA_NAMES_DICT.values(), 1)]


@click.group()
def cli():
    """Выбираем пиццу из меню"""
    pass


@log('🛵 Delivered in {} sec!')
def deliver(pizza: Pizza):
    """Доставляет пиццу"""
    pizza.delivery()


@log('🏠 Pickup in {} sec!')
def pickup(pizza: Pizza):
    """Самовывоз пиццы"""
    pizza.pickup()


@log('🍕 Baked in {} sec!')
def bake(pizza: Pizza):
    """Готовит пиццу"""
    pizza.bake()


@cli.command()
@click.argument('pizza_name', nargs=1)
@click.option('--delivery', default=False, is_flag=True)
def order(pizza_name: str, delivery: bool) -> None:
    """Вызывает готовку и доставку/самовывоз пиццы"""
    if pizza_name.lower() not in PIZZA_NAMES_DICT:
        raise ValueError(f'Incorrect name of pizza: {pizza_name}')
    pizza = PIZZA_NAMES_DICT[pizza_name.lower()]
    bake(pizza)
    if delivery:
        deliver(pizza)
    else:
        pickup(pizza)


@cli.command()
def menu():
    """Показывает меню"""
    for pizza in MENU:
        print(pizza)


if __name__ == '__main__':
    cli()
