#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        if sentence == "":
            sentence[0] = None
        t = len(sentence), sentence[0]
        return t
