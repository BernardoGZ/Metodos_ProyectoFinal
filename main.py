# Proyecto Final: Cadenas de Markov
# Bernardo García  |   A00570682
# 20 de octubre de 2022
# Métodos cuantitativos

import numpy as np
from random import randint, random, uniform

def random_matrix(size = 3):
    #Initializing matrix and lists to be added
    matrix = np.zeros(shape=(size, size))

    #Constructing the matrix
    for x in range(size):
        n = 1
        acum = 0
        for y in range(size):
            if(y == size-1):
                n = 1 - acum
            else:
                n = round(uniform(0, 1 - acum), 2)

            matrix[x][y] = n
            acum += n
            # print(matrix)  
    
    return matrix

def random_warriors(size = 3, max_warriors = 10):
    return np.random.randint(low = 1, high= max_warriors, size = size)

def choose_poor_guy(size = 3):
    return randint(0, size-1)

def attack(team_number, poor_guy):
    pass



if __name__ == '__main__':
    #Variables iniciales pueden ser elegidas por el usuario
    
    # sel = input("Deseas ingresar los valores iniciales por tu cuenta? Y/N")
    # teams_quantity = input("Ingresa la cantidad de equipos: ")
    # max_warriors = input("Ingresa la cantidad maxima de guerreros: ")

    teams_quantity = 5
    max_warriors = 10
    
    sel = "N"

    if (sel == "N" or sel == "n"):
        main_matrix = random_matrix(teams_quantity)
        teams = random_warriors(teams_quantity, max_warriors)
    else:
        pass

    playing = True
    print(main_matrix)
    
    while(playing):
        aux_list = []
        turn = randint(0, teams_quantity-1)
        poor_guy = choose_poor_guy(teams_quantity)
        print(teams)
        teams[poor_guy] -= 1
        if 0 in teams:
            print(teams)
            if len(teams) == 2:
                playing = False
            else:
                for x in teams:
                    if x != 0:
                        aux_list.append(x)
                teams = aux_list
                teams_quantity = len(teams)
                main_matrix = random_matrix(teams_quantity)
                print(teams)
                print(main_matrix)

    print(teams)
    print(main_matrix)


