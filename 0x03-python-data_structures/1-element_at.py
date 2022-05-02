#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0: #no se puede imprimir
        return (None)
    else idx <= len(my_list): #puede recorrerlo
            return my_list[idx] #returna una posicion x en la lista
