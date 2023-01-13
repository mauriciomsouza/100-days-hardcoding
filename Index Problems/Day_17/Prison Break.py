import random

def inverter(arr):
    for i in range(len(arr)):
        if arr[i] == 1:
            arr[i] = 0 
        else:
            arr[i] = 1
    return arr


def freedPrisoners(arr):
    counter = 0 
    cursor = 0
    for cursor in range(len(arr)):
        if arr[cursor] == 1:
            print(f"You free the prisoner in the cell {cursor+1}")
            counter += 1
            arr = inverter(arr)
        
    return counter





arr = random.choices([0,1],k=random.randint(3,7))
print(arr)
print(freedPrisoners(arr))