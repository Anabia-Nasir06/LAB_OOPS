from rational import Rational 

class App:
    
    def run(self):
        
        num1=Rational(4,4)
        num2=Rational(8,16)

        print("THe addition of num1", num1 ,"and num2",num2 ,"is", num1+num2)
        print("THe addition of num1", num1 ,"and num2",num2 ,"is", num1-num2)

        print(f"The Greatest Common Divisor of {num1.num}/{num1.deno} is:",num1.GCD(4,4))
        print(f"The Least Common Multiple of {num2.num}/{num2.deno} is:",num2.LCM(8,16))

        num3=Rational(4,1) #--> Raises Value Error for the denominator