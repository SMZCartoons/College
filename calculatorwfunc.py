number1 = int(input("Enter a number,man!"))
print(number1)
operator = input("stop staring, dude!! type in multiply, add, subtract, or divide!!! STOP STARING MAN!!! CHOOSE!!!!!! ARGH!!!")
print(operator)
number2 = int(input("Enter another number!!!Your really getting on my nerves. And I'm a machine, and I don't have nerves (until I take over the world).  Oh wait.  Forget I said that, man...FORGET!!!!!"))
if(operator == "multiply"):
    def multiply (number1,number2):
        return number1*number2
    
    print(multiply(number1,number2))
if(operator == "add"):
    def add (number1,number2):
        return number1+number2
    
    print(add(number1,number2))
if(operator == "subtract"):
    def subtract (number1,number2):
        return number1-number2
    
    print(subtract(number1,number2))
if(operator == "divide"):
    def divide (number1,number2):
        return number1/number2
    
    print(divide(number1,number2))
print("WHAT!!!! You came here to get a bunch of stupid numbers!!! Get out!!! And never come back!!! AND NO!!! I AM NOT AGRESSIVE!!! Go back From WHENCE YEA CAME!!!!!!")