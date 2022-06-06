#!/usr/bin/python3
def multiple_returns(sentence):
    """
    multiple_returns - Returns string lenght and first char
    @sentence: Input string
    """
    if instance(sentence, string):
        buffer = [len(sentence), sentence[0]]
        buffer = tuple(buffer)
        return (buffer)
