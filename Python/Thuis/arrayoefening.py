getallen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"het 5e getal is: {getallen[4]}")

# Negatief indexen kan ook, is handig als je niet weet hoe lang de list is en het laatste getal wil hebben:

print(f"Negatieve index [-1]: {getallen[-1]}")

# Multdimensionale listen zijn ook een ding:

multidim = [[1, 2, 3], "multidimensionaal", ["a", "b", "c"], 8]

print(f"2e array 2e karakter is: {multidim[2][1]}")
print(f"laatste karakter van multidim is: {multidim[-1]}")

# Kijken in arrays of het dingen bevat

a = [1, 2, 3, 4, 4, 4, 4, 4]
if 3 in a:
    print("in array a zit 3")
else:
    print("geen 3 in array a")

b = a.count(4)
print(f"in array a zit het getal 4 {b} keer")
