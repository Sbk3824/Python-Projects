#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 22:52:29 2018

@author: sbk
"""

def fibonacci(n):
    cur = 0
    next = 1
    for i in range(0,n):
        cur,next = next,cur+next
    return cur

fibonacci(36)