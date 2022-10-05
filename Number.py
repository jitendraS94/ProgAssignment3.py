import logging
logging.basicConfig(filename="NUmber.log",level= logging.DEBUG,format="%(levelname)s %(asctime)s %(name)s %(message)s")

class NUMBER:
    logging.info("This is a number check  funtion ")
    def Check_no_p_n_z(self):
        logging.info("we are in the funtion where we Check if a Number is Positive, Negative or Zero ")
        try:
            num = int(input("Enter the any number :-"))
            logging.info("Enter number is %s", num)
            if num > 0:
                logging.info("Number is positive ")
                return "Number is positive"
            elif num < 0:
                logging.info("Number is negative ")
                return "Number is negative"
            else:
                logging.info("Number is zero ")
                return "Number is zero"

        except Exception as e:
            logging.exception(e)

    def Number_odd_even(self):
        logging.info("we are in a function where we check number is odd or even")
        try:
            num = int(input("Enter the any NUmber"))
            logging.info("Enter number is %s" , num)
            while True:
                if num%2 == 0:
                    logging.info("Number is Even")
                    return "Number is Even"
                    break
                else:
                    logging.info("Number is Odd")
                    return "Number is Odd"
                    break

        except Exception as e:
            logging.exception(e)
class leap_year:
    logging.info("This is a leap year funtion")
    def Check_Leap_Year(self):
        logging.info("Check leap year")
        try:
            year =  int(input("Enter the year which you want to print  :-"))
            logging.info("Enter year is %s :-", year)
            if (year%4 ==0 and year%400 !=0 or year%100 ==0):
                logging.info("This is leap year")
                return "This is leap year"
            else:
                logging.info("This yrear is not leep year")
                return "This yrear is not leep year"
        except Exception as e:
            logging.exception(e)

class Prime_number:
    logging.info("This is prime number funtion")
    def  prime_Number(self):
        logging.info("Program to Check Prime Number")
        try:
            num = int(input("Enter  the number :-"))
            logging.info("Enter number is %s ",num)

            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        logging.info("This is not Prime num %s ", num)
                        return "The number is not prime number :-", num
                        break
                else:
                    logging.info("This is a Prime num %s ",num)
                    return " this is a Prime num :-", num

        except Exception as e:
            logging.exception(e)

    def prime_number_interval(self):
        logging.info("Program to Print all Prime Numbers in an Interval ")
        try:
            num1 = int(input("Enter the start point number  :-"))
            num2 = int(input("Enter the end point number :-"))
            logging.info("Enter number is %s %s ",num1,num2)
            for i in range(num1,num2):
                if i > 1:
                    for j in range(2,i):
                        if i%j == 0:
                            break
                    else:
                        logging.info("Prime number is %s", i)
                        print(i,end=" ")
        except Exception as e:
            logging.exception(e)

class All_class(NUMBER,leap_year,Prime_number):
    pass




n = NUMBER
#n.Check_no_p_n_z
#print(n.Check_no_p_n_z("num"))
#n.Number_odd_even
#print(n.Number_odd_even("num"))
#y =leap_year
#y.Check_Leap_Year
#print(y.Check_Leap_Year("year"))
#p =Prime_number
#print(p.prime_Number("number"))
#p.prime_number_interval
#print(p.prime_number_interval("i"))
A = All_class
A.prime_Number
print(A.prime_Number("num"))
