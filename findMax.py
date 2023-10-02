# CSC 349-01, Fall 2023)
# Noa Kehle and Andrew Okerlund
# Lab 1


"""
    findMaxLinear:
        finds the maximum value in an array of integers using a linear search method
    Parameters:
        parameter1 (a = array): the array used to find the max
    Returns:
        (tmp = int): the maximum integer in the array
"""
def findMaxLinear(a):
    tmp = a[0]  # temporary max

    for i in a:  # linearly go through the whole list
        if tmp < i:
            tmp = i

    return tmp

""" 
    findMaxLinearWithCount:
        finds the maximum value in an array of integers using a linear search method and counts the number of comparrisons
    Parameters:
        parameter1 (a = array): the array used to find the max 
    Returns:
        return 1 (int): the maximum integer in the array 
        return 2 (int): the number of comparisons made
"""

def findMaxLinearWithCount(a):
    tmp = a[0]  # temporary max
    cnt = 0     # count
    l = len(a)  # length

    for i in range(1, l): # linearly go through the list
        if tmp < a[i]:
            tmp = i
        cnt += 1

    return tmp, cnt     # returns a tuple

""" 
    findMaxDNC:
        finds the maximum value in an array of integers using a divide and conquer approach
    Parameters:
        parameter1 (a): the array used to find the max 
        parameter2 (i): lowerBound index 
        parameter3 (j): upperBound index 

    Returns:
        return1 (int): the maximum integer in the array 
"""

def findMaxDNC(a, i, j): # (array, lowerBound, upperBound)

    if a[i] == a[j]:    # base case
        return a[i]

    mid = (i + j) // 2  # midpoint of the array leaning on the left side
    left = findMaxDNC(a, i, mid)    # recrsive call to the left half
    right = findMaxDNC(a, mid + 1, j)  # recrsive call to the right half

    return max(left, right)

""" 
    findMaxDNCWithCount:
        finds the maximum value in an array of integers using a divide and conquer approach and counts comps
    Parameters:
        parameter1 (a): the array used to find the max 
        parameter2 (i): lowerBound index 
        parameter3 (j): upperBound index 

    Returns:
        return1 (int): the maximum integer in the array 
        return2 (int): the amount of comparisons
"""

def findMaxDNCWithCount(a, i, j):

    if a[i] == a[j]:    # base case
        return a[i], 0  # 0 comparrisons if there is only one

    mid = (i + j) // 2  # midpoint of the array leaning on the left side
    left, comp_left = findMaxDNCWithCount(a, i, mid)    # recrsive call to the left half
    right, comp_right = findMaxDNCWithCount(a, mid + 1, j)  # recrsive call to the right half

    return max(left, right), comp_left + comp_right + 1     # adds the comparissons of both halves and 1 more for the final

""" 
    findSecondLinear:
        finds the second max value in an array of integers using a linear approach
    Parameters:
        parameter1 (a): the array used to find the max 

    Returns:
        return1 (int): the second maximum integer in the array 
"""

def findSecondLinear(a):
    largest = a[0]
    cmp = list()    # list of numbers compared to the largest

    for i in range(1, len(a)):
        if a[i] > largest:
            cmp.clear()         # clear the list if a new largest is found
            cmp.append(largest) # append the one it was compared to
            largest = a[i]      # update the largest
        else:
            cmp.append(a[i])

    res = findMaxDNC(cmp, 0, len(cmp) - 1)  # sort through the compared values

    return res

""" 
    findSecondLinear:
        finds the second max value in an array of integers using a linear approach and counts comps
    Parameters:
        parameter1 (a): the array used to find the max 

    Returns:
        return1 (int): the second maximum integer in the array 
        return2 (int): number of comparisons
"""
def findSecondLinearWithCount(a):
    largest = a[0]
    cmp = list()
    cnt = 0

    for i in range(1, len(a)):
        if a[i] > largest:
            cmp.clear()         # clear the list if a new largest is found
            cmp.append(largest) # append the one it was compared to
            largest = a[i]      # update the largest
        else:
            cmp.append(a[i])
        cnt += 1

    res = findMaxDNCWithCount(cmp, 0, len(cmp) - 1)     # sort through the list of compared values

    return res[0], cnt + res[1]

""" 
    findMaxDNCWithComps:
        finds the list of numbers that are compared to the largest value in an array
    Parameters:
        parameter1 (a): the array used to list
        parameter2 (i): lowerBound index 
        parameter3 (j): upperBound index 

    Returns:
        return1 (int): array of numbers being compared to the largest (a[0] = largest element)
"""

def findMaxDNCWithComps(a, i, j):

    if a[i] == a[j]:     # base case
        cmp = list()
        cmp.append(a[i])    # start with the first item
        return cmp

    mid = (i + j) // 2
    cmp_left = findMaxDNCWithComps(a, i, mid)       # recurive call on left half
    cmp_right = findMaxDNCWithComps(a, mid + 1, j)  # recurive call on right half

    if cmp_left[0] > cmp_right[0]:      # if the left halves' largest value > the right halves' largest
        cmp_left.append(cmp_right[0])   # add the right's largest to the left halves' cmp list
        return cmp_left
    else:
        cmp_right.append(cmp_left[0])   # if the left halves' largest value < the right halves' largest
        return cmp_right

""" 
    findSecondDNC:
        finds the second largest number by calling findMaxDNCWithComps and sifting through the given list
    Parameters:
        parameter1 (a): the array used to list
    Returns:
        return1 (int): second largest number in initial array a 
"""
def findSecondDNC(a):
    cmp = findMaxDNCWithComps(a, 0, len(a) - 1)[1:]     # get the list of numbers compared to the largest
    if len(cmp) < 1:    # if the initial list is of length 1
        return a[0]
    else:
        return findMaxLinear(cmp)

""" 
    findSecondDNCWithCount:
        finds the second largest number by calling findMaxDNCWithComps and sifting through the given list and counts comps
    Parameters:
        parameter1 (a): the array used to list
    Returns:
        return1 (int): second largest number in initial array a
        return2 (int): the number of comparrisons
"""
def findSecondDNCWithCount(a):
    cmp = findMaxDNCWithComps(a, 0, len(a) - 1)[1:]     # get the list of numbers compared to the largest
    if len(cmp) < 1:    # if the initial list is of length 1
        return a[0], 0
    else:
        return findMaxLinear(cmp), findMaxLinearWithCount(cmp)[1] + len(a) - 1
