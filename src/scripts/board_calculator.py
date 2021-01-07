# Hourly product made

# formula: [boxes on pallet] x [outers in box]

# how many boxes on the pallet?
# how many pallets out?
def calc_print_user_board():
    outers = input("Outers per case: ")
    cases = input("Cases: ")
    print(f"Total outers: {_simple_calc_board(outers, cases)}")


def _simple_calc_board(outers, cases):
    return int(outers) * int(cases)


def _calc_board(outers, *cases):
    total_cases = 0
    for case in cases:
        total_cases += int(case)
    return int(outers) * int(total_cases)
