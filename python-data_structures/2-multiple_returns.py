#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    char = sentence[0] if lenght > 0 else None
    return lenght, char
