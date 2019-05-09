# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:12:32 2019

@author: thompson
"""

def checkString(s):
    if (s == "MU"):
        return True
    else:
        return False
        
def rule1(stringList):
    if (parent[-1] == 'I'):
        child = parent + 'U'
        if (checkString(child)):
            return True
    return False

def applyRules(stringList, operationList):   
    parent = stringList[-1]    
    
    if (operationList[-1] == 1):
        rule1(stringList)
        
    
        
    

    


myString = ""