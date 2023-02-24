# This codes displays a car dealership between two people
import numpy as np
c = int(input('Welcome, what is your budget for a car: GHS'))
#c=vehicle or car
print()

if c > 100000:
    print('You can purchase a Dodge Challenger')
elif 90000 <= c < 100000:
    print('You can purchase a Ford Shelby')
elif 80000 <= c < 90000:
    print('You can purchase a Bugatti')
elif 70000 <= c < 80000:
    print('You can purchase a Lamborghini')
elif 60000 <= c < 70000:
    print('You can purchase a Ferrari')
elif 50000 <= c < 60000:
    print('You can purchase a Rolls Royce')
elif 40000 <= c < 50000:
    print('You can purchase a Bently')
elif 30000 <= c < 40000:
    print('You can purchase a Lexus')
elif 20000 <= c < 30000:
    print('You can purchase an Audi')
elif 15000 <= c < 20000:
    print('You can purchase a Mercedes Benz')
elif 10000 <= c < 15000:
    print('You can purchase a Porsche')
elif 9500 <= c < 10000:
    print('You can purchase a BMW')
elif 9000 <= c < 9500:
    print('You can purchase a Chervolet')
elif 8500 <= c < 9000:
    print('You can purchase a Land Rover')
elif 8000 <= c < 8500:
    print('You can purchase a Jaguar')
elif 7500 <= c < 8000:
    print('You can purchase a Volkswagen')
elif 7000 <= c < 7500:
    print('You can purchase a Honda')
elif 6500 <= c < 7000:
    print('You can purchase a Hyundai')
elif 6000 <= c < 6500:
    print('You can purchase a Volvo')
elif 5500 <= c < 6000:
    print('You can purchase a Tesla')
elif 5000 <= c < 5500:
    print('You can purchase a Toyota')
elif 4500 <= c < 5000:
    print('You can purchase an Alpha Romeo')
elif 4000 <= c < 4500:
    print('You can purchase a Subaru')
elif 3500 <= c < 4000:
    print('You can purchase a Peugot')
elif 3000 <= c < 3500:
    print('You can purchase a Mazda')
elif 2500 <= c < 3000:
    print('You can purchase a Citreon')
elif 2000 <= c < 2500:
    print('You can purchase a Kantanka')
elif 1500 <= c < 2000:
    print('You can purchase a Saturn')
elif 1000 <= c < 1500:
    print('You can purchase a GMC')
elif 500 <= c < 1000:
    print('You can purchase a Matiz II')
elif 250 <= c < 500:
    print('You can purchase a Fiat')
else:
    print('We are sorry but you cannot afford any car from our store but we sell other car accessories if you are interested')
