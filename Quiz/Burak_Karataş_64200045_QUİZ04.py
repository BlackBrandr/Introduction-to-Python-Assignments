def Main():
    Cel()
    Fah()

def Cel():
    Celsius = eval(input("Enter the weather heat(Celsius): "))

    fahrenheit = (Celsius * 1.8) + 32
    print(Celsius,"celsius is",fahrenheit, "fahrenheit")

def Fah():
    fahrenheit = eval(input("Enter the weather heat(Fahrenheit): "))
    celsius = (5/9) * (fahrenheit - 32)
    print(fahrenheit,"fahrenheit is",celsius, "celsius")

