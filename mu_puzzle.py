# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:12:32 2019

@author: thompson
"""
from treelib import Tree

def checkString(s):
    return (s == 'MU')

def rule1(tree, node, count):
    if (tree[node].tag[-1] == 'I'):
        string = tree[node].tag + 'U'
        tree.create_node(string, count, parent=tree[node].identifier, data=[1])        
        count += 1
        return [checkString(string), count]
    return [False, count]

def rule2(tree, node, count):
    string = tree[node].tag + tree[node].tag[1:]
    tree.create_node(string, count, parent=tree[node].identifier, data=[2])
    count += 1
    return [checkString(string), count]

def rule3(tree, node, count):
    for i in range(len(tree[node].tag) - 2):
        if (tree[node].tag[i] == 'I' and tree[node].tag[i+1] == 'I' and tree[node].tag[i+2] == 'I'):
            string = tree[node].tag[:i] + 'U' + tree[node].tag[i+3:]
            tree.create_node(string, count, parent=tree[node].identifier, data=[3,i])
            count += 1
            if checkString(string):
                return [True, count]
    return [False, count]

def rule4(tree, node, count):
    for i in range(len(tree[node].tag) - 1):
        if (tree[node].tag[i] == 'U' and tree[node].tag[i+1] == 'U'):
            string = tree[node].tag[:i] + tree[node].tag[i+2:]
            tree.create_node(string, count, parent=tree[node].identifier, data=[4,i])
            count += 1
            if checkString(string):
                return [True, count]
    return [False, count]

def buildTree(tree):
    current_node = 0
    node_count = 1
    limit = 1000000
    
    while node_count < limit:
        #tree.show()

        [found, node_count] = rule1(tree, current_node, node_count)
        if found:
            break
        [found, node_count] = rule2(tree, current_node, node_count)
        if found:
            break
        [found, node_count] = rule3(tree, current_node, node_count)
        if found:
            break
        [found, node_count] = rule4(tree, current_node, node_count)
        if found:
            break
        
        current_node += 1
    
    #tree.show()
    if node_count < limit:
        print("Found!")
    else:
        print("Failed")
        
        
    
tree = Tree()
tree.create_node("MI", 0)
buildTree(tree)

