
Source Code:

def FibRec(a):  

   if a <= 1:  

       return a  

   else:  

       return(FibRec(a-1) + FibRec(a-2))  

 aterms = int(input("Enter the terms? ")) 

  
if aterms <= 0:  

   print("Please enter a positive integer")  

else:  

   print("Fibonacci sequence:")  

   for z in range(aterms):  

       print(FibRec(z))

Output:

Enter the terms?

5

0 1 1 2 3
