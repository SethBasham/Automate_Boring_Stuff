catNames = []

while True:
    print('Enter the name of your cat ' + str(len(catNames) + 1) + 
        ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames += [name] # List concatenation

print('The cat names are: ')
for name in catNames:
    print('\t' + name)