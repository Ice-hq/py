import time
import random 

matrix_comp, matrix_swap = 0, 0
MATRIX = False
def shellSort(array): #сортировка Шелла
    global matrix_swap # для матрицы
    global matrix_comp
    try:
        array = [int(i) for i in array] 
    except ValueError:
        pass
    start_time = time.time() #начало отсчёта
    comparison_count = 0 
    swap_count = 0
    n = len(array)
    k = n//2
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            
            while j >= interval and array[j - interval] > temp:
                print('interval is ', interval)
                print('comparing: ', array[j - interval], ' and ', temp)
                print('while')
                print(array)
                
                comparison_count += 1
                print(comparison_count)
                array[j] = array[j - interval]
                swap_count += 1
                j -= interval
            if (array[j - interval] > temp) == False:
                print('interval is ', interval)
                print('comparing: ', array[j - interval], ' and ', temp)
                print('if')
                comparison_count += 1
                print(comparison_count)
                print (array)
            array[j] = temp
            # swap_count += 1
        k -= 1
        interval = 2**k -1
    if MATRIX == True:
        matrix_swap += swap_count
        matrix_comp += comparison_count
    if MATRIX != True:
        print("--- %s seconds ---" % (time.time() - start_time))
        print("comparisons = ", comparison_count)
        print("swaps = ", swap_count)
    return array


array1 = [-2, 2, -5, 0]
array2 = [-2, 2, 0, -5]
array3 = [0, 2, -5, -2]

shellSort(array1)
print(array1)
# print('')
# shellSort(array2)
# print('')
# shellSort(array3)
