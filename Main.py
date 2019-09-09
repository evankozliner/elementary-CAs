import argparse
from InitialConditions import MiddleStateIsOne, RandomState, FarRightIsOne
from Rules import simple_rule, apply_elementary_rule, rule_110
from Automata import Automata

def main():
    args, initial_condition = parse_args()
    # Always multiply the number of evolutions by 2 to get the length of each row. 
    # This produces cleaner images.
    automata = Automata(initial_condition(args.evolutions * 2), apply_elementary_rule(args.rule_number))
    automata.evolve(len(automata.state))

def parse_args():
    parser = argparse.ArgumentParser(description="Build elementary cellular automata.") 
    parser.add_argument('-e', '--evolutions', default=16, type=int, help="The number of evolutions for the CA.")
    parser.add_argument('-r', '--rule_number', default=30, type=int, help="The rule number for the cellular automata.")
    parser.add_argument('-s', '--state', default=0, type=int, help="The initial conditions for the first row.\n0: Middle is *. Other cells are -. (default)\n1: Random initial row\n2:Far right is *. (*). Other cells are -.")

    args = parser.parse_args()
    initial_conditions_map = {
        0: MiddleStateIsOne,
        1: RandomState,
        2: FarRightIsOne
    }
    if not args.state in initial_conditions_map.keys():
        raise ValueError("Input '{}' for state is not valid. Please choose 0, 1 or 2.".format(args.state))

    return args, initial_conditions_map[args.state]

if __name__ == "__main__":
    main()
