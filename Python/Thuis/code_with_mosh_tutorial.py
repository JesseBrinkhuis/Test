# https://www.youtube.com/watch?v=_uQrJ0TkZlc

naam = "Menno"
print(type(naam))  # print de datatype

# Exercise weight conversion

gewicht_pnd = 40  # int(input("Wat is je gewicht in pnd? ")) #uitgecomment anders moet ik m steeds invullen
gewicht_kg = gewicht_pnd * 0.4535

print("Je gewicht in kg = " + str(gewicht_kg))


# Verschil tussen double en single quotes

# string1 = 'Single quotes voor een "double quote"'
# string2 = "Double quotes voor een 'single' quote"
# string 3 = '''Tekst met
# enters
#'''

# Strings
string = "Hoi ik ben Menno"
string2 = "Citroen"
print(string[1])
print(string[11:17])
print(string[4:])  # print van eerste getal tot einde
print(string[1:-1])
print(len(string2))  # Print de hoeveelheid karakters
print(string2.find("r"))
print(string.replace("ben", "heet"))
print("Menno" in string)  # Boolean of iets ergens in zit

print("-----------------------------------------------------------------------------")
# Operators voor calculations
print(10 / 3)  # Deling
print(10 // 3)  # Deling zonder komma
print(10 % 3)  # Wat blijft er over als alles er 'heel' inpast
print(10**3)  # Tot de macht

getal = 14
getal += 3
print(getal)

getal2 = -7.32423
print(round(getal2))
print(abs(getal2))

import math

# maakt dingen als 'math.cos' mogelijk, handig met formules en rekenen
print(math.ceil(abs(getal2)))
print(math.floor(abs(getal2)))

print("-----------------------------------------------------------------------------")

# if statements and while loops and for loops
prices = [10, 20, 30]
total = 0

for price in prices:
    total += price
print(f"de totaalprijs is {total}")

# while loop kan ook een 'else' hebben
# kan ook and not gebruiken, javascript zou dat ! zijn


# range functie:
for item in range(3, 10, 2):  # Print TOT niet tot en met het ingevoerde getal
    print(item)

# Loop nesting, handig voor bijv coordinaten
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

print("-----------------------------------------------------------------------------")

# lists
# Oefenopdrachtje: vind hoogste getal in lijst

getallen = [1, 7, 23, 65, 2, 7564]
hoogste = max(getallen)
print(f"Het hoogste getal is {hoogste}")

