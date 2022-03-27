import numpy as np

def construieste_solutia_bidirectional(nod_comun, parinti1, parinti2, start, stop):
    solutie = []

    nod_curent = nod_comun
    solutie.append(nod_curent)

    while nod_curent != start:
        nod_curent = parinti1[nod_curent]
        solutie.append(nod_curent)
        #print("while 1 ")

    #print(solutie)
    solutie = solutie[::-1]

    nod_curent = nod_comun
    while nod_curent != stop:
        nod_curent = parinti2[nod_curent]
        solutie.append(nod_curent)
        #print("while 2 ")
    solutie = solutie[::-1]

    print(f"Solutia este {solutie}")

    return solutie

orase = ["Constanta", "Tulcea", "Braila", "Piatra Neamt", "Iasi",
         "Suceava", "Bistrita", "Targu Mures", "Sibiu", "Brasov",
         "Pitesti", "Bucuresti", "Craiova", "Alba Iulia", "Cluj Napoca",
         "Baia Mare", "Satu Mare", "Oradea", "Arad", "Timisoara"]
''' 
Constanta = 0 |Tulcea = 1 |Braila = 2 |Piatra Neamt = 3 |Iasi = 4 |
Suceava = 5 |Bistrita = 6 |Targu Mures = 7 |Sibiu = 8 |Brasov = 9 |
Pitesti = 10 |Bucuresti = 11 |Craiova = 12 |Alba Iulia = 13 |Cluj Napoca = 14 |
Baia Mare = 15 |Satu Mare = 16 |Oradea = 17 |Arad = 18 |Timisoara = 19 |
'''

# construim matricea de adiacenta = legaturile dintre noduri
m = np.zeros([20, 20], int)

m[0, 1] = 1
m[0, 11] = 1
m[1, 2] = 1
m[2, 3] = 1
m[2, 11] = 1
m[3, 4] = 1
m[3, 11] = 1
m[3, 9] = 1
m[4, 5] = 1
m[5, 6] = 1
m[6, 7] = 1
m[6, 14] = 1
m[7, 14] = 1
m[7, 8] = 1
m[7, 9] = 1
m[8, 9] = 1
m[8, 13] = 1
m[9, 10] = 1
m[9, 11] = 1
m[10, 11] = 1
m[10, 12] = 1
m[12, 13] = 1
m[12, 19] = 1
m[13, 14] = 1
m[13, 19] = 1
m[14, 15] = 1
m[14, 17] = 1
m[14, 18] = 1
m[15, 16] = 1
m[16, 17] = 1
m[17, 18] = 1
m[18, 19] = 1

# aducem matricea de ad.  la o forma simetrica
for i in range(20):
    for j in range(20):
        if m[i, j] == 1:
            m[j, i] = 1

start = 7
stop = 5

''' # input din tastatura
while True:
    start = int(input("Introduceti nod start "))
    stop = int(input("Introduceti nod stop "))
    if start == stop:
        print("Orasul de start nu trebuie sa fie acelasi cu orasul de stop ! ")
        start = int(input("Introduceti nod start "))
        stop = int(input("Introduceti nod stop "))
    else:
        break
'''
noduri1 = np.array([start], int)  # primul cauta de la start la stop
vizitate1 = np.zeros([20], int)
parinte1 = np.full([20], -1, int)
gasit_solutie1 = False

noduri2 = np.array([stop], int)  # al doilea cauta de la stop la start
vizitate2 = np.zeros([20], int)
parinte2 = np.full([20], -1, int)
gasit_solutie2 = False

orase_distincte = [start, stop]

vizitate1[start] = 1
vizitate2[stop] = 1
check = False
while (not gasit_solutie1 and len(noduri1) > 0) and (not gasit_solutie2 and len(noduri2) > 0) and not check:
    nod1 = noduri1[0]  # selectam nodul1 de pe prima pozitie din lista 1 activa drept nod1 = nod curent
    noduri1 = np.delete(noduri1, 0)  # scoatem nodul1 curent din lista

    nod2 = noduri2[0]  # selectam nodul2 de pe prima pozitie din lista 2 activa drept nod2 = nod curent
    noduri2 = np.delete(noduri2, 0)  # scoatem nodul2 curent din lista

    if nod1 == stop:
        gasit_solutie1 = True
    elif nod2 == start:
        gasit_solutie2 = True
        # !!! sa adaugam daca fiecare gaste in lista noduri a celuilalt un element comun !!!
    else:
        for q in range(20):
            # poate vreunul din algoritmi gaseste primul solutia , verificam
            if m[nod1, q] > 0 and vizitate1[q] == 0:
                noduri1 = np.append(noduri1, q)
                vizitate1[q] = 1
                parinte1[q] = nod1
            if m[nod2, q] > 0 and vizitate2[q] == 0:
                noduri2 = np.append(noduri2, q)
                vizitate2[q] = 1
                parinte2[q] = nod2
            #verificam daca algoritmul bidimensional da roate , element vizitat comun
            if vizitate1[q] == 1 and vizitate2[q] == 1:
                check = True
                sol = construieste_solutia_bidirectional(q, parinte1, parinte2, start, stop)
                for i in sol:
                    print(orase[i])
                break
if check:
    print("Solutie bidimimensionala !!! ")
elif gasit_solutie1 == True:
    print("Solutie 1  gasita")
    sol = []
    curent = stop
    sol.append(curent)
    while curent != start:
        curent = parinte1[curent]
        sol.append(curent)
    sol = sol[::-1]
    print(sol)
    for i in sol:
        print(orase[i])
elif gasit_solutie2 == True:
    print("Solutie 2 gasita")
    sol = []
    curent = start
    sol.append(curent)
    while curent != stop:
        curent = parinte2[curent]
        sol.append(curent)
    sol = sol[::-1]
    print(sol)
    for i in sol:
        print(orase[i])
else:
    print("Solutia nu exista")
