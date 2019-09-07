from functools import wraps

def print_star_dashes(rule):
    mapping = {0: '-', 1: '*'}

    @wraps(rule)
    def print_rule(state):
        print(''.join( [mapping[s] for s in state] ))
        return rule(state)
    return print_rule

@print_star_dashes
def repeat_rule(state):
    return state

@print_star_dashes
def simple_rule(state):
    new_state = []
    for index, cell in enumerate(state):
        if index == 0:
            new_state.append(1 if state[1] == 1 else 0)
        elif index == len(state) - 1:
            new_state.append(1 if state[-1] == 1 else 0)
        else:
            new_state.append(0 if state[index - 1] == state[index + 1] else 1)

    return new_state

@print_star_dashes
def rule_30(state):
    state = list(map(int, state))
    new_state = []
    for index, cell in enumerate(state):
        if index == 0:
            new_state.append(0 ^ (state[index] | state[index + 1]))
        elif index == len(state) - 1:
            new_state.append(state[index - 1] ^ (state[index] | 0))
        else:
            new_state.append( state[index - 1] ^ (state[index] | state[index + 1] ))


    return new_state

@print_star_dashes
def rule_110(state):
    state = list(map(int, state))
    new_state = []
    # elemntary cellular automata
    # 110 in binary 
    # rule = [(110/pow(2,i)) % 2 for i in range(8)]
    #rule = [0, 1, 1, 1, 0, 1, 1, 0]
    rule = list(map(int, list(str(bin(110))[2:].zfill(8))))
    for index, cell in enumerate(state):
        if index == 0:
            new_state.append(rule[2 * state[index] + state[index + 1]])
        elif index == len(state) - 1:
            new_state.append( rule[4 * state[index - 1]  + 2 * state[index]] )
        else:
            new_state.append( rule[4 * state[index - 1] + 2 * state[index] + state[index + 1]] )


    return new_state

# TODO numpy
def apply_elementary_rule(rule_num):

    @print_star_dashes
    def apply_rule(state):
        state = list(map(int, state))
        new_state = []
        # TODO comment
        rule = list(reversed(list(map(int, list(str(bin(rule_num))[2:].zfill(8))))))
        for index, cell in enumerate(state):
            if index == 0:
                new_state.append(rule[2 * state[index] + state[index + 1]])
            elif index == len(state) - 1:
                new_state.append( rule[4 * state[index - 1]  + 2 * state[index]] )
            else:
                new_state.append( rule[4 * state[index - 1] + 2 * state[index] + state[index + 1]] )


        return new_state
    
    return apply_rule

