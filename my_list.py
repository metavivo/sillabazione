# Alessandro Valitutti

# Last version date: 25/03/22

##############################################################################
#                      IMPORT

from my_regexp import *

##############################################################################
#                     GLOBAL VARIABLES

##############################################################################
#                      PARAMETERS

##############################################################################
#                      CLASSES

##############################################################################
#                      FUNCTIONS
#*****************************************************************************
#                  remove_duplicates

# Removes duplicates from a list.

def remove_duplicates(l):
    """Removes duplicates from a list.

    :param l: Input list. 
    :type l: list 
    :returns: list -- the list without duplicates. 

    """ 
    accum = []
    for el in l:
        if el not in accum:
            accum.append(el)
    return accum

#*****************************************************************************
#                  remove_duplicates_fast

# Removes duplicates from a list.

def remove_duplicates_fast(l):
    out = list(set(l))
    return out

#*****************************************************************************
#                  remove_duplicates_fast_nocase

# Removes duplicates from a list.

def remove_duplicates_fast_nocase(l):
    d = {}
    for x in l:
        d[x.lower()] = 0
    out = []
    for x in d.keys():
        out = out + [x]
    return out

#*****************************************************************************
#                  append

# Concatenates two lists.

def append(list1, list2):
    """Concatenates two lists.

    :param list1: first list
    :type list1: list 
    :param list2: second list
    :type list2: list 
    :returns: list -- the list obtained concatenating list1 and list2


    :examples:

    >>> list1 = ['a', 'b']

    >>> list2 = ['c', 'd']

    >>> append(list1, list2)
    ['a', 'b', 'c', 'd']

    >>> list1
    ['a', 'b']

    >>> list2
    ['c', 'd']

    """ 
    outlist = []
    for el in list1:
        outlist.append(el)
    for el in list2:
        outlist.append(el)
    return outlist

#*****************************************************************************
#                  cons

# Appends an element as the beginning of a list.

def cons(el, inlist):
    """Appends an element as the beginning of a list.

    :param el: element to be appended
    :type el: object
    :param inlist: input list
    :type inlist: list 
    :returns: list -- the list obtained appending el at the beginning of inlist


    :examples:

    >>> my_list.cons(1, [2, 3])
    [1, 2, 3]

    >>> my_list.cons('a', ['b', 'c'])
    ['a', 'b', 'c']

    """ 
    outlist = append([], inlist)
    outlist.insert(0, el)
    return outlist

#*****************************************************************************
#                  apply

def apply(op, arg_list):
    return op(*arg_list)

#*****************************************************************************
#                  map

def map(op, inlist):
    return [apply(op, [x]) for x in inlist]

#*****************************************************************************
#                  get_combination

def get_combination(set1, set2, op):
    if set1 == []:
        return []
    else: 
        return [op(set1[0], x) for x in set2] + get_combination(set1[1:], set2, op)

#*****************************************************************************
#                  accumulate

# Accumulate the elements of a list.

def accumulate(op, initial, inlist):
    """Accumulate the elements of a list.

    :param op: operator by which the accumulation is performed
    :type op: function
    :param initial: the initial list
    :type initial: list
    :param inlist: input list
    :type inlist: list
    :returns: list -- the list obtained through the accumulation

    :examples: 

      >>> accumulate(lambda x,y: x + y, 0, [1,2,3,4])
      10

      >>> accumulate(lambda x,y: append(x, y), [], [['a'], ['b', 'c']])
      ['a', 'b', 'c']
    

    """ 
    l = inlist
    accum = initial
    if inlist == []:
        return initial
    else:
        while len(l) > 0:
            accum = apply(op, [accum, l[0]])
            l = l[1:len(l)] 
    return accum

#*****************************************************************************
#                  cdr

# Gets the list without the first element. Returns the empty list if
# the input list is empty.

def cdr(inlist):
    """Gets the list without the first element. Returns the empty list if the input list is empty.

    :param inlist: input list
    :type inlist: list
    :returns: list -- the list without the first element (if the list is not empty), the empty list otherwise

    :examples: 

      >>> cdr([])
      []
      >>> cdr([1])
      []
      >>> cdr([1,2])
      [2]
      >>> cdr([1,2,3])
      [2, 3]

    """ 
    if inlist == []:
        return inlist
    else:
        return inlist[1:len(inlist)]

#*****************************************************************************
#                  car

# If the list is not empty, returns the first element, otherwise returns the empty list.

def car(inlist):
    """If the list is not empty, returns the first element, otherwise returns the empty list.

    :param inlist: input list
    :type inlist: list
    :returns: object -- if the list is not empty, it is the first element, otherwise it is the empty list

    :examples: 

      >>> car([])
      []
      >>> car([1])
      1
      >>> car([1,2])
      1
      >>> car([1,2,3])
      1

    """ 
    if inlist == []:
        return inlist
    else:
        return inlist[0]

#*****************************************************************************
#                  cadr

def cadr(inlist):
    return car(cdr(inlist))

#*****************************************************************************
#                  filter

# Filters the elements of a list according to a given predicate.

def filter(op, inlist):
    """Filters the elements of a list according to a given predicate.

    :param op: operator by which the filtering is performed
    :type op: function
    :param inlist: input list
    :type inlist: list
    :returns: list -- the list obtained through the filtering

    :examples:
    
      >>> filter(lambda x: x > 3, [1,2,3,4,5,6])
      [4, 5, 6]

    """ 
    l = inlist
    accum = []
    if inlist == []:
        return inlist
    else:
        while len(l) > 0:
            if apply(op, [l[0]]):
                accum = append(accum, list(car(l)))
            l = cdr(l)
    return accum

#*****************************************************************************
#                  filter_new

def filter_new(op, inlist):
    l = inlist
    accum = []
    if inlist == []:
        return inlist
    else:
        while len(l) > 0:
#            if apply(op, [l[0]]):
            if op(*[l[0]]):
                accum = append(accum, list(car(l)))
            l = cdr(l)
    return accum

#filter(lambda x: x > 3, [1,2,3,4,5,6])

#*****************************************************************************
#                  filter_py

def filter_fast(op, inlist):
    return list(filter(op, inlist))[0]
#    return [x for x in inlist if op]

#*****************************************************************************
#                  filter_count

# Filters the elements of a list according to a given predicate. In this version, a counter of remaining items is shown.

def filter_count(op, inlist):
    """Filters the elements of a list according to a given predicate. In this version, a counter of remaining items is shown.

    :param op: operator by which the filtering is performed
    :type op: function
    :param inlist: input list
    :type inlist: list
    :returns: list -- the list obtained through the filtering

    :examples:
    
      >>> filter_count(lambda x: x > 3, [1,2,3,4,5,6])
    6
    5
    4
    3
    2
    1
      [4, 5, 6]

    """ 
    l = inlist
    print(len(l))
    accum = []
    if inlist == []:
        return initial
    else:
        while len(l) > 0:
            print(len(l))
            if apply(op, [l[0]]):
                accum = append(accum, list(car(l)))
            l = cdr(l)
    return accum

#*****************************************************************************
#                  filter_count_new

# Filters the elements of a list according to a given predicate. In this version, a counter of remaining items is shown.

def filter_count_new(op, inlist):
    """Filters the elements of a list according to a given predicate. In this version, a counter of remaining items is shown.

    :param op: operator by which the filtering is performed
    :type op: function
    :param inlist: input list
    :type inlist: list
    :returns: list -- the list obtained through the filtering

    :examples:
    
      >>> filter_count(lambda x: x > 3, [1,2,3,4,5,6])
    6
    5
    4
    3
    2
    1
      [4, 5, 6]

    """ 
    l = inlist
    print(len(l))
    accum = []
    if inlist == []:
        return initial
    else:
        while len(l) > 0:
            print(len(l))
            if op(*[l[0]]):
                accum = append(accum, list(car(l)))
            l = cdr(l)
    return accum

#*****************************************************************************
#                  list

# Puts an elements in a empty list.

def list(el):
    """Puts an elements in a empty list.

    :param el: input element
    :type op: object
    :returns: list -- the list containing the input element

    :examples:
    
      >>> list(1)
      [1]
    
      >>> list([1])
      [[1]]


    """ 
    return cons(el, [])

#*****************************************************************************
#                  sort

# Gets a list as input and returns a sorted list.

def sort(inlist):
    """Gets a list as input and returns a sorted list.

    :param inlist: input list
    :type inlist: list
    :returns: list -- the sorted list

    :examples:
    
      >>> sort(['b', 'c', 'a']
      ['a', 'b', 'c']
    

    sorted([[3],[2],[1]], key=my_list.car, reverse=True)
    Out[85]: [[3], [2], [1]]

    sorted([[3],[2],[1]], key=lambda x: my_list.car(x), reverse=True)
    Out[86]: [[3], [2], [1]]

    """ 
    outlist = sorted(inlist)
    return outlist

#*****************************************************************************
#                  member

# Checks if an element is a member of a list.

def member(el, inlist):
    """Checks if an element is a member of a list.

    :param el: element to check in the list
    :type el: object
    :param inlist: input list
    :type inlist: list
    :returns: boolean -- true is the element is contained in the list

    :examples: 

    >>> member(1, [1, 2])
    True

    >>> member(1, [3, 2])
    False


    """ 
    if(el in inlist):
        return True
    else:
        return False

#*****************************************************************************
#                  member_pred

# Checks if an element is a member of a list with the given matching predicate.

def member_pred(el, inlist, pred):
    """Checks if an element is a member of a list with the given matching predicate.

    :param el: element to check in the list
    :type el: object
    :param inlist: input list
    :type inlist: list
    :param pred: predicate
    :type pred: function
    :returns: boolean -- true is the element is contained in the list

    :examples: 

    >>> member_pred(1, [1,2,3], lambda x, y: x == y)
    True

    >>> member_pred('a', ['a'], lambda x, y: my_regexp.match_regexp(x, y))
    True

    >>> member_pred('house', ['casa', 'tetto', 'house'], lambda x, y: my_regexp.match_regexp(x, y))
    True

    >>> member_pred('House', ['casa', 'tetto', 'house'], lambda x, y: my_regexp.match_regexp(x, y))
    False

    >>> member_pred('House', ['casa', 'tetto', 'house'], lambda x, y: my_regexp.match_regexp_nocase(x, y))
    True

    """ 
    if len(filter(lambda x: pred(el, x), inlist)) > 0:
        return True
    else:
        return False

#*****************************************************************************
#                  member_nocase

def member_nocase(el, inlist):
#    return member_pred(el, inlist, lambda x y: x.lower() == y.lower())
    return member_pred(el, inlist, lambda x, y: x.lower() == y.lower())

#*****************************************************************************
#                  member_string_nocase

# Checks if an string is contained in a list of strings (case insensitive).

def member_string_nocase(string, stringlist):
    """Checks if an string is contained in a list of strings (case insensitive).

    :param string: string to check
    :type string: string
    :param stringlist: list of strings
    :type inlist: list
    :returns: boolean -- true is the element is contained in the list

    :examples: 

    >>> member('casa', ['tetto', 'casa'])
    True

    >>> member('Casa', ['tetto', 'casa'])
    False

    >>> member_string_nocase('casa', ['tetto', 'casa'])
    True

    >>> member_string_nocase('Casa', ['tetto', 'casa'])
    True

    >>> member_string_nocase('Casaa', ['tetto', 'casa'])
    False

    """
    string1 = add_backslash_to_regexp_chars(string)
    return member_pred(string1, stringlist, lambda x, y: match_regexp_nocase('^' + x + '$', y))
    
#*****************************************************************************
#                  make_sequence

# Generate a sequence with an input element repeated a given number of times.

def make_sequence(elem, n):

    """Generate a sequence with an input element repeated a given number of times

    :param elem: input element
    :type object: elem
    :param n: number of times instring should be concatenated
    :type n: int
    :returns: list -- output list

    """ 
    if (n == 1):
        return [elem]
    else:
        return append(list(elem), make_sequence(elem, n - 1))
    
#*****************************************************************************
#                  last

# Returns the last element of a list, or None if the list is empty.

def last(inlist):
    """Returns the last element of a list, or None if the list is empty.

    :param inlist: input list
    :type inlist: list
    :returns: object

    :examples: 

      >>> last([])
      None
      >>> last([1, 2, 3])
      3

    """ 
    if inlist == []:
        return None
    else:
        return inlist[len(inlist)-1]

#*****************************************************************************
#                  intersection

# Returns the intersection of two lists.

def intersection(list1, list2):
    """Returns the intersection of two lists.

    :param list1: first list
    :type list1: list 
    :param list2: second list
    :type list2: list 
    :returns: list -- intersection of list1 and list2


    :examples:

    >>> list1 = ['a', 'b']

    >>> list2 = ['b', 'c']

    >>> intersection(list1, list2)
    ['b']

    """ 
    step1 = filter(lambda x: member(x, list1), list2)
    return step1

#*****************************************************************************
#                     member_position

# Checks an element in a list and find its first position

def member_position(el, inlist):
    """Checks an element in a list and find its first position.

    :param el: input element
    :type: object
    :param inlist: input list
    :type inlist: list
    :returns: int -- position of the element in the list

    :examples: 
    >>> member_position(1, [])

    >>> member_position(1, [1])
    0

    >>> member_position(1, [1, 2, 3])
    0

    >>> member_position("1", ["1", 2, 3])
    0

    >>> member_position("1", ["1", "2", 3])
    0
    
    >>> member_position("1", [4, "1", "2", 3])
    1

    """
    if inlist == []:
        return None
    else:
        i = 0
        while i < len(inlist) and el != inlist[i]:
            i = i + 1
        if i == len(inlist):
            return None
        else:
            return i
    
##############################################################################
#                      INSTRUCTIONS

#-----------------------------------------------------------------------------


