# Introduction To Programming
# Week 5 Assignment
# 25 September 2020

def Ee_igh():
    return ', Ee-igh, Ee-igh, Oh!'

def macD(animal, sound):
    print('Old MacDonald had a farm' + Ee_igh())
    print('And on the farm he had a', animal + Ee_igh())
    print('With a', sound + ',', sound, 'here and a', sound + ',' ,sound, \
          'there.')
    print('Here a', sound + ', there a', sound + ' , everywhere a', sound + \
          ',', sound + '.')
    print('Old MacDonald had a farm' + Ee_igh())

def main():
    macD('cow', 'moo')

main()
          
