#SEARCH:


#Sequential Search

def sequentialSearch(lista, item):
    index = 0
    found = False
    
    while index < len(lista) and not found:
        if lista[index] == item:
            found = True
        else:
            index += 1
            
    return found
    
#Binary Search


#SORT:


#Bubble Sort


#Selection Sort


#Insertion Sort


#Shell Sort


#Merge Sort


#Quick Sort


#HASHING:


#Space to tests cases:

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))

