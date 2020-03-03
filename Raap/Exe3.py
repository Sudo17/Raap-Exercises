
#Defining a Dictionary
n = int(input("enter a value:"))
dict = {}

#Creating a user defined dictionary with input values
for i in range(n):
    keys = input()
    values = int(input())
    dict[keys] = values
print(dict)

#%%
#Sum of values
def returnSum(dict): 
      
     sum = 0
     for i in dict: 
           sum = sum + dict[i] 
       
     return sum
  
# Driver Function  
print("Sum :", returnSum(dict)) 