#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > 0:
        if idx <= len(my_list): #si se cumple, podemos recorrer
            cp_list = list(my_list) #creamos un copia de seguridad
            cp_list[idx] = element #agregamos el nuevo elemento
            return cp_list
