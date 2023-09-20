def checkYearIsLeap(year):
    if (year % 400 == 0) and (year % 100 == 0):
        print("{0} is a leap year".format(year))
    elif (year % 4 == 0) and (year % 100 != 0):
        print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))

def checkNumberIsPrime(number):
    flag = True
    if number == 1:
        flag = False
    else:
        for i in range(2, number):
            if number % i == 0:
                flag = False
                break
    if flag:
        print("{0} is Prime".format(number))
    else:
        print("{0} is not Prime".format(number))
def convertDecimalToOther(dec_number):
    print(bin(dec_number), "in binary.")
    print(oct(dec_number), "in octal.")
    print(hex(dec_number), "in hexadecimal.")
#.1
print("Hello, world")

#.2
year = 2016
checkYearIsLeap(year)

#.3
num = 407
checkNumberIsPrime(num)

#.3
dec = 344
convertDecimalToOther(dec)