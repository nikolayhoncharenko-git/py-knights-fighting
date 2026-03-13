from app.Knight import Knight


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


def summon_knight(knight_base: list, name: str) -> Knight:
    out_knight = None
    for knight in knight_base:
        if knight.name == name:
            out_knight = knight

    return out_knight


def get_knight_base(base: dict) -> list:
    out_list = []
    for key, value in base.items():
        out_list.append(Knight.get_knight(value))

    return out_list


def fight(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection


def fix_death(knight: Knight) -> None:
    if knight.hp <= 0:
        knight.hp = 0


def battle(knights_config: dict) -> dict:
    knights = get_knight_base(knights_config)

    lancelot = summon_knight(knights, "Lancelot")
    arthur = summon_knight(knights, "Arthur")
    mordred = summon_knight(knights, "Mordred")
    red_knight = summon_knight(knights, "Red Knight")

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    for knight in knights:
        fix_death(knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
