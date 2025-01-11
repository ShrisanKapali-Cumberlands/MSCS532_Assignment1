# Assignment 1 - Python program for Insesrtion Sort in monotonically decreasing order
# Shrisan Kapali
# Student Id - 005032249


# First Defining a function for insertion sort
def monotonically_decreasing_insertion_sort(array):
    # As insertion sort begins with index 1, create a for loop starting index 1 and length of array
    for i in range(1, len(array)):
        # The key is the value of array at position i
        key = array[i]
        # The object to compare is the value of array at position i-1
        j = i - 1
        # Now decreasing the value of j and comparing and sorting the arrays
        # If the value of key is greater than the value of array at position j, swap the values that way the greater interger is at earlier index
        while j >= 0 and key > array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
