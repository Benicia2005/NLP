def fsm(inputs):
    state = 0
    for char in inputs:
        if state == 0 and char == 'a':
            state = 1
        elif state == 1 and char == 'b':
            state = 2
        else:
            state = 0
    return state == 2
print(fsm('ab'))
print(fsm('aab')) 
