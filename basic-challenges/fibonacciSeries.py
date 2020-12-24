
def fibonacciNumbers(num):
 
    f1 = 0
    f2 = 1
    if (num < 1):
        return
    print(f1, end=" ")
    for x in range(1, num):
        print(f2, end=" ")
        next = f1 + f2
        f1 = f2
        f2 = next
  
n=0
while(n>=0):
   n = int(input("\nHow many terms? "))
   fibonacciNumbers(n);
 
"""
Output

How many terms? 0

How many terms? 1
0 
How many terms? 2
0 1 
How many terms? 3
0 1 1 
How many terms? 4
0 1 1 2 
How many terms? 5
0 1 1 2 3 
How many terms? 6
0 1 1 2 3 5 
How many terms? 7
0 1 1 2 3 5 8 
How many terms? 8
0 1 1 2 3 5 8 13 
How many terms? 9
0 1 1 2 3 5 8 13 21 
How many terms? 10
0 1 1 2 3 5 8 13 21 34 
How many terms? 
"""
