def IsMountain(arr):
    peak = max(arr)
    peak_index = arr.index(peak)
    if peak_index == 0:
        return False
    elif peak_index == len(arr)-1:
        return False
    else:
        aux_a, aux_b = 0, 0
        for i in range(peak_index):
            if arr[i] < arr[i+1]:
                aux_a += 1
        for i in range(peak_index,len(arr)-1):
            if arr[i] > arr[i+1]:
                aux_b += 1
        if (aux_a == peak_index) and (aux_b == len(arr) - 1 - peak_index):
            return True 
        else:
            return False 
def IsValley(arr):
    trough = min(arr)
    trough_index = arr.index(trough)
    if trough_index == 0:
        return False
    elif trough_index == len(arr) - 1:
        return False
    else:
        aux_a, aux_b = 0, 0
        for i in range(trough_index):
            if arr[i] > arr[i+1]:
                aux_a += 1
        for i in range(trough_index,len(arr)-1):
            if arr[i] < arr[i+1]:
                aux_b += 1
        if (aux_a == trough_index) and (aux_b == len(arr) - 1 - trough_index):
            return True 
        else:
            return False
def LandscapeType(arr):
    pass


