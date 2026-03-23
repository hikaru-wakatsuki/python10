from time import time
from functools import wraps
from typing import Any


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*argc, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start: float = time()
        try:
            result: Any = func(*argc, **kwargs)
        except Exception as error:
            raise Exception(f"Function execution failed: {error}")
        end: float = time()
        print(f"Spell completed in {end - start} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    if min_power < 0:
        raise ValueError("min_power must be non-negative")

    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(self, power: int, *argc, **kwargs) -> Any:
            if not isinstance(power, int):
                raise TypeError("power must be an integer")
            if power < min_power:
                return "Insufficient power for this spell"
            try:
                return func(self, power, *argc, **kwargs)
            except Exception as error:
                raise Exception(f"Function execution failed: {error}")
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    if max_attempts <= 0:
        raise ValueError("max_attempts must be greater than 0")

    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*argc, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*argc, **kwargs)
                except Exception:
                    if attempt == max_attempts:
                        return (
                            f"Spell casting failed after "
                            f"{max_attempts} attempts")
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    try:
        print()
        print("Testing spell timer...")

        def fireball(spell: str) -> str:
            return f"{spell.capitalize()} cast!"
        wrapper: callable = spell_timer(fireball)
        result: Any = wrapper('fireball')
        print(f"Result: {result}")
        print()
        print("Testing MageGuild...")
        mageguild: MageGuild = MageGuild()
        print(mageguild.validate_mage_name('Lightning'))
        print(mageguild.validate_mage_name('123 456'))
        print(mageguild.cast_spell(15, 'Lightning'))
        print(mageguild.cast_spell(1, 'Lightning'))
    except Exception as error:
        print(error)
