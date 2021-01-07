# Hourly product made
# designing

# formula: [boxes on pallet] x [outers in box]

# how many boxes on the pallet?
# how many pallets out?


def calc_board(outers, *cases):
    total_cases = 0
    for case in cases:
        total_cases += int(case)
    print(outers * total_cases)