from can import ALL_SKILLS
from game import Game, GameOptions
from loadout import Loadout
from item_data import all_items
from connection_data import VanillaAreas
from location_data import pullCSV
import logicExpert
from Main import Main

name_by_slug = {
    'bomb': 'Bombs',
    'spring-ball': 'Springball',
    'grappling-beam': 'Grapple Beam',
    'hi-jump-boots': 'HiJump',
    'spazer-beam': 'Spazer',
}

item_by_name = {}
item_by_slug = {}

SKIPS = ['draygon', 'phantoon', 'kraid', 'ridley']

for name, item in all_items.items():
    slug = name.lower().replace(' ', '-')
    name_by_slug[slug] = name
    item_by_name[name] = item
    item_by_slug[slug] = item

def get_logic(slug):
    return logicExpert


def randomize(options):
    return Main(options)


def get_locations(options):
    logic = get_logic(options.get('logic'))
    game_options = GameOptions(
        logic,
        fill_choice='MM',
        can=[]
    )
    csvdict = pullCSV()
    game = Game(
        game_options,
        logic,
        csvdict,
        False, # area rando
        VanillaAreas())
    loadout = Loadout(game)
    for slug, quantity in options['inventory'].items():
        if slug in SKIPS:
            continue
        name = name_by_slug[slug]
        item = item_by_name[name]
        loadout.contents[item] = quantity
    locations = {}
    for name, func in logic.location_logic.items():
        locations[name] = func(loadout)
    return locations

def get_schema():
    schema = {
        'type': 'object',
        'required': ['logic', 'can'],
        'properties': {
            'logic': {
                'type': 'string',
                'enum': ['expert'],
                'default': 'expert',
            },
            'can': {
                'type': 'array',
                'default': [],
                'items': {
                    'type': 'string',
                    'enum': list(ALL_SKILLS.keys()),
                    'enumNames': list(ALL_SKILLS.values()),
                }
            }
        }
    }
    return schema


if __name__ == '__main__':
    import json
    import sys
    from collections import defaultdict
    options = {
        'logic': 'expert',
        'inventory': defaultdict(int),
    }
    args = sys.argv[1:]
    while args:
        arg = args.pop(0)
        if arg == '--logic':
            options['logic'] = args.pop(0)
        elif arg == '--inventory':
            names = args.pop(0).split(',')
            for name in names:
                options['inventory'][name] += 1
    print(json.dumps({
        'locations': get_locations(options),
        'schema': get_schema(),
    }))
