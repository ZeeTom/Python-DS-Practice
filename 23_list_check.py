def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for ele in lst:
        if not type(ele) == list:
            return False
            
    return True
#all function, like .every() in JS
# return all([type(ele) == list for ele in lst])