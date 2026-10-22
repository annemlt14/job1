def verifie(nombre):
    if nombre %2 == 0 and nombre > 0:
        print("Pair")
    else:
        print("impair")
    
    return nombre
    
print(verifie(7))
print(verifie(12))
print(verifie(3))