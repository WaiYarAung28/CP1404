celsius: float = float(input('Enter temperatures in Celsius: '))
fahrenheit: float = float(input('Enter temperatures in Fahrenheit: '))
def main():
    celsius_to_fahrenheit(celsius)
    fahrenheit_to_celsius(fahrenheit)

def celsius_to_fahrenheit(celsius):
    fahrenheit: float = (celsius * 9 / 5) + 32
    print(f'{celsius:.2f} C is {fahrenheit:.2f} F')

def fahrenheit_to_celsius(fahrenheit):
    celsius: float = (fahrenheit - 32) * 5 / 9
    print(f'{fahrenheit} F is {celsius:.2f} C')

main()
