def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    if not all('power' in artifact for artifact in artifacts):
        raise ValueError("artifact missing 'power' field")
    if not all(isinstance(artifact.get('power'), int)
               for artifact in artifacts):
        raise ValueError("artifact power must be int")
    return sorted(
        artifacts, key=lambda artifact: artifact['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    if not all('power' in mage for mage in mages):
        raise ValueError("mage missing 'power' field")
    if not all(isinstance(mage.get('power'), int) for mage in mages):
        raise ValueError("mage power must be int")
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: '* ' + spell + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        raise ValueError("mages list cannot be empty")
    if not all('power' in mage for mage in mages):
        raise ValueError("mage missing 'power' field")
    if not all(isinstance(mage.get('power'), int) for mage in mages):
        raise ValueError("mage power must be int")
    return {
        'max_power': max(mages, key=lambda mage: mage['power'])['power'],
        'min_power': min(mages, key=lambda mage: mage['power'])['power'],
        'avg_power': round(
            sum(map(lambda mage: mage['power'], mages)) / len(mages), 2),
    }


def main() -> None:
    try:
        print()
        print("Testing artifact sorter...")
        artifacts: list[dict] = [
            {'name': 'Crystal Orb', 'power': 85, 'type': 'crystal'},
            {'name': 'Fire Staff', 'power': 92, 'type': 'fire'}
        ]
        sorted_artifacts: list[dict] = artifact_sorter(artifacts)
        print(f"{sorted_artifacts[0].get('name')} "
              f"({sorted_artifacts[0].get('power')} power) comes before "
              f"{sorted_artifacts[1].get('name')} "
              f"({sorted_artifacts[1].get('power')} power)")
        print()
        print("Testing spell transformer...")
        print(spell_transformer(['fireball', 'heal', 'shield']))
    except (ValueError, TypeError, IndexError, KeyError) as error:
        print(error)


if __name__ == "__main__":
    main()
