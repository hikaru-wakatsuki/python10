def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs) -> callable:
        try:
            result1 = spell1(*args, **kwargs)
            result2 = spell2(*args, **kwargs)
            return (result1, result2)
        except Exception as error:
            return f"Spell combination failed: {error}"
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplifier(*args, **kwargs) -> callable:
        try:
            return base_spell(*args, **kwargs) * multiplier
        except Exception as error:
            return f"Power amplification failed: {error}"
    return amplifier


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kwargs) -> callable:
        try:
            if condition(*args, **kwargs):
                return spell(*args, **kwargs)
            return "Spell fizzled"
        except Exception as error:
            return f"Conditional casting failed: {error}"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs) -> callable:
        result: list = []
        for spell in spells:
            try:
                result.append(spell(*args, **kwargs))
            except Exception as error:
                result.append(f"Spell failed: {error}")
        return result
    return sequence


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


def damage() -> int:
    return 10


def main() -> None:
    print()
    print("Testing spell combiner...")
    combined: callable = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result}")
    print()
    print("Testing power amplifier...")
    amplified: callable = power_amplifier(damage, 3)
    print(f"Original: {damage()}, Amplified: {amplified()}")


if __name__ == "__main__":
    main()
