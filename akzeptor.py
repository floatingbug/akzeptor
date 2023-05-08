#return True if sign is accepted otherwise return False.
def check_is_sign_accepted(sign, allowed_signs):
    for allowed_sign in allowed_signs:
        if sign == allowed_sign:
            return True
    return False

#function to run the akzeptor.
def run(word, allowed_signs):
    word = word
    allowed_signs = allowed_signs
    curr_state = 0

    #transition to state 1 from state 0.
    for i in range(0, 10):
        if word[0] == str(i):
            curr_state = 1
            break

    #check word in state 1.
    if curr_state == 1:
        for i in range(0, len(word)):
            if not check_is_sign_accepted(word[i], allowed_signs):
                return "sign: ", word[i], " in state 1 is not accepted"
        return "word: ", word, " in state 1 ist not accepted"

    #transition to state 2 from state 0.
    if not check_is_sign_accepted(word[0], allowed_signs):
        return "sign: ", word[0], " is not allowed"

    #check word in state 2
    for i in range(1, len(word)):
        if not check_is_sign_accepted(word[i], allowed_signs):
            return "word: ", word, " is not allowed in state 2"
    return "word: ", word, " is accepted"
