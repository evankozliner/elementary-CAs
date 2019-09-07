import math
from InitialConditions import MiddleStateIsOne, RandomState, FarRightIsOne
from Rules import simple_rule, apply_elementary_rule, rule_110
0
def main():
    size = 32
    automata = Automata(MiddleStateIsOne(size), apply_elementary_rule(30))
    automata.evolve(len(automata.state))

class Automata:
    def __init__(self, initial_condition, rule):
        self.state = initial_condition.state
        self.rule = rule

    def evolve(self, steps):
        for i in range(math.floor(steps / 2)):
            self.state = self.rule(self.state)

if __name__ == "__main__":
    main()
