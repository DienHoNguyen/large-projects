#uhhh idk
import random

airport = {
    0: 'Runway',
    1: 'Taxi A1',
    2: 'Taxi A2',
    3: 'Taxi A3',
    4: 'taxi A4',
    5: 'Taxi B1',
    6: 'Taxi B2',
    7: 'taxi B3',
    8: 'taxi B4',
    9: 'Gate 1',
    10: 'Gate 2'
}

airlines = ['AAL', 'UAL', 'DAL']
random_airlines = random.choice(airlines)
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)
num4 = random.randint(0, 9)
print(f'{airlines} {num1}{num2}{num3}{num4}')
