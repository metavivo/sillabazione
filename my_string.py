#########################################################################
#                      IMPORT

import nltk

import my_regexp

##############################################################################
#                     GLOBAL VARIABLES

#########################################################################
#                      PARAMETERS

#########################################################################
#                      CLASSES

#########################################################################
#                      FUNCTIONS
#*****************************************************************************
#                  concatenate_string

# Concatenates two strings.

def concatenate_string(string1, string2):

    """Concatenates two strings..

    :param string1: first string. 
    :type string1: string 
    :param string2: second string. 
    :type string2: string 
    :returns: string -- the string obtained by the concatenation

    """ 

    return string1 + string2

#*****************************************************************************
#                  remove_duplicates

# Get the subseq of a string.

def subseq(instring, n1, n2):

    """Get the subseq of a string.

    :param instring: input string. 
    :type instring: string 
    :param n1: first position
    :type n1: integer
    :param n2: second position
    :type 2: integer
    :returns: string -- the list without duplicates. 

    :examples:

      >>> subseq("teacher", 0 3)
      'tea'

    """ 

    return instring[n1:n2]

#*****************************************************************************
#                  find

# Find the first position of a substring inside a string.

def find(substring, mainstring):
    """Find the first position of a substring inside a string.

    :param substring: the input substring
    :type mainstring: string
    :param mainstring: the string where to search the substring
    :type substring: string 
    :returns: integer -- the position of the substring. 

    :examples:

monty.find('Python')

      >>> find('Python', 'Monty Python')
      6

    """ 

    return mainstring.find(substring)

#*****************************************************************************
#                  string_downcase

# Puts a string in lower case.

def string_downcase(instring):

    """Puts a string in lower case.

    :param instring: input string. 
    :type instring: string 
    :returns: string -- output string

    :examples:

      >>> string_downcase("Rome")
      'rome'

      >>> string_downcase("Barack Obama")
      'barack obama'


    """ 

    return instring.lower()

#*****************************************************************************
#                  string_upcase

# Puts a string in upper case.

def string_upcase(instring):

    """Puts a string in upper case.

    :param instring: input string. 
    :type instring: string 
    :returns: string -- output string

    :examples:

      >>> string_upcase("Rome")
      'ROME'

      >>> string_downcase("Barack Obama")
      'BARACK OBAMA'


    """ 

    return instring.upper()

#*****************************************************************************
#                  stringlist_to_string

# Transform a list of string in a string using a token as separator.

def stringlist_to_string(stringlist, sep):

    """Transform a list of string in a string using a token as separator.

    :param stringlist: input string list
    :type stringlist: list
    :returns: string -- output string

    :examples:

    >>> stringlist_to_string2(["a", "b"], "|")
    'a|b'


    """ 

    if (stringlist == []):
        return ''
    elif (len(stringlist) == 1):
        return stringlist[0]
    else:
#        return stringlist[0] + sep + stringlist_to_string2(stringlist[1:len(stringlist)], sep)
        i = 0
        accum = stringlist[0]
        i = 1
        while i < len(stringlist):
            accum = accum + sep + stringlist[i]
            i = i + 1
        return accum

#*****************************************************************************
#                  string_trim

# Trim a string from the given token

def string_trim(instring, token):
    
    """Trim a string from the given token

    :param instring: input string. 
    :type instring: string 
    :param token: input token
    :type token: string
    :returns: string -- trimmed string

    :examples:
      >>> string_trim("  The dog  ")
      'The dog'
    """ 
    if instring == '':
        return instring
    else:
        step1 = my_regexp.replace_regexp(instring, '^' + token + '+', '')
        step2 = my_regexp.replace_regexp(step1, token + '+' + '$', '')
        return step2
    
#*****************************************************************************
#                  check_string

def check_string(in_obj):
    return isinstance(in_obj, str)
    
#########################################################################
#                      INSTRUCTIONS

#------------------------------------------------------------------------
