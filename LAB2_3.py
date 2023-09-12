name = input('Enter the name: ')
age = int(input(f'Enter the {name}\'s age: '))

if age < 10:
    age_group = '0대'
elif (10 <= age < 20):
    age_group = '10대'
elif (20 <= age < 30):
    age_group = '20대'
elif (30 <= age < 40):
    age_group = '30대'
elif (40 <= age < 50):
    age_group = '40대'
else:
    age_group = '50대 이상'
    
print(f'{name}은 {age_group}이다')