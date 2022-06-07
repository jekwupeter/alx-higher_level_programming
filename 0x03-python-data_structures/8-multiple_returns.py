#!/usr/bin/python3
def multiple_returns(sentence):
    """
    multiple_returns - Returns string lenght and first char
    @sentence: Input string
    """
    if isinstance(sentence, str):
        if len(sentence) != 0:
            buffer = [len(sentence), sentence[0]]
        else:
            buffer = [len(sentence), None]
        buffer = tuple(buffer)
        return buffer
