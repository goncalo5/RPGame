SCREEN = '800x650'
FORMATED_OPTIONS = "[{}]  "
MENU = ["move", "select item", "exit"]
INFO = {"location": "forest", "health": 100, "energy": 100,
        "items": {}, "selected_item": None}
SITES = {
    "city": {
        "options": {"house", "market", "smith"},
    },
    "forest": {
        "options": {
            "Pick wood": {"energy": -10, "wood": 1},
            "Plant a tree": {"energy": -20, "tree": -1},
            "Pick apples": {"energy": -5, "apples": 1},
            },
        "probabilities": {"tree": 0.1, "apples": 0.2},
        "wood": 2, "apples": 10,
    },
    "mine": {},
}