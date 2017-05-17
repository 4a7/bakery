import _thread
import time
DELAY=1 #tiempo que espera en cada seccion
NT=25 #numero de threads
choosing=[False]*NT
number=[0]*NT
#retorna el numero maximo en el arreglo de numeros
def max_number():
    global choosing
    global number
    max=-1
    for i in number:
        if(i>max):
            max=i
    return max
#hace la comparacion de tuplas
def comparacion_tuplas(j,i):
    global choosing
    global number
    if(number[j]<number[i]):
        return True
    elif (number[j]==number[i] and j<i):
        return True
    return False
def lock(i):
    global choosing
    global number
    choosing[i]=True
    number[i]=max_number()+1
    choosing[i]=False
    for j in range(NT):
        while(choosing[j]):
            continue
        while(number[j]!=0 and comparacion_tuplas(j,1)):
            continue
def unlock(i):
    global choosing
    global number
    number[i]=0
def ejecutar_thread(i):
    while(True):
        lock(i)
        print("Thread "+str(i)+" en seccion critica\n")
        time.sleep(DELAY)
        unlock(i)
        print("Thread "+str(i)+" fuera de seccion critica\n")
        time.sleep(DELAY)
def bakery():
    for i in range(NT):
        _thread.start_new_thread( ejecutar_thread, (i,) )
bakery()
    
    
