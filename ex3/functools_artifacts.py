from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul, gt, lt


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        raise ValueError("spells list cannot be empty")
    operations = {
        "add": add,
        "multiply": mul,
        "max": lambda x, y: x if gt(x, y) else y,
        "min": lambda x, y: x if lt(x, y) else y
    }
    if operation not in operations:
        raise ValueError("invalid operation")
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': partial(base_enchantment, 50, 'fire'),
        'ice_enchant': partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': partial(base_enchantment, 50, 'lightning')
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def cast_spell(arg) -> str:
        return "Unknown spell type"

    @cast_spell.register
    def _(arg: int) -> str:
        return f"Damage spell deals {arg} damage"

    @cast_spell.register
    def _(arg: str) -> str:
        return f"Casting enchantment: {arg}"

    @cast_spell.register
    def _(arg: list) -> str:
        return f"Casting multi-spell sequence: {', '.join(map(str, arg))}"
    return cast_spell


if __name__ == "__main__":
    try:
        print()
        print("Testing spell reducer...")
        print(f"Sum: {spell_reducer([40, 60], 'add')}")
        print(f"Product: {spell_reducer([40, 6000], 'multiply')}")
        print(f"Max: {spell_reducer([40, 6], 'max')}")
        print()
        print("Testing memoized fibonacci...")
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")
    except ValueError as error:
        print(error)
