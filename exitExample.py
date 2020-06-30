import sys 

while True:
    print('Type quit to exit')
    response = input()
    if response == 'quit':
        sys.exit()
    print('You typed ' + response + '.')