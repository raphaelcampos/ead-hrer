def swap_case(s):
    result = ""
    for c in s:
        result += c.upper() if c.islower() else c.lower()
    return result