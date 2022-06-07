#!/usr/bin/python3
def multiple_returns(sentence):
    total_str = len(sentence)
    char = sentence[0] if total_str > 0 else "None"
    new_str = total_str, char
    return(new_str)
