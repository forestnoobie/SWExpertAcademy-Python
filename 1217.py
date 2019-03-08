# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:56:12 2019

@author: Nakyilkim
"""

memoi = {}
def recursiveMul(number, times):
    #Base Case
    if times == 0 :
        memoi[0] = 1
        return 1
    
    if times == 1:
        memoi[1] = 1
        return number
    
    if times in memoi.keys():
        return memoi[times]
    
    if times %2 == 0 :
        time1 = times/2 
        time2 = times/2
    else:
        time1 = (times+1)/2
        time2 = (times-1)/2

    
    result = recursiveMul(number, time1) *recursiveMul(number, time2)
    memoi[times] = result
    return result