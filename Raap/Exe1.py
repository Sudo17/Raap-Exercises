#Enter the  value to define he range
print('Enter your value:')
n = int(input());

#%%
#Print 'fizz' ,'buzz' , 'fizzbuzz' for multiples of 3, 5 and 15
for fizzbuzz in range(1,n+1):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)