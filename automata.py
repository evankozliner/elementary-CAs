import math

class Automata:
    def __init__(self, initial_condition, rule):
        self.state = initial_condition.state
        self.rule = rule

    def evolve(self, steps):
        for i in range(math.floor(steps / 2)):
            self.state = self.rule(self.state)
