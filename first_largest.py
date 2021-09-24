"""
Python program to find the largest element and its location.
"""

def largest_element(a, loc = False):
    """ Return the largest element of a sequence a.
    """
    maxval = a[0]
    val_loc = 0
    try:
        for i in range(1, len(a)):
            if a[i]> maxval:
                maxval = a[i]
                val_loc = i
    except TypeError:
        print("Values must all be of the same type")
        return
    except:
        print("Unidentified error")
        return

    if loc==True:
        return maxval, val_loc
    return maxval




if __name__ == "__main__":

    a = [1,2,'a',2,1]
    print("Largest element is {:}".format(largest_element(a)))
