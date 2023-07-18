
import random
number = random.randint(-10000, 10000)
num22 = str(number)
num = (num22[-1:])
if int(num) == 0:
    print("Last digit of {} is {} and is 0".format(number, num))
elif int(num) > 5 and number < 0:
    print("Last digit of {} is -{} and is less than 6 and not 0".format(number, num))
elif int(num) < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, num))
elif int(num) > 5 and number > 0:
    print("Last digit of {} is {} and is greater than 5".format(number, num))