#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Alessandro Valitutti

# Last version date: 14 Aug 2022

#########################################################################
#                      IMPORT

import re

##############################################################################
#                     GLOBAL VARIABLES

#########################################################################
#                      PARAMETERS

#########################################################################
#                      CLASSES

#########################################################################
#                      FUNCTIONS
#*****************************************************************************
#                  match_regexp

# Match a string with a regular expression

def match_regexp(regexp, str):
    """Replace a regular expression in a string.

    :param regexp: regular expression to use in the matching
    :type regexp: regular expression
    :param str: string to use in the matching
    :type str: string
    :returns: boolean -- True if the matching succeeds, False otherwise

    :examples:

    >>> match_regexp('ca.', 'Casa')
    False
    >>> match_regexp_nocase('ca.', 'Casa')
    True


    """ 
    return bool(re.search(regexp, str))

#*****************************************************************************
#                  match_regexp_nocase

# Match a string with a regular expression (case insensitive)

def match_regexp_nocase(regexp, str):
    """Replace a regular expression in a string (case insensitive.

    :param regexp: regular expression to use in the matching
    :type regexp: regular expression
    :param str: string to use in the matching
    :type str: string
    :returns: boolean -- True if the matching succeeds, False otherwise

    :examples:

      >>> bool(re.search("hi", "abcdefghijkl"))
      True

    """ 
    return bool(re.search(regexp, str, re.I))

#*****************************************************************************
#                  replace_regexp

# Replace a regular expression in a string.

def replace_regexp(string, regexp, repl):
    """Replace a regular expression in a string.

    :param regexp: regular expression to use in the replacement
    :type regexp: regular expression
    :param repl: replacement expression
    :type repl: string
    :param string: string where the replacement is applied
    :type string: string
    :returns: string -- new string obtained with the replacement

    :examples:
      >>> replace-regexp("the dogAis red", r'(^[^A]+?)A(.*?)', r"\\1----\\2")
      'the dog----is red'
      >>> replace_regexp("caaaasioioioioapppp", "^([^s]+?)([^a]+)(.*)$", "\\\\1---\\\\2---\\\\3")
      'caaaa---sioioioio---apppp'


    """ 
    return re.sub(regexp, repl, string)

#*****************************************************************************
#                  replace_regexp_nocase 

# Replace a regular expression in a string  (case insensitive)

def replace_regexp_nocase(string, regexp, repl):
    pattern = re.compile(regexp, re.IGNORECASE)
    return pattern.sub(repl, string)

#*****************************************************************************
#                  search_string

# Search a string in a file and returns the list of lines containing it.

def search_string(pattern, filename):
    """Search a pattern in a file and returns the list of lines containing it.

    :param pattern: input string
    :type pattern: string
    :param filename: input file
    :type filename: string
    :returns: list -- the list of lines containing the pattern

    """ 
    f = open(filename, 'r')
    r=[]
    for line in f:
        if re.search(pattern,line):
            r.append(line)
    return r

#*****************************************************************************
#                  search_string_nocase

# Search a string in a file (case insensitive) and returns the list of
# lines containing it.

def search_string_nocase(pattern, filename):
    """Search a string in a file (case insensitive) and returns the list of lines containing it.

    :param pattern: input string
    :type pattern: string
    :param filename: input file
    :type filename: string
    :returns: list -- the list of lines containing the pattern

    """ 
    f = open(filename, 'r')
    r=[]
    for line in f:
        if re.search(pattern,line, re.IGNORECASE):
            r.append(line)
    return r

#*****************************************************************************
#                  search_word

# Search a string in a file and returns the list of lines containing it.

def search_word(word, filename):
    """Search a word in a file and returns the list of lines containing it.

    :param word: input word
    :type word: string
    :param filename: input file
    :type filename: string
    :returns: list -- the list of lines containing the word

    """ 
    f = open(filename, 'r')
    r=[]
    pattern1 = "[^a-zA-Z]+" + word + "\\b"
    pattern2 = "\\b" + word + "[^a-zA-Z]+"
    for line in f:
        if re.search(pattern1 ,line) or re.search(pattern2 ,line) :
            r.append(line)
    return r

#*****************************************************************************
#                  split_regexp

# Split a string according to a given token.

def split_regexp(regexp, instring):
    """Split a string according to a given token.

    :param regexp: given regular expression
    :type regexp: regular expression
    :param instring: input string
    :type instring: string
    :returns: list -- the list of strings splitted by the token

    :examples:
      >>> split_regexp(" ", "a b c")
      ['a', 'b', 'c']

    """ 
#    return instring.split(regexp)
    return re.split(regexp, instring)

#*****************************************************************************
#                  split_regexp_nocase

# Split a string according to a given token (case insensitive).

def split_regexp_nocase(regexp, instring):
    """Split a string according to a given token (case insensitive)

    :param regexp: given regular expression
    :type regexp: regular expression
    :param instring: input string
    :type instring: string
    :returns: list -- the list of strings splitted by the token

    :examples:
      >>> split_regexp(" ", "a b c")
      ['a', 'b', 'c']

    """ 
    return re.compile(regexp, re.IGNORECASE).split(instring)

#*****************************************************************************
#                  string_trim

# Removes a given token from the sides of a string.

def string_trim(token, instring):
    """Removes a given character from the sides of a string.

    :param token: given character
    :type token: string
    :param instring: input string
    :type instring: string
    :returns: string -- the string obtained through the trimming

    :examples:
      >>> string_trim(" ", " dog ")
      'dog'

    """ 
    outstring = replace_regexp(instring, '^' + token + '*', '')
    outstring = replace_regexp(outstring, token + '*$', '')
    return outstring

#*****************************************************************************
#                  add_backslash_to_regexp_chars

# Add a backslash to the special characters of regular expressions, contained in the input string:   ? ) ( \ . * [

def add_backslash_to_regexp_chars(instring):
    """Add a backslash to the special characters of regular expressions, contained in the input string:   ? ) ( \ . * [

    :instring: input string
    :type instring: string
    :returns: string -- the string where each special character is preceded by backslash

    :examples:
    >>> instring = 'asfa111000_-? ) ( \ . * ['


    """ 
    step1 = replace_regexp(instring, '\?', '\?')
    step2 = replace_regexp(step1, '\(', '\\(')
    step3 = replace_regexp(step2, '\)', '\\)')
    step4 = replace_regexp(step3, '\.', '\.')
    step5 = replace_regexp(step4, '\*', '\*')
    step6 = replace_regexp(step5, '\+', '\+')
    step7 = replace_regexp(step6, '\[', '\[')
    return step7

#########################################################################
#                      INSTRUCTIONS

#------------------------------------------------------------------------
