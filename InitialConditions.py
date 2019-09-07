import numpy as np
import math

class InitialCondition:
    def __init__(self, size = 64):
        self.size = size

class FarRightIsOne(InitialCondition):
    def __init__(self, size):
        self.state = self._build_state(size)
        InitialCondition.__init__(self, size)

    def _build_state(self, size):
        state = np.zeros(size)
        state[-1] = 1
        return state

class MiddleStateIsOne(InitialCondition):
    def __init__(self, size):
        self.state = self._build_state(size)
        InitialCondition.__init__(self, size)

    def _build_state(self, size):
        state = np.zeros(size)
        middle_index = math.floor(len(state) / 2) - 1
        state[middle_index] = 1
        return state

class RandomState(InitialCondition):
    def __init__(self, size):
        self.state = np.random.randint(2, size=size)
        InitialCondition.__init__(self, size)

