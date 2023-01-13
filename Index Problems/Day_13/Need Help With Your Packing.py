def CanFit(arr, n):
    
    if sum(arr) < 10*n:
        return True
    else:
        return False
n = 4
arr = [2, 1, 2, 5, 4, 3, 6, 1, 1, 9, 3, 2]
arr = [2, 7, 1, 3, 3, 4, 7, 4, 1, 8, 2]
print(CanFit(arr, n))