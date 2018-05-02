import random
import numpy as np

# Funcion llamada sort_doors() que retorna la lista desordenada aleatoriamente. 

def sort_doors():

	list = ['goat','goat','car']
	random.shuffle(list)
	return list
	
print "Reshuffled list : ", sort_doors()

# Funcion llamada choose_door() que retorna un numero aleatorio entre 0,1 y 2

def choose_door():

	list = [0,1,2]
	rand = np.random.choice(list)
	return rand

print "Eleccion del participante : ", choose_door()

# Recorre la lista en los espacios que no incluyen a choice y cuando encuentra la primera cabra y modifica su valor por GOAT_MONTY

def reveal_door(lista, choice):

	for i in range (len(lista)):
		if ((choice != i) & (lista[i] =='goat')):
			lista[i] = 'GOAT_MONTY'
			return lista

print reveal_door(sort_doors(), choose_door())

def truefalse():

	list = [True, False]
	randbool = np.random.choice(list)
	return randbool


def finish_game(lista,choice,change):

	for i in range (len(lista)):
		if ((change == True) & (lista[i] != 'GOAT_MONTY') & (lista[i] != lista[choice])):
			return lista[i]
		else:
			return lista[choice]

print finish_game(sort_doors(), choose_door(),False)
print finish_game(sort_doors(), choose_door(),True)
print finish_game(sort_doors(), choose_door(),truefalse())

	
#def game(lista,choice,change):
#	countertrue = 0
#	counterfalse =0
#	while (counterfalse <101 or counterfalse <101):
#		for i in range (len(lista)):
#			if ((change == True) & (lista[i] != 'GOAT_MONTY') & (lista[i] != lista[choice])):
#				countertrue = countertrue+1
#			else:
#				counterfalse = counterfalse+1
#
#	return counterfalse, countertrue


# Se definen las listas
# Simular el juego una cantidad de 100 veces, se guarda  el  valor  del  resultado  en  una  lista, y se imprime un  mensaje  con #la  probabilidad  de  obtener  el  premio  cuando  no  hubo  cambio  de  puerta  y  la  probabilidad respectiva cuando si hubo 
#cambio de puerta


listtrue=[]

listfalse=[]

for i in range(100): 

	n = choose_door()	

	listtrue.append(finish_game(reveal_door(sort_doors(), n), n , True))
	
	listfalse.append(finish_game(reveal_door(sort_doors(), n), n , False))	

counter = 0
plus= 1

for i in range (len(listtrue)): 
	if(listtrue[i] == "car"):
		counter= counter+ plus  	
print "The probability of winning changing door is: ", counter,"%"

counterB = 0 

for i in range(len(listfalse)):

	if(listfalse[i] == "car"):
		counterB = counterB+ plus
print "The probability of winning without changing door is: ", counterB,"%"


