"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
    """ done. """
    for i,v in enumerate(mylist):
        if v == key:
            return i
    return -1

def test_linear_search():
    """ done. """
    assert linear_search([1,2,3,4,5], 5) == 4
    assert linear_search([1,2,3,4,5], 1) == 0
    assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
    """ done. """
    return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
    """
    Recursive implementation of binary search.
    
    Params:
      mylist....list to search
      key.......search key
      left......left index into list to search
      right.....right index into list to search

    Returns:
      index of key in mylist, or -1 if not present.
    """
    if right >= left:
        x = (right +left)//2
        if mylist[x] < key:
            return _binary_search (mylist, key, x + 1, right)
        elif mylist[x] > key:
            return _binary_search (mylist, key, left, x - 1)
            
        else:
            return x
    else:
        return -1
                
    ### TODO

    pass

def test_binary_search():
    assert binary_search([1,2,3,4,5], 5) == 4
    assert binary_search([1,2,3,4,5], 1) == 0
    assert binary_search([1,2,3,4,5], 6) == -1
    ### TODO: add two more tests here.

    assert binary_search([1,2,3,4,5], 2) == 1
    assert binary_search([1,2,3,4,5], 3) == 2
  
    pass


def time_search(search_fn, mylist, key):

    """
    Return the number of milliseconds to run this
    search function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds.
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """

    ##print(mylist.sort())
    start = time.time()
    search_fn(mylist,key)
    LVar = time.time()
    legnth = (LVar - start) * 1000

    return legnth
    ### TODO
    pass

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
     
    """"
    Compare the running time of linear_search and binary_search
    for input sizes as given. The key for each search should be
    -1. The list to search for each size contains the numbers from 0 to n-1,
    sorted in ascending order.

    You'll use the time_search function to time each call.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """

    tuple = []
    for n in sizes:
        mylist = range(int(n))
        legnthL = time_search(linear_search, mylist, -1)
        legnthB = time_search(binary_search, mylist, -1)
        tuple.append((n, legnthL, legnthB))
    return tuple

    ### TODO
    pass

def print_results(results):
    """ done """
    print(tabulate.tabulate(results,
        headers=['n', 'linear', 'binary'],
        floatfmt=".3f",
        tablefmt="github"))

def test_compare_search():
    res = compare_search(sizes=[10, 100])
    print_results(res)
    assert res[0][0] == 10
    assert res[1][0] == 100
    assert res[0][1] < 1
    assert res[1][1] < 1

    
