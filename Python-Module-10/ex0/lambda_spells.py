from typing import List
from collections.abc import Callable


artifact_sorter: Callable[[List[dict]], List[dict]] = (
    lambda artifacts:
    sorted(artifacts,
           key=lambda item:
           item["power"],
           reverse=True)
)

power_filter: Callable[[List[dict], int], List[dict]] = (
    lambda mages, min_power:
    list(filter(lambda power: power["power"] >= min_power, mages))
)

spell_transformer: Callable[[List[str]], List[str]] = (
    lambda spells:
    list(map(lambda string: "* " + string + " *", spells))
)

mage_stats: Callable[[List[dict]], dict] = (
    lambda mages:
    {
        "max_power": max([item["power"] for item in mages]),
        "min_power": min([item["power"] for item in mages]),
        "avg_power": round(sum([item["power"] for item in mages])
                           / len(mages), 2)
    }
)

print("Testing artifact sorter...")
artifacts = artifact_sorter([
    {'name': 'Earth Shield', 'power': 68, 'type': 'armor'},
    {'name': 'Shadow Blade', 'power': 116, 'type': 'armor'},
    {'name': 'Light Prism', 'power': 95, 'type': 'weapon'},
    {'name': 'Crystal Orb', 'power': 114,
        'type': 'accessory'}
])

artifact = " comes before ".join([f"{artifact['name']} "
                                  f"({artifact['power']})" for artifact in
                                  artifacts])
print(artifact)

print("\n\nTesting power filter...")
powers = power_filter([
    {'name': 'Luna', 'power': 85, 'element': 'ice'},
    {'name': 'Storm', 'power': 81, 'element': 'wind'},
    {'name': 'Morgan', 'power': 75, 'element': 'earth'},
    {'name': 'Sage', 'power': 97, 'element': 'light'},
    {'name': 'Alex', 'power': 67, 'element': 'ice'}
], 80)

for power in powers:
    print("power:", power["power"], end=" ")

print("\n\nTesting spell transformer...")
spells = spell_transformer([
    'shield', 'meteor', 'heal', 'earthquake'
])

for spell in spells:
    print(spell, end=" ")

print("\n\nTesting mage stats...")
mages = mage_stats([
    {'name': 'Phoenix', 'power': 75, 'element': 'shadow'},
    {'name': 'River', 'power': 53, 'element': 'water'},
    {'name': 'Riley', 'power': 67, 'element': 'wind'},
    {'name': 'Zara', 'power': 96, 'element': 'ice'},
    {'name': 'Rowan', 'power': 76, 'element': 'lightning'}
])

for mage_key, mage_value in mages.items():
    print(f"{mage_key}: {mage_value}")
