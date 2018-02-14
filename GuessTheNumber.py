#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:45:58 2018

@author: sbk
"""

import random

number = random.randint(1,100)
guess = 0
guessCount = 0

while guess == 0:
    gNumber = input("Guess the Number between 1 and 100 : ")
    if (gNumber == number):
        print('Nice Work, You Guessed it correctly')
        print("You took", guessCount+1, "chances to guess the number")
        guess = 1
    elif (gNumber > number):
        print('Try Smaller Number')
        guessCount +=1      
    else:
        print('Try Bigger Number')
        guessCount +=1
    