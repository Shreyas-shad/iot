# Python code to find factorial 
num =int(input("Enter number to find factorial ")) #taking user input to find find factorial
factorial = 1
  
for i in range(1,num+1): 
    factorial = factorial * i #factorial formula
      
print ("The factorial is : ",end="") 
print (factorial ) #print factorial

