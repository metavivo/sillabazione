#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Alessandro Valitutti

# Last version date: 15 Aug 2022

#########################################################################
#                      IMPORT

import my_string
import my_regexp
import my_list
import input_output
import my_random

from eccezioni import *

#########################################################################
#                     GLOBAL VARIABLES

global vowels
global consonants

##############################################################################
#                      CLASSES
#************************************************************************

#########################################################################
#                      FUNCTIONS
#************************************************************************
#                      sdfasfa

#------------------------------------------------------------------------

#************************************************************************
#                  split_syls
   
def split_syls(s):
    step1 = my_string.string_trim(s, ' ')
    step2 = encode_syl(step1)
    step3 = [x[0] for x in step2]
    step4 = my_string.stringlist_to_string(step3, '')
    step5 = dividi(step4)
    if step5 == None:
#        print('caso 1')
        return ''
    else:
#        print('caso 2')
        step6 = decode_syl(step5, step2)
        return step6
"""



"""
#------------------------------------------------------------------------

def encode_syl(s):
    if s == "":
        return s
    elif check_consonant(s[0]):
        if s[1:] == '':
            return [[s[0], s[0]]]
        else:
            return [[s[0], s[0]]] + encode_syl(s[1:])
    elif check_vowel(s[0]):
        token1 = my_regexp.replace_regexp_nocase(s, '^(' + v() + '+).*', '\\1')
        token2 = my_regexp.replace_regexp_nocase(s, '^' + v() + '+(.*)', '\\1')
        if token2 == '':
            return [[s[0], token1]]
        else:
            return [[s[0], split_vowels(token1)]] + encode_syl(token2)

#------------------------------------------------------------------------

def split_vowels(s):
    if s == "" or len(s) == 1:
        return s
    elif s[0] == 'i' or s[0] == 'u':
        return s
    else:
        return s[:1] + '-' + s[1:]
    
#------------------------------------------------------------------------

def decode_syl(s, tab):
    if s == '':
        return s
    elif s[0] == '-':
        return '-' + decode_syl(s[1:], tab)
    else:
        return tab[0][1] + decode_syl(s[1:], tab[1:])
"""

sciacquare
scialacquare
    
"""
#************************************************************************
#                      dividi

def dividi(s):

#    print('-----------------')
#    print('s = ', s)    
    
    # eccezioni: io, criptico, feldspato
    
    if s in eccezioni:
#        print('R1')
        return eccezioni[s]
    
    # parole intere
    
    # ''
    elif s == '':
#        print('R2a')
        return s

    # a, e, i, o, u
    elif len(s) == 0 or len(s) == 1:
#        print('R2b')
        return s
        
    # one syllable: al lo, il
    elif len(s) == 2:
#        print('R2c')
        return s
    
    elif len(s) == 3:
        
#        print('len 3')
    
        # est, alt
        if my_regexp.match_regexp_nocase('^' + v() + c() + c() + '$', s):
#            print('R2c1')
            return s

        # sto
        elif my_regexp.match_regexp_nocase('^' + 's' + c() + v() + '$', s):
#            print('R2c2')
            return s

        # tra, fra
        elif my_regexp.match_regexp_nocase('^' + c() + liq() + v() + '$', s):
#            print('R2c3')
            return s

        # nel, don, per, doc, dop
        elif my_regexp.match_regexp_nocase('^' + c() + v() + c() + '$', s):
#            print('R2c4')
            return s

        # che
        elif my_regexp.match_regexp_nocase('^' + c() + c() + v() + '$', s):
#            print('R2c5')
            return s
        

  #  elif len(s) == 4:
        
#        print('len 4')
    
    # (stro)
    elif my_regexp.match_regexp_nocase('^' + 's' + c() + liq() + v() + '$', s):
#        print('R3')
        return s
        
    # "Khan"
    elif my_regexp.match_regexp_nocase('^' + c() + c() + v() + c() + '$', s):
#        print('R4')
        return s
	# vlad, gran, tran
    elif my_regexp.match_regexp_nocase('^' + c() + c() + v() + c() + '$', s):
#        print('R5')
        return s

    # left patterns

    # L7

	# scritto, sfratto
    # scrittura, distratto, strattone, strattonare, sbroccare
    elif my_regexp.match_regexp_nocase('^s' + c() + liq() + v() + '(' + c() + ')(\\1)' + v(), s):
#        print('L7')
#        print(s[:5], '- +', s[5:])
#        return s[:5] + '-' + dividi(s[5:])
    
#    elif my_regexp.match_regexp_nocase(***, s):
#        return s[:n] + '-' + dividi(s[n:])

    # L6

    # strano
    # scrupolo
    elif my_regexp.match_regexp_nocase('^s' + c() + liq() + v() + c() + v(), s):
#        print('L6a')
#        print(s[:4], '- +', s[4:])
        return s[:4] + '-' + dividi(s[4:])

    # larghi, parchi
    # narghilè
    elif my_regexp.match_regexp_nocase('^' + c() + v() + liq() + '[cg]h' + v(), s):
#        print('L6b')
#        print(s[:3], '- +', s[3:])
        return s[:3] + '-' + dividi(s[3:])

	# sgherro
    elif my_regexp.match_regexp_nocase('^' + scgh() + v() + '(' + c() + ')(\\1)' + v(), s):
#        print('L6c')
#        print(s[:5], '- +', s[5:])
        return s[:5] + '-' + dividi(s[5:])

    # sghembo, schermo
    # scharmato
    elif my_regexp.match_regexp_nocase('^' + scgh() + v() + liq() + c(), s):
#        print('L6d')
#        print(s[:5], '- +', s[5:])
        return s[:5] + '-' + dividi(s[5:])

	# schema, schifo
    # schifoso, schifosamente
    elif my_regexp.match_regexp_nocase('^' + scgh() + v() + c() + v(), s):
#        print('L6e')
#        print(s[:4], '- +', s[4:])
        return s[:4] + '-' + dividi(s[4:])

    # L5

	# Sandro, contro
    # Alessandro
    elif my_regexp.match_regexp_nocase('^' + c() + v() + liq() + c() + liq(), s):
#        print('L5a')
#        print(s[:3], '- +', s[3:])
        return s[:3] + '-' + dividi(s[3:])

	# astro, astratto
    # astrakhan
    elif my_regexp.match_regexp_nocase('^' + v() + 's' + c() + liq() + v(), s):
#        print('L5b')
#        print(s[:1], '- +', s[1:])
        return s[:1] + '-' + dividi(s[1:])

    # splende
    # splendido, splendore, strambo, sfranto
    elif my_regexp.match_regexp_nocase('^s' + c() + liq() + v() + liq(), s):
#        print('L5c')
#        print(s[:5], '- +', s[5:])
        return s[:5] + '-' + dividi(s[5:])

    # (strakhan)
    # strabello, strasexy
    elif my_regexp.match_regexp_nocase('^s' + c() + liq() + v() + c(), s):
#        print('L5d')
#        print(s[:4], '- +', s[4:])
        return s[:4] + '-' + dividi(s[4:])

	# Alessandro
    elif my_regexp.match_regexp_nocase('^' + v() + c() + v() + '(' + c() + ')(\\1)' + v(), s):
#        print('L5e')
#        print(s[:1], '- +', s[1:])
        return s[:1] + '-' + dividi(s[1:])

    # trema, prete, prego, prima, brina, clima, drago, trave, vlado
    # fragola, tremare, stomaco, brivido
    # pronome, preposto
    elif my_regexp.match_regexp_nocase('^[bcdfgpstvz]' + c() + v() + c() + v(), s):
#        print('L5e')
#        print(s[:3], '- +', s[3:])
        return s[:3] + '-' + dividi(s[3:])

	# brocca, stallo, grosso, dramma, grillo
    elif my_regexp.match_regexp_nocase('^' + c() + c() + v() + '(' + c() + ')(\\1)' + v(), s):
#        print('L5f')
#        print(s[:4], '- +', s[4:])
        return s[:4] + '-' + dividi(s[4:])

	# Trento, pranzo, grande, grembo
    elif my_regexp.match_regexp_nocase('^' + c() + c() + v() + liq() + c(), s):
#        print('L5g')
#        print(s[:4], '- +', s[4:])
        return s[:4] + '-' + dividi(s[4:])

	# carpa, pende, talpa
	# vicenda, avvincente, avvicendamento, pendenza --> CHECK
    elif my_regexp.match_regexp_nocase('^' + c() + v() + liq() + c() + v(), s):
#        print('L5h')
#        print(s[:3], '- +', s[3:])
        return s[:3] + '-' + dividi(s[3:])

    # L4

    # passa, disse, detto, pacco, matto, palla, gallo
	# (lessandro)
    # lessema, parroco, villetta
    elif my_regexp.match_regexp_nocase('^' + c() + v() + '(' + c() + ')(\\1)' + v(), s):
#        print('L4a')
#        print(s[:3], '- +', s[3:])
        return s[:3] + '-' + dividi(s[3:])

	# (tacqu)
    elif my_regexp.match_regexp_nocase('^' + c() + v() + 'cq', s):
#        print('L4b')
#        print(s[:3], '- +', s[3:])
        return s[:3] + '-' + dividi(s[3:])
    
    # asse, esso, atto, alla, osso
    # attico
	# apparato, atterrare, attillato
    elif my_regexp.match_regexp_nocase('^' + v() + '(' + c() + ')(\\1)', s):
#        print('L4c')
#        print(s[:2], '- +', s[2:])
        return s[:2] + '-' + dividi(s[2:])

	# asta
    # ascoli, ascolana, aspirina
    elif my_regexp.match_regexp_nocase('^' + v() + 's' + c() + v(), s):
#        print('L4d')
#        print(s[:1], '- +', s[1:])
        return s[:1] + '-' + dividi(s[1:])

	# ocra
	# Abramo, 
    # aprire
    # griturismo
    elif my_regexp.match_regexp_nocase('^' + v() + c() + liq() + v(), s):
#        print('L4d')
#        print(s[:1], '- +', s[1:])
        return s[:1] + '-' + dividi(s[1:])

    # L3
    
    # alba, orto, orco
	# articolo, albino, Urbino
    # ambo, onda, orlo
	# imprudente, improbabile
    elif my_regexp.match_regexp_nocase('^' + v() + liq() + c(), s):
#        print('L3a')
#        print(s[:2], '- +', s[2:])
        return s[:2] + '-' + dividi(s[2:])
    
	# (acqu)
    elif my_regexp.match_regexp_nocase('^' + v() + 'cq', s):
#        print('L3b')
#        print(s[:2], '- +', s[2:])
        return s[:2] + '-' + dividi(s[2:])

    # Cristo, presto, crisma
    # tristezza 
    elif my_regexp.match_regexp_nocase('^' + c() + liq() + v(), s):
#        print('L3c')
#        print(s[:3], '- +', s[3:])
        return s[:3] + '-' + dividi(s[3:])

	# avido, Irina, Ugolino, obolo
	# Aladino, Ugolino, aliscafo
    elif my_regexp.match_regexp_nocase('^' + v() + '(' + c() + v() + ')+', s):
#        print('L3d')
#        print(s[:3], '- +', s[3:])
        return s[:1] + '-' + dividi(s[1:])

    # L2

	# casa, mela
	# patatine, vicenda, diritto
    elif my_regexp.match_regexp_nocase('^' + c() + v(), s):
#        print('L2')
#        print(s[:2], '- +', s[2:])
        return s[:2] + '-' + dividi(s[2:])

    else:
#        print('String not recognized')
        return 'GAP!'

"""

spartano

tasche, taschino, maschera, mascherato

schema, sghembo

Ferrari, villino

raro, rarità
    
astalavista
    
turismo, agriturismo

imprudente, improbabile

"""
#************************************************************************
#                      check_vowel

def check_vowel(x):
    return check_vowel1(x, vowels)

#------------------------------------------------------------------------
    
def check_vowel1(x, vowels):
    if my_list.member(my_string.string_downcase(x), vowels):
        return True
    else:
        return False

"""
check_vowel('l')
Out[60]: False

check_vowel('a')
Out[61]: True
"""
#************************************************************************
#                      liq

def liq():
    return '[lmnr]'

#************************************************************************
#                      scgh

def scgh():
    return 's[cg]h'

#************************************************************************
#                      check_consonant

def check_consonant(x):
    return check_consonant1(x, consonants)

"""
check_vowel('l')
Out[60]: False

check_vowel('a')
Out[61]: True
"""
#------------------------------------------------------------------------
    
def check_consonant1(x, consonant):
    if my_list.member(my_string.string_downcase(x), consonants):
        return True
    else:
        return False

"""    
check_consonant('a')
Out[63]: False

check_consonant('l')
Out[64]: True

check_consonant('L')
Out[65]: True
"""
#************************************************************************
#                      v

def v():
  return '[aeiouàáèéìíòóùú]'

#************************************************************************
#                      c

def c():
  return '[^a^e^i^o^u^à^á^è^é^ì^í^ò^ó^ù^ú]'

#************************************************************************
#                      double_c

def double_c():
  return '[bb|cc|dd|ff|gg|ll|mm|nn|pp|rr|ss|tt|vv|zz]'

#************************************************************************
#                  check_word_single_vowel

def check_word_single_vowel(w):
    
#    print(w)
    
    # 1) '^' + v() + '$' =  a, e, i
    if my_regexp.match_regexp_nocase('^' + v() + '$' , w):
#        print('R1')
        return True
    
    # 2) '^' + c() + '$' =  l, p, b
    if my_regexp.match_regexp_nocase('^' + c() + '$' , w):
#        print('R2')
        return True
    
    # 3) '^' + c() + c() + '$' = bb
    if my_regexp.match_regexp_nocase('^' + c() + c() + '$', w):
#        print('R3')
        return True
    
    # 3) '^' + v() + c() + '$' = ab
    if my_regexp.match_regexp_nocase('^' + v() + c() + '$', w):
#        print('R3')
        return True
    
    # 4) '^' + c() + v() + '$' = ba
    if my_regexp.match_regexp_nocase('^' + c() + v() + '$', w):
#        print('R4')
        return True
    
    # 5)  bba, cab
    if my_regexp.match_regexp_nocase(c(), w[:1]) and check_word_single_vowel(w[1:]):
#        print('R5')
        return True
    
    # 6)  abba, acab
    if my_regexp.match_regexp_nocase(v(), w[:1]) and my_regexp.match_regexp_nocase(c(), w[:2]) and check_word_single_vowel(w[2:]):
#        print('R6')
        return True
    
    else:
        return False
"""
catamarano
assassinassero
supercalifragilistichespiralidoso
"""   
#************************************************************************
#                  check_word_more_vowels

def check_word_more_vowels(w):
    return my_regexp.match_regexp_nocase(v() + v(), w)

#########################################################################
#                      INSTRUCTIONS
#------------------------------------------------------------------------

vowels = ['a', 'e', 'i', 'o', 'u', 'à', 'á', 'è', 'é', 'ì', 'í', 'ò', 
          'ó', 'ù', 'ú', 'w', 'y']

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
              'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']

#------------------------------------------------------------------------

