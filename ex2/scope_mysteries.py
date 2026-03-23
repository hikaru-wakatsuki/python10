from typing import Any


def mage_counter() -> callable:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    total_power: int = initial_power

    def accumulator(power: int) -> int:
        nonlocal total_power
        total_power += power
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, callable]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        if key in memory:
            return memory[key]
        return "Memory not found"
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print()
    print("Testing mage counter...")
    counter: callable = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {counter()}")
    print()
    print("Testing enchantment factory...")
    enchantment_flaming: callable = enchantment_factory("Flaming")
    enchantment_frozen: callable = enchantment_factory("Frozen")
    print(enchantment_flaming("Sword"))
    print(enchantment_frozen("Shield"))
