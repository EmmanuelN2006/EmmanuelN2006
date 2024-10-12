import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns

def bubble_sort(L):
    n = len(L)
    for i in range(n - 1):
        for j in range(n - i - 1):
            #operaciones += 1
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                #intercambios += 1
        #print(f"paso {i + 1}: {L}")
    return L
  
def partition(array, low, high):

    '''
    # choose the rightmost element as pivot
    pivot = array[high]
    '''

    '''    
    # choose a random element
    r = randrange(low, high)
    array[r], array[high] = array[high], array[r]
    pivot = array[high]
    '''
    
    
    # choose median of 3
    m = int((low + high) / 2)
    if array[m] < array[low]: 
        array[low], array[m] = array[m], array[low]
    if array[high] < array[low]:
        array[low], array[high] = array[high], array[low]
    if array[m] < array[high]:
        array[m], array[high] = array[high], array[m] 
    pivot = array[high]
    

 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            array[i], array[j] = array[j], array[i]
 
    # Swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]
 
    # Return the position from where partition is done
    return i + 1

def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        #print(f"Lista de la izquierda: {data[:pi]}")
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
        #print(f"Lista de la derecha: {data[pi:]}")
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

def insertSort(L):
    i = 1
    while i < len(L):
        j = i
        while j > 0 and L[j - 1] > L[j]:
            #operaciones += 1
            L[j], L[j - 1] = L[j - 1], L[j]
            #intercambios += 1
            j -= 1
        i += 1

def Selectsort(L):
    for i in range(len(L) - 1):
        min = i
        for j in range(i + 1, len(L)):
            #operaciones += 1
            if (L[min] > L[j]):
                min = j
    if min != i:
        L[min], L[i] = L[i], L[min]
        #intercambios += 1
        #operaciones += 1

num_elements = np.arange(1000, 5001, 1000)
size = num_elements.size
print(size)
#print(num_elements)
t_bubble = np.zeros(size)
t_selection = np.zeros(size)
t_insertion = np.zeros(size)
t_quick_sort = np.zeros(size)

for i, n in enumerate(num_elements) :
    # crear el vector desordenado
    vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
    # Burbuja
    #copiamos el vector para ordenar
    vector_b = np.copy(vector_ord)
    print(vector_b)
    # tomamos el tiempo
    t_inicio = perf_counter_ns()
    bubble_sort(vector_b)
    t_final = perf_counter_ns()
    print(vector_b)
    t_bubble[i] = t_final - t_inicio
    print(f"Tiempo burbuja para {n} elementos = {t_final - t_inicio}")
    
    # Quick Sort
    #copiamos el vector para ordenar
    vector_q = np.copy(vector_ord)
    print(vector_q)
    # tomamos el tiempo
    t_inicio = perf_counter_ns()
    size = vector_q.size
    quickSort(vector_q, 0, size - 1)
    t_final = perf_counter_ns()
    print(vector_q)
    t_quick_sort[i] = t_final - t_inicio
    print(f"Tiempo quicksort para {n} elementos = {t_final - t_inicio}")
    
    # InsertSort
    #copiamos el vector para ordenar
    vector_r = np.copy(vector_ord)
    print(vector_r)
    # tomamos el tiempo
    t_inicio = perf_counter_ns()
    insertSort(vector_r)
    t_final = perf_counter_ns()
    print(vector_r)
    t_insertion[i] = t_final - t_inicio
    print(f"Tiempo Insert para {n} elementos = {t_final - t_inicio}")
    
    #Selection sort
    #Copiamos el vector para ordenar
    vector_y = np.copy(vector_ord)
    print(vector_y)
    # tomamos el tiempo
    t_inicio = perf_counter_ns()
    Selectsort(vector_y)
    t_final = perf_counter_ns()
    print(vector_y)
    t_selection[i] = t_final - t_inicio
    print(f"Tiempo Selection para {n} elementos = {t_final - t_inicio}")
 
t_total= perf_counter_ns()
print(f"Tiempo total de las operaciones = {t_total}")
plt.plot(num_elements, t_quick_sort, "b-", num_elements, t_bubble, "r-", num_elements, t_insertion, "g-", num_elements, t_selection, "y-")
plt.show()