def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs) -> callable:
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplifier(*args, **kwargs) -> callable:
        return base_spell(*args, **kwargs) * multiplier
    return amplifier


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kwargs) -> callable:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs) -> callable:
        result: list[callable] = []
        for spell in spells:
            result.append(spell(*args, **kwargs))
        return result
    return sequence


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f" Heals {target}"


def damage() -> int:
    return 10


def main() -> None:
    print()
    print("Testing spell combiner...")
    combined: callable = spell_combiner(fireball, heal)
    result: tuple[str] = combined("Dragon")
    print(f"Combined spell result: {result}")
    print()
    print("Testing power amplifier...")
    amplified: callable = power_amplifier(damage, 3)
    print(f"Original: {damage()}, Amplified: {amplified()}")


if __name__ == "__main__":
    main()
