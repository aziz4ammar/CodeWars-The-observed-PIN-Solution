import itertools

def get_pins(observed):
    adjacent_digits = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['0', '5', '7', '8', '9'],
        '9': ['6', '8', '9']
    }

    # Generate adjacent digits for each observed digit
    adjacent_digits_list = []
    for digit in observed:
        adjacent_digits_list.append(adjacent_digits[digit])

    # Generate all possible combinations using itertools.product
    possible_combinations = list(itertools.product(*adjacent_digits_list))

    # Convert combinations to strings
    pin_list = [''.join(combo) for combo in possible_combinations]

    return pin_list
