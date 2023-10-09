#!/usr/bin/python3
def multiple_returns(sentence):
    lent = len(sentence)
    if lent == 0:
        first_char = None
        _tuple = (lent, first_char)
        return _tuple
    else:
        first_char = sentence[0]
        _tuple = (lent, first_char)
        return _tuple
