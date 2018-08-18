while True:
    print('Please enter your name.')
    name = input()
    if name != 'Naoto':
        continue
    print('Hello, Naoto. What is your password? (animal\'s name)')
    password = input()
    if password == 'cat':
        break
print('Verified!')
