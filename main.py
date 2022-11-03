# Proyecto Final: Cadenas de Markov
# Bernardo García  |   A00570682
# 20 de octubre de 2022
# Métodos cuantitativos

import numpy as np
from random import randint, random, uniform

'''
Print functions
'''

def print_initial(matrix, teams):
    result = print_matrix(matrix) + '\n'
    result += print_teams(teams)
    return result

def print_matrix(matrix):
    return str(matrix)

def print_teams(teams):
    result = f'''Number of warriors for each group \n'''
    for x in range(len(teams)):
        result += f'Group {x+1} : {teams[x]}\n'
    return result

def print_attack(attacker, poor_guy, teams):
    result = f'\nGroup {attacker+1} attacked Group {poor_guy+1}!\n'
    result += print_teams(teams)
    return result

def print_annihilation(status = 0, poor_guy = 0, winner = 0):
    if status == 1:
        result = f'''Group {poor_guy+1} is annihilated!

===============================
Group {winner+1} is the winner!
==============================='''
    else:
        result = f'''Group {poor_guy+1} is annihilated!

=================================
Reconfiguring stochastic matrix
'''
    return result

'''
    General project functions
'''


def random_matrix(size = 3):
    #Initializing matrix and lists to be added
    matrix = np.zeros(shape=(size, size))

    #Constructing the matrix
    for x in range(size):
        n = 1
        acum = 0
        if x == size-1:
            size_to_compare = 2
        else:
            size_to_compare = 1
        for y in range(size):
            if(x == y):
                matrix[x][y] = 0.0
            else:
                if(y == size-size_to_compare):
                    n = 1 - acum
                else:
                    n = round(uniform(0, 1 - acum), 1)

                matrix[x][y] = n
                acum += n
                # print(matrix)
    
    return matrix

def random_warriors(size = 3, max_warriors = 10):
    return np.random.randint(low = 1, high= max_warriors, size = size)

def choose_poor_guy_v1(size = 3, team_number = 0):
    n = -1
    while (n != team_number):
        n = randint(0, size-1)
    return n
    
def choose_poor_guy_v2(team_number, main_matrix):
    probability_list = []
    team_probs = main_matrix[team_number] * 10
    team_probs = [int(x) for x in team_probs]
    # print(team_probs)
    # for x in range(10):
    for y in range(len(team_probs)):
        while team_probs[y] != 0:
            probability_list.append(y)
            team_probs[y] -= 1
    
    num_attack = randint(0, 8)
    return probability_list[num_attack]



if __name__ == '__main__':
    #Variables iniciales pueden ser elegidas por el usuario
    
    # sel = input("Deseas ingresar los valores iniciales por tu cuenta? Y/N")

    teams_quantity = 5
    max_warriors = 10    
    sel = "N"

    if (sel == "N" or sel == "n"):
        # teams_quantity = int(input("Ingresa la cantidad de equipos: "))
        # max_warriors = int(input("Ingresa la cantidad maxima de guerreros: "))
        main_matrix = random_matrix(teams_quantity)
        teams = random_warriors(teams_quantity, max_warriors)
    else:
        pass

    playing = True

    # Game starts!    
    resultados = "Initial matrix \n"
    resultados += print_initial(main_matrix, teams)

    while(playing):
        aux_list = []
        turn = randint(0, teams_quantity-1)
        poor_guy = choose_poor_guy_v2(turn, main_matrix)
        teams[poor_guy] -= 1
        resultados += print_attack(turn, poor_guy, teams)
        if 0 in teams:            
            if len(teams) == 2:
                playing = False
                resultados += print_annihilation(1, poor_guy, turn)
            else:
                for x in teams:
                    if x != 0:
                        aux_list.append(x)
                teams = aux_list
                teams_quantity = len(teams)
                main_matrix = random_matrix(teams_quantity)
                resultados += print_annihilation(0, poor_guy)
                resultados += print_matrix(main_matrix)

    with open("resultados.txt", "w") as f:
        f.write(resultados)

