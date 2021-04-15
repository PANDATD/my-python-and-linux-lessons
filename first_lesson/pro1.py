#!/bin/env/python3

'''
Problem:
    Get an array from user 
    sort array in accending format 
    without using any builtin method ot funcation  

psudocode:
    Func sortData(array: list)->list:
    len(array)
    sortarray = []
    for i in range(length):
        minData = minArray(array: list)
        append min data to sortarray
        sortarry.append(mindata)
        remove mindata from array 
        array.remove(mindata)
        print Resut 
        
'''

#code

def sortDatainAccending(array: list)->list:
    try:
    
        print()
        print(f"Data after sorting{array}")
        '''
        This funcation takes an array as parameter
        Example :
        sortDatainAccending([99,20,34,65,78])
        --------------------------------------
        (Funcation name ( [parameter] :TYPE list  )   )
        '''
        length = len(array) # This will find the length of an array.
        sortArray = [] # This empty array stores the sorted result.
        for i in range(length):
            
            minData = min(array) # Find the min value from array.
            sortArray.append(minData) # Appending Result in new sorted array.
            array.remove(minData) # Removing minData from array that alrady is beging checked or sorted form previous list.
        print(f"The Sorted data is : {sortArray}")
        print()
    except:
        print("Sorting opretion cannot be done in <int> and <string> data")
        
sortDatainAccending([20,34,5000,23,1,0,0.1,-8,-1,23])
sortDatainAccending(['a','z','c','abc'])
sortDatainAccending(['abc',12,'abc'])
