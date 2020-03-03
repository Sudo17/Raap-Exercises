def DuplicatesWithCount(listOfElems):
    dictOfElems = dict()
# Iterate over each element in list
    for elem in listOfElems:
# If element exists in dict then increment its value else add it in dict
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1    
# Filter key-value pairs in dictionary. Keep pairs whose value is greater than 1
    dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}

    return dictOfElems

#%%
#Enter the array of numbers
print('Enter the values')
listOfElems = [int(i) for i in input().split()]

# Dictionary containing duplicate elements in list and their frequency count
dictOfElems = DuplicatesWithCount(listOfElems)     

for key, value in dictOfElems.items():
        print(key , ' :: ', value)