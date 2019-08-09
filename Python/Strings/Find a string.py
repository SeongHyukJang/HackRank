def count_substring(string, sub_string):
    res = 0
    while sub_string in string:
        res += 1
        string = string[string.index(sub_string)+1:]
    return res
