name = input("Enter name: ")
print('(H)ello')
print('(G)oodbye')
print('(Q)uit')
choice = input("Choose").upper()
while True:
    if choice=="H":
        print(f'Hello. {name}')
    elif choice=="G":
        print(f'Goodbye, {name}')
    elif choice=="Q":
        print(f'Bye, {name}')
    print()