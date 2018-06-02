import re

pattern = r"^[+-]?\d*\.\d+$"

T = int(input())
for _ in range(T):
    if re.match(pattern, input()):
        print(True)
    else:
        print(False)