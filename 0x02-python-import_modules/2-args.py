#!/usr/bin/python3
indice = 0 #set in zero
numbers = [1, 2, 3, 4, 5, 6]
args = ["Hello", "Welcome", "To", "The", "Best", "School"]
#funcion len() devuelve la longitu de la lista
indice = input()
while indice < len(numbers): #loop using len
    print(numbers[indice], args[indice])
    indice += 1
print(f"{indice}{numbers}, arguments:")
