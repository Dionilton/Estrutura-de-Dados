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

def binarySearch(lista, item):
    found = False
    first = 0
    last = len(lista) - 1
    
    while first <= last and not found:
        mid = (first + last) // 2
        
        if lista[mid] == item:
            found = True
        else:
            if lista[mid] < item:
                first = mid + 1
            else:
                last = mid - 1
    
    return found

def recursiveBinarySearch(lista, item):
    if len(lista) == 0:
        return False
    else:
        mid = len(lista) // 2
        if lista[mid] == item:
            return True
        else:
            if lista[mid] < item:
                return recursiveBinarySearch(lista[mid+1:], item)
            else:
                return recursiveBinarySearch(lista[:mid], item)

#Hashing:

def hash(xstring, tablesize):
    sum = 0
    for pos in range(len(xstring)):
        sum = sum + ord(xstring[pos])
    
    return sum%tablesize

#checkpoint: Hashing Self Check

#SORT:


#Bubble Sort


#Selection Sort


#Insertion Sort


#Shell Sort


#Merge Sort


#Quick Sort


#Space to tests cases:

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(recursiveBinarySearch(testlist, 3))
print(recursiveBinarySearch(testlist, 13))

#Temp Note:

'''
900:               Ind:
    250(n.n.)          0
    150(TdG)           1
    150(V-P-F)         2
    50(Fn.)            3
    300(m.f.):         4
        200(hlp-m)
        100(RE)

'''

lista = [250,150,150,50,300]
total = 0

for i in range(len(lista) - 1):
    total += lista[i]

print(f'Total: {total}')

#Temp Note:
