# Hourly product made

# formula: [boxes on pallet] x [outers in box]

# how many boxes on the pallet?
# how many pallets out?
def calc_print_user_board():
    outers = int(input("Outers per case: "))
    cases = int(input("Cases: "))
    print(f"Total outers: {_simple_calc_board(outers, cases)}")


def _simple_calc_board(outers, cases):
    return outers * cases


def _calc_board(outers, *cases):
    total_cases = 0
    for case in cases:
        total_cases += case
    return outers * total_cases
