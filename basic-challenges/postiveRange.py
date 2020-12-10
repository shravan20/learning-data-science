def filterPositive(arr):
     arr = [x for x in arr if x>=0]
     return arr


print(filterPositive([1,-2,-3,4]))  # [1,4]

print(filterPositive([-1,2,3,-4]))  # [2,3]
