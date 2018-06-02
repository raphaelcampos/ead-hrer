def count_substring(string, sub_string):
    total = 0
    for i in range(len(string)):
        total += string.count(sub_string, i, i + len(sub_string))
    return total