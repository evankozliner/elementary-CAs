import math
import random

class InitialCondition:
    def __init__(self, size = 64):
        self.size = size

class FarRightIsOne(InitialCondition):
    def __init__(self, size):
        self.state = self._build_state(size)
        InitialCondition.__init__(self, size)

    def _build_state(self, size):
        state = [0] * size
        state[-1] = 1
        return state

class MiddleStateIsOne(InitialCondition):
    def __init__(self, size):
        self.state = self._build_state(size)
        InitialCondition.__init__(self, size)

    def _build_state(self, size):
        state = [0] * size
        middle_index = math.floor(len(state) / 2) - 1
        state[middle_index] = 1
        return state

class RandomState(InitialCondition):
    def __init__(self, size):
        self.state = [random.randint(0,1) for i in range(size)]

        InitialCondition.__init__(self, size)

