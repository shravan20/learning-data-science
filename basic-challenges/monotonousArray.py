def isMonotonic(arr):
	return arr == sorted(arr) or arr == sorted(arr, reverse=True)


print('isMonotonic([6, 5, 4, 4]):',isMonotonic([6, 5, 4, 4]))
print('isMonotonic([5,15, 20, 10]):', isMonotonic([5,15, 20, 10]))
print('isMonotonic([5,15, 20, 30]):',isMonotonic([5,15, 20, 30]))
print('isMonotonic([30,20,15,10]):',isMonotonic([30,20,15,10]))
print('isMonotonic([30,20,15,20]):',isMonotonic([30,20,15,20]))
print('isMonotonic([30,20,5,15,20]):',isMonotonic([30,20,5,15,20]))
