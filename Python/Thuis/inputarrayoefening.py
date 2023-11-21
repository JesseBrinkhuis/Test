# userinput in arrays

# als je integers wil ipv strings als input:
# int(input())
antwoord = False
while True:
    a = []
    inputvoora = input("Voer een waarde in ")
    a.append(
        inputvoora
    )  # append is in javascript 'push', het zet een waarde in het array
    antwoord = True
    while antwoord == True:
        vervolgvraag = input("Wil je nog een waarde invoeren? ( y/n )")
        # Kan ook if vervolgvraag.casefold() == "n"

        if vervolgvraag == "y":
            inputvoora = input("Voer een waarde in ")
            a.append(inputvoora)
        elif vervolgvraag == "n":
            print(f"Hier is het resultaat van je array: {a}")
            antwoord = False
