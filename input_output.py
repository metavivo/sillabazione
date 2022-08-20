# Alessandro Valitutti

# Module: input_output

# Last version date: 30 Jul 2022

##############################################################################
#                     IMPORT

import os.path

import my_regexp

##############################################################################
#                     FUNCTIONS
#*****************************************************************************
#                   read_file_to_list

# Loads a list from a file.

def read_file_to_list(filename):
    """Load a list from a file.

    :param filename: Input file. 
    :type filename: string 
    :returns: list -- the list stored in the file. 

    """ 
    f = open(filename, 'r')
    raw = f.read()
    lines = raw.splitlines()
    return lines

"""
OTHER WAYS

1) readlines
    
# Python code to
# demonstrate readlines()
 
L = ["Geeks\n", "for\n", "Geeks\n"]
 
# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()
 
# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

-----------
2) readline
    
# Python program to
# demonstrate readline()
 
L = ["Geeks\n", "for\n", "Geeks\n"]
 
# Writing to a file
file1 = open('myfile.txt', 'w')
file1.writelines((L))
file1.close()
 
# Using readline()
file1 = open('myfile.txt', 'r')
count = 0
 
while True:
    count += 1
 
    # Get next line from file
    line = file1.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    print("Line{}: {}".format(count, line.strip()))
 
file1.close()

-------

filepath = 'Iliad.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1

-------

(BEST OPTION!)

myfile = open("demo.txt", "r")
myline = myfile.readline()
print(myline)
myfile.close()

---------------------
3) for loop
    
# Python program to
# demonstrate reading files
# using for loop
 
L = ["Geeks\n", "for\n", "Geeks\n"]
 
# Writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()
 
# Opening file
file1 = open('myfile.txt', 'r')
count = 0
 
# Using for loop
print("Using for loop")
for line in file1:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
 
# Closing files
file1.close()





"""
#*****************************************************************************
#                   read_file_to_string

# Loads a list from a file.

def read_file_to_string(filename):
    f = open(filename, 'r')
    raw = f.read()
    return raw

#*****************************************************************************
#                   stringlist_to_file

# Reads the content of the input file and loads each line on a list.

def stringlist_to_file(inlist, outfile):
    """Reads the content of the input file and loads each line on a list.

    :param inlist: input list
    :type inlist: list
    :param outfile: output filename
    :type outfile: string

    """ 
    f = open(outfile, 'a')
    f.writelines('\n'.join(inlist) + '\n')
    f.close()

#*****************************************************************************
#                   printlist

# Prints a list of items.

def printlist(inlist):
    """Prints a list of items.

    :param inlist: input list
    :type inlist: list

    """ 
    for l in inlist:
        print(l)

#*****************************************************************************
#                   save_pairs

# Save a dictionary of string pairs where the separator is "|".

def save_pairs(pairs, fileout):
    """Save a dictionary of string pairs where the separator is "|".

    :param pairs: list of pairs
    :type pairs: dictionary
    :param fileout: filein
    :type fileout: file

    """ 
    step1 = [x[0] + '|' + x[1] for x in pairs]
    stringlist_to_file(step1, fileout)

#*****************************************************************************
#                   load_pairs

# Load a list of pairs from a file where the separator is "|".

def load_pairs(filein):
    """Load a list of pairs from a file where the separator is "|".

    :param filein: filein
    :type filein: file
    :returns: list -- the list of pairs stored in the file. 

    """ 
    step1 = read_file_to_list(filein)
    step2 = [my_regexp.split_regexp('\|', x) for x in step1]
    return step2

#*****************************************************************************
#                   load_pairs_sep

# Load a list of pairs from a file where the given separator.

def load_pairs_sep(filein, sep):
    """Load a list of pairs from a file where the given separator.

    :param filin: input file
    :type filein: file
    :param sep: separator
    :type sep: string
    :returns: list -- the list of pairs.

    """ 
    step1 = read_file_to_list(filein)
    step2 = [my_regexp.split_regexp(sep, x) for x in step1]
    return step2

#*****************************************************************************
#                   print_rows

# Shows a table with the required spacing.

def print_rows(rows, n):
    max_length = max([max([len(str(x)) for x in row]) for row in rows])
    width = max_length + n
    new_rows = [[str(x) + (width - len(str(x))) * ' ' 
                 for x in row] for row in rows]
    stringlist = [''.join(row) for row in new_rows]
    outstring = '\n'.join(stringlist)
    print(outstring)
    
#*****************************************************************************
#                   n_rows_file

# Get the number of rows in the input file.

def n_rows_file(filein):
    return sum(1 for line in open(filein))

#*****************************************************************************
#                   check_if_file_exists

def check_if_file_exists(f):
    return os.path.exists(f)

#*****************************************************************************
#                   create_empty_file_append

# Create empty file. If the file already exists, it is not canceled.

def create_empty_file_append(f):
    open(f, 'a').close()

#*****************************************************************************
#                   create_empty_file_cancel

# Create empty file. If the file already exists, it is canceled.

def create_empty_file_cancel(f):
    open(f, 'w').close()

##############################################################################
#                     INSTRUCTIONS
#*****************************************************************************

#-----------------------------------------------------------------------------

