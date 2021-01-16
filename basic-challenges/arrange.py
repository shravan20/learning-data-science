def shuffleNumbers(arr):

    temp = [0 for k in range(len(arr))] 
    pCounter = 0
    
    for index in range(len(arr)):
         if(arr[index]>0):
             temp[pCounter] = arr[index]
             pCounter+=1 

    if(pCounter == len(arr)):
        return temp

    for index in range(len(arr)):
         if(arr[index]<0):
             temp[pCounter] = arr[index]
             pCounter+=1 
    
    return temp
    


a=[-1, -1, -3, -2, -7, -5, -11, -6]
print(shuffleNumbers(a))
