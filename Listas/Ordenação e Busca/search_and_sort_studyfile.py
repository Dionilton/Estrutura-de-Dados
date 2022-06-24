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

def orderedSequentialSearch(lista, item):
    index = 0
    found = False
    stop = False
    
    while index < len(lista) and not found and not stop:
        if lista[index] == item:
            found = True
        else:
            if lista[index] > item:
                stop = True
            else:
                index +=1
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

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))

