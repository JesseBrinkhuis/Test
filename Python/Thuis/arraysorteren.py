Citroen = [
    {"type": "Bx", "gewicht": 1010, "score": 10},
    {"type": "Xm", "gewicht": 1450, "score": 8},
    {"type": "Xantia", "gewicht": 1400, "score": 7},
]


def getGewicht(car):
    return car["gewicht"]


def getScore(car):
    return car["score"]


Citroen.sort(
    key=getGewicht, reverse=True
)  # Reverse laat de score aflopen, hier geef je in de key ook al de Citroen mee
print(f"Op basis van gewicht: {Citroen}")

Citroen.sort(key=getScore)
print(f"Op basis van score: {Citroen}")
