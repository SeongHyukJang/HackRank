def mutate_string(string, position, character):
    res = list(string)
    res[position] = character
    return "".join(res)
