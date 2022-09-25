"""
CP1404 - Practical no 02
Temp conversions - f to c - vice versa
Mason McKenzie
"""

MENU = """C - From Celsius to Fahrenheit
F - From Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("conversion: {:.3f} F".format(fahrenheit))
    elif choice == "F":
        # converting 'f' to 'c'
        fahrenheit = float(input("Fahrenheit : "))
        celsius = (fahrenheit - 32) * 5 / 9
        print("conversion: {:.3f} C".format(celsius))
    else:
        print("not valid")
    print(MENU)
    choice = input(">> ").upper()
print("Goodbye.")
