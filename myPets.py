myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name: ')
name = input().capitalize()

if name not in myPets:
    print(f'I do not have a pet named {name}')
else:
    print(f'{name} is my pets name too.')