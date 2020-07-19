def spam():
    global eggs
    eggs = 'spam' # This is a global

def bacon():
    eggs = 'bacon' # This is a local

def ham():
    print(eggs) # This is the global

eggs = 42 # This is a global
spam()
print(eggs)