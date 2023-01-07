def ProgressMile(arr):
    progress = 0
    for i in range(len(arr) - 1):

        if arr[i+1] > arr[i]:
            progress +=1
    return progress


print(ProgressMile([10, 10]))