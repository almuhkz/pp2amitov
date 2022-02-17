def toCentigrade(F):
    celcius = (5 / 9)*(F - 32)
    return celcius
farenheit = int(input("Enter temperature in Farenheit: "))
print("Temperature in Celcius: "+ str(toCentigrade(farenheit)))
