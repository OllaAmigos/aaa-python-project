class Pizza:
    """Base pizza recipe class"""
    PIZZA_SIZES = ['L', 'XL']

    def __init__(
            self,
            ingredients: list[str, ...],
            size: str = 'L',
            emoji: str = '',
            is_baked: bool = False,
            is_delivered: bool = False,
            is_pickup: bool = False
    ) -> None:
        """
        Объявляет рецепт пиццы.
         Аргументы:
             ingredients: list; список ингредиентов.
             size: str; Размер пиццы (L или XL).
             emoji: str; эмоджи рядом с названием пиццы'.
             is_baked: bool; указывающий, испечена ли пицца.
             is_delivered: bool; указывающий, доставлена ли пицца.
             is_pickup: bool; указывающий, забрали ли пиццу.
         Что вызывает:
             ValueError: Если некорректный размер.
        """
        if size not in self.PIZZA_SIZES:
            raise ValueError(f'Invalid pizza size: {size}')

        self.ingredients = ingredients
        self.size = size
        self.emoji = emoji
        self.is_baked = is_baked
        self.is_delivered = is_delivered
        self.is_pickup = is_pickup

    def bake(self) -> None:
        """Bakes the pizza."""
        self.is_baked = True

    def delivery(self) -> None:
        """Delivers the pizza."""
        self.is_delivered = True

    def pickup(self) -> None:
        """Picks up the pizza."""
        self.is_pickup = True

    def abot(self) -> str:
        """Печатает вид пиццы и ингредиенты в удобном формате"""
        return f'Pizza with {self.size} size\ningredients: {", ".join(self.ingredients)}'

    def __dict__(self) -> dict:
        """Возвращает пиццу как словарь"""
        return {
            'size': self.size,
            'ingredients': self.ingredients,
        }

    def __eq__(self, other) -> bool:
        """Сравнивает равенство двух пицц по типу и размеру"""
        if not isinstance(other, Pizza):
            raise ValueError(f'Invalid pizza type: {type(other)}')

        return (
                self.size == other.size
                and self.ingredients == other.ingredients
        )


class Margherita(Pizza):
    """Рецепт пиццы Маргарита"""

    emoji = '🧀'
    ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']

    def __init__(self, size: str = 'XL') -> None:
        """Объявляем пиццу Маргарита конкретного размера"""
        super().__init__(self.ingredients, size, self.emoji)


class Pepperoni(Pizza):
    """Рецепт пиццы Пепперони"""

    emoji = '🍕'
    ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']

    def __init__(self, size: str = 'L') -> None:
        """Объявляем пиццу Пепперони конкретного размера"""
        super().__init__(self.ingredients, size, self.emoji)


class Hawaiian(Pizza):
    """Рецепт Гавайской пиццы"""

    emoji = '🍍'
    ingredients = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']

    def __init__(self, size: str = 'L') -> None:
        """Объявляем Гавайскую пиццу конкретного размера"""
        super().__init__(self.ingredients, size, self.emoji)
