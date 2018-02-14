#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:33:49 2018

@author: sbk
"""

story = '''
{} is a good friend of {}. Once they went to {} , 
but they had no idea about {}.
So they started {} in the {}. Finally, they ended at {}. 
It was {} experience for {} and {}.
'''

def main() :
    name = []
    name.append(raw_input('Enter a Person Name :'))
    name.append(raw_input('Enter a Person Name :'))
    place = raw_input('Enter a place name eg: Playground, Library.. :')
    activity = []
    activity.append(raw_input('Enter an Activity eg: Running, Swimming.. :'))
    activity.append(raw_input('Enter an Activity eg: Running, Swimming.. :'))
    time = raw_input('Enter a place, eg:Forest, River..')
    city = raw_input('Enter a city Name:')
    adjective = []
    adjective.append(raw_input('Enter an Adjective, eg: Bad, Good, Sad...'))
    
    mad_lib = story.format(name[0],name[1],place,activity[0],activity[1],
                           time,city,adjective[0],name[0],name[1])
    print(mad_lib)
    
main()  
