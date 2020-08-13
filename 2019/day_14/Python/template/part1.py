from load_input import get_input


def parse_recipe(recipe_string):
    """

    """
    parsed_recipe = {}
    for component in recipe_string.split(', '):
        quantity, chemical = component.split()
        parsed_recipe[chemical] = int(quantity)
    return parsed_recipe


def parse_input(reactions):
    """

    """
    parsed_input = {}
    for line in reactions:
        recipe, result = line.split(' => ')
        quantity, chemical = result.split()
        parsed_input[chemical] = {
            'quantity': int(quantity),
            'recipe': parse_recipe(recipe)
        }
    return parsed_input


def walk_into():
    """

    """
    pass


def calculate_total_ore(reactions):
    """

    """
    fuel_details = reactions['FUEL']
    ore = calculate_ore(fuel_details, reactions)
    total_ore = 0
    for base_chemical, base_quantity in ore.items():
        total_ore += base_quantity
    return total_ore


def calculate_ore(chemical_details, reactions):
    ore = {}
    for chemical, quantity in chemical_details['recipe'].items():
        nested_recipe = reactions[chemical]['recipe']
        if 'ORE' in nested_recipe:
            if chemical not in ore:
                ore[chemical] = 0
            ore[chemical] += quantity
        else:
            calculate_ore(nested_recipe, reactions)

    return ore


def pseudo_code():
    """
    1 fuel = 7A + 1E
    1 fuel = 7A + (7A + 1D)
           = 14A + 1D
           = 14A + (7A + 1C)
           = 21A + 1C
           = 21A + (7A + 1B)
           = 28A +1B
           = 28A + (1 ORE)
           =

    Note: dict where is just chemical, values are recipe and quantity
    """
    pass



def main():
    # temporary input (make parsing function later)
    raw_input = get_input()
    reactions = parse_input(raw_input)
    ore = calculate_total_ore(reactions['FUEL'])
    print(f'{ore} ore required')


if __name__ == "__main__":
    print(main())
