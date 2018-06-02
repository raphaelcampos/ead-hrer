n = int(input())
result = n%2

if result == 1 :
    print('Weird')
elif result == 0 and n >= 2 and n <= 5:
    print('Not Weird')
elif result == 0 and n >= 6 and n <= 20:
    print('Weird')
else:
    print('Not Weird')